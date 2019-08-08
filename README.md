# Face Detector Service

This service detect faces in images provided by the cameras.

## Streams

| Name | Input (topic/message) | Output (topic/message) | Description
| --- |--- | --- | --- |
|Face.Detection | **CameraGateway.\d+.Frame** [Image](https://github.com/labviros/is-msgs/blob/modern-cmake/docs/README.md#is.vision.Image) | **SkeletonsDetector.\d+.Detection** [Image](https://github.com/labviros/is-msgs/blob/modern-cmake/docs/README.md#is.vision.Image)|After detection, faces are drew on input image and published for visualization.

## About
It is a machine learning based approach where a cascade function is trained and then used to detect objects in other images. [OpenCV](https://docs.opencv.org/3.4.1/d7/d8b/tutorial_py_face_detection.html) already contains many pre-trained classifiers for face, eyes, smiles, etc. 

You can choose the scale factor, minimal neighboors and minimal size. This options are specified in the [Protocol Documentation](https://github.com/labviros/is-face-detector#protocol-documentation).
## Developing

In case you need to make any change on options protobuf file, will be necessary to rebuild the documentation file related to it. For do that, simply run the script [src/conf/generate_docs.sh](https://github.com/labviros/is-face-detector/blob/master/src/conf/generate_docs.sh).
```shell
cd src/conf/
chmod +x generate_docs.sh
./generate_docs.sh
``` 



 

 

 

 



# Protocol Documentation
<a name="top"></a>

## Table of Contents

- [options.proto](#options.proto)
    - [FaceDetectorOptions](#.FaceDetectorOptions)
    - [HaarCascadeModel](#.HaarCascadeModel)
  
  
  
  




<a name="options.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## options.proto



<a name=".FaceDetectorOptions"></a>

### FaceDetectorOptions
Service Configuration


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| broker_uri | [string](#string) |  |  |
| zipkin_host | [string](#string) |  |  |
| zipkin_port | [uint32](#uint32) |  |  |
| model | [HaarCascadeModel](#HaarCascadeModel) |  | Configurations of the HaarCascade model |






<a name=".HaarCascadeModel"></a>

### HaarCascadeModel



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| model_file | [string](#string) |  | Path of the model |
| scale_factor | [float](#float) |  | The value indicates how much the image size is reduced at each image scale |
| min_neighbors | [uint32](#uint32) |  | How many “neighbors” each candidate rectangle should have |
| min_size | [google.protobuf.ListValue](#google.protobuf.ListValue) |  | The minimum object size |





 

 

 

 



