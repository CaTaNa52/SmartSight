# SmartSight Project - Cat Detection

# Import necessary libraries
import cv2                   # OpenCV for image processing and video capture
import numpy as np           # NumPy for numerical operations

# Initialize the Pi Camera (use camera index 0)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("[ERROR] Unable to access the camera.")
    exit()

# Load pre-trained Haar Cascade classifier for full body detection
# Make sure the path to the haarcascade file is correct
cat_cascade = cv2.CascadeClassifier('./assets/haarcascade_fullbody.xml')

# Check if the classifier is loaded properly
if cat_cascade.empty():
    print("[ERROR] Could not load the Haar Cascade classifier.")
    exit()

# Main loop to capture frames and detect cats
while True:
    # Capture frame from the camera
    ret, frame = cap.read()
    
    # If frame is not captured successfully, break the loop
    if not ret:
        print("[ERROR] Failed to capture frame.")
        break

    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect cats (full bodies) in the grayscale image
    cats = cat_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around detected cat faces/bodies
    for (x, y, w, h) in cats:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Blue rectangle

    # Display the resulting frame with detected cats
    cv2.imshow('SmartSight - Cat Detection', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()
