#script works on raspberry pi 
# more information can be found here on aruco 
# https://mecaruco2.readthedocs.io/en/latest/notebooks_rst/Aruco/Projet+calibration-Paul.html#use-of-camera-calibration-to-estimate-3d-translation-and-rotation-of-each-marker-on-a-scene

import numpy as np
import cv2
import cv2.aruco as aruco
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_1000)
    arucoParameters = aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(
        gray, aruco_dict, parameters=arucoParameters)
    frame = aruco.drawDetectedMarkers(frame, corners)
    print(ids)

cap.release()
cv2.destroyAllWindows()