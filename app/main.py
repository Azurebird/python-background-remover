import cv2
import mediapipe as mp
import numpy as np

# Initialize mediapipe
mp_selfie_segmentation = mp.solutions.selfie_segmentation
selfie_segmentation = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)

# Store background images in a list
bg_image = cv2.imread("images/cafe.jpeg")

# Create videocapture object to access the webcam
cap = cv2.VideoCapture(0)
while cap.isOpened():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)

cap.release()
cv2.destroyAllWindows()