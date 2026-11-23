import cv2 
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title('Object Tracking Projects')

def convert_to_rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# background_sub = cv2.createBackgroundSubtractorMOG2()
# captures = cv2.VideoCapture(r'C:\Users\emsha\Documents\judy\AI-and-ML\ComputerVision\Data\background video _ people _ walking _.mp4')

# while captures.isOpened():
#     ret, frame = captures.read()
#     if not ret:
#         break
#     fgmask = background_sub.apply(frame)
#     (contours, _) = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     for i in contours:
#         if cv2.contourArea(i) < 500:
#             continue

#         (x, y, w, h) = cv2.boundingRect(i)
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
#     cv2.imshow('Foreground mask', fgmask)
#     cv2.imshow('Tracked object', frame)

#     if cv2.waitKey(30) & 0xFF == ord('q'):
#         break

# captures.release()
# cv2.destroyAllWindows() #close all windows
