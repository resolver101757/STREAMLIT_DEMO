# this shows the video in streamlit 
# 

import cv2
import numpy as np
import streamlit as st
import time
import sys

# print debugging information
st.write(sys.version_info) 

# Define detect function
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

# Detects faces when passed a image and draws a box around the returned face in the image
def detect_face(img):
    img_copy = img.copy()
    face_rects = face_cascade.detectMultiScale(img_copy ) 
    for (x, y, w, h) in face_rects:
        cv2.rectangle(img_copy, (x, y), (x+w, y+h), (255, 255, 255), 3)
        
    return img_copy

# Call the cam
cap = cv2.VideoCapture(0) 

# ST.button shows the start button
# When pressed it shows a video of the start button
if st.button('Start'):

    cap.set(cv2.CAP_PROP_FPS, 10) # sets frames per second. 
    image_placeholder = st.empty() # 

    while True: 
        # reads the image and stores in image       
        success, image = cap.read()
        if not success: 
            break
        image = detect_face(image) #detects faces and draws a box around the face
        image_placeholder.image(image, channels="BGR") #displays the video of the image

cap.release()