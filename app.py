import cv2 
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import tempfile

def convert_to_rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


st.title('Object Tracking Projects')

video_file = st.file_uploader('Upload a video', type=['mp4', 'avi', 'mov'], key='video_uploader')
if video_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())
    tfile.close()

    col1,col2 = st.columns(2)

    with col1:
        st.header('Masked Video')
        stfram1 = st.empty()
    with col2:
            st.header('Tracked Video')
            stfram2 = st.empty()    

    captures = cv2.VideoCapture(tfile.name)

    background_sub = cv2.createBackgroundSubtractorMOG2()
    
    while captures.isOpened():
        ret, frame = captures.read()
        if not ret:
            break
        fgmask = background_sub.apply(frame)
        (contours, _) = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for i in contours:
            if cv2.contourArea(i) < 500:
                continue

            (x, y, w, h) = cv2.boundingRect(i)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        stfram1.image(caption='Foreground mask', image=fgmask)
        stfram2.image(caption='Tracked object', image=convert_to_rgb(frame))
 
        

    captures.release()
