# Creates a simple streamlit app that will present a button and once pressed will save the image and display on screen

# for the open cv i followed the tutorial here https://towardsdatascience.com/computer-vision-for-beginners-part-3-79de62dbeef7

import streamlit as st
import numpy as np
import cv2

# face detecting function 
def detect_face(img):
    img_2  = img.copy()
    face_rects = face_cascade.detectMultiScale(img_2 , 
                                               scaleFactor = 1.1,
                                               minNeighbors = 3)
    for (x, y, w, h) in face_rects:
        cv2.rectangle(img_2, (x, y), (x+w, y+h), (255, 255, 255), 3)
        
    return img_2, face_rects

# settings for detecting a face 
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

# places a button on screen to take a picture 
if st.button('Take a picture'):
    st.write('picture being processed, please wait...')
  
    # initialize the camera
    cam = cv2.VideoCapture(0)   # Creates a opencv video object 
    s, img = cam.read() # takes a picture and saves it to img
    
    # Checks the picture is valid and displays/saves image  
    if s:    # frame captured without any errors        
        st.write('Raw image') # writes text to the screen
        st.image(img) # Displays the image 
        
        cv2.imwrite("selfie.jpg",img) #save image
        
        # converts images to rgb and gray scale
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # displays the 
        st.write('RGB image') # writes text to screen 
        st.image(img_rgb) # Displays the image 
        st.write('Grey scale image') # writes text to screen 
        st.image(img_gray) # Displays the image

        
        # Detect the face
        roi = img_gray
        roi_detected,face_rects = detect_face(roi) # opencv to detect faces 
        st.write('face detection image, there should be a circle around my face') # writes the text to screen 
        st.image(roi_detected, cmap = 'gray') # displays the image 
        st.write(face_rects) # writes the text to screen