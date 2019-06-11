import numpy as np
import cv2

cascPath = '/home/luiz/Desktop/is-face-detection/src/haarcascade_frontalface_default.xml'
imagePath = "/home/luiz/Desktop/is-face-detection/src/hodor.jpg"


faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    

# Detect faces in the image
faces = faceCascade.detectMultiScale(gray, 1.3, 5)

print (len(faces))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)