from is_wire.core import Logger
from is_msgs.image_pb2 import Image, ObjectAnnotations
import numpy as np
import cv2
from utils import load_options


class FaceDetector:
    def __init__(self, options):
        self._op = options
        self.faceCascade = cv2.CascadeClassifier(options['cascPath'])
        self.log = Logger("FaceDetection", Logger.DEBUG)
    
    def detect(self, image):
        # Read the image
        self.image = cv2.imread(image)
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.faces = self.faceCascade.detectMultiScale(gray, 1.3, 5)
        self.log.info(f"{len(self.faces)} faces found! :)")


#imagePath = "/home/luiz/Desktop/is-face-detection/src/hodor.jpg"
