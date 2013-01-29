"""
This module is used for testing the opencv2 capabilities
"""


import cv2

#get webcam feed
capture = cv2.VideoCapture(0)


while True:
    #combines VideoCapture.grab() and VideoCapture.retrieve()
    retrieval_value, image = capture.read()

    #shows captured image in a window
    cv2.imshow("webcam", image)

    #will stop capture with capatible webcam
    if cv2.waitKey(10) == 27:
        break
