# for the open cv i followed teh tutorial here https://towardsdatascience.com/computer-vision-for-beginners-part-3-79de62dbeef7
# 


import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
from cv2 import *



# Create the face detecting function 
def detect_face(img):
    img_2  = img.copy()
    face_rects = face_cascade.detectMultiScale(img_2 , 
                                               scaleFactor = 1.1,
                                               minNeighbors = 3)
    for (x, y, w, h) in face_rects:
        cv2.rectangle(img_2, (x, y), (x+w, y+h), (255, 255, 255), 3)
        
    return img_2, face_rects

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')



if st.button('Take a picture'):
    st.write('picture being processed, please wait...')
  
    # initialize the camera
    cam = VideoCapture(0)   # 0 -> index of camera
    s, img = cam.read()
    if s:    # frame captured without any errors
        #namedWindow("cam-test",flags= cv2.WINDOW_GUI_NORMAL)
        st.write('Raw image')
        st.image(img)
        imwrite("filename.jpg",img) #save image
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        st.write('RGB image')
        st.image(img_rgb)
        st.write('Grey scale image')
        st.image(img_gray)

        roi = img_gray
        # Detect the face
        roi_detected,face_rects = detect_face(roi)
        st.write('face detection image, there should be a circle around my face')
        st.image(roi_detected, cmap = 'gray')
        st.write(face_rects)

