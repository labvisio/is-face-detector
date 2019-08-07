import re
import dateutil.parser as dp

from is_wire.core import Logger, Channel, Subscription, Message
from is_wire.core import Tracer, AsyncTransport
from opencensus.ext.zipkin.trace_exporter import ZipkinExporter
from is_msgs.image_pb2 import Image

from .face_detector import FaceDetector
from .service_channel import ServiceChannel
from .image_tools import to_image, to_np, draw_detection
from .utils import load_options


def span_duration_ms(span):
    dt = dp.parse(span.end_time) - dp.parse(span.start_time)
    return dt.total_seconds() * 1000.0


def main():

    service_name = "FaceDetector.Detection"
    re_topic = re.compile(r'CameraGateway.(\w+).Frame')

    op = load_options()
    face_detector = FaceDetector(op.model)

    log = Logger(name=service_name)
    channel = ServiceChannel(op.broker_uri)
    log.info('Connected to broker {}', op.broker_uri)

    max_batch_size = max(100, op.zipkin_batch_size)
    exporter = ZipkinExporter(
        service_name=service_name,
        host_name=op.zipkin_host,
        port=op.zipkin_port,
        transport=AsyncTransport,
    )

    subscription = Subscription(channel=channel, name=service_name)
    subscription.subscribe(topic='CameraGateway.*.Frame')

    while True:
        msg, dropped = channel.consume(return_dropped=True)

        tracer = Tracer(exporter, span_context=msg.extract_tracing())
        span = tracer.start_span(name='detection_and_render')
        detection_span = None

        with tracer.span(name='unpack'):
            im = msg.unpack(Image)
            im_np = to_np(im)

        with tracer.span(name='detection') as _span:
            faces = face_detector.detect(im_np)
            detection_span = _span

        with tracer.span(name='render_pack_publish'):
            img_rendered = draw_detection(im_np, faces)
            rendered_msg = Message()
            rendered_msg.topic = re_topic.sub(r'FaceDetector.\1.Rendered', msg.topic)
            rendered_msg.pack(to_image(img_rendered))
            channel.publish(rendered_msg)

        span.add_attribute('Detections', len(faces))
        tracer.end_span()
        log.info('detections = {:2d}, dropped_messages = {:2d}', len(faces), dropped)
        log.info('took_ms = {{ detection: {:5.2f}, service: {:5.2f}}}',
                 span_duration_ms(detection_span), span_duration_ms(span))


if __name__ == "__main__":
    main()