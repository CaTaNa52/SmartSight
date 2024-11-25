# SmartSight Project - Camera Test

# Import necessary libraries
import cv2  # OpenCV for image processing and video capture

# Initialize the Pi Camera
cap = cv2.VideoCapture(0)  # Open the Pi camera (index 0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("[ERROR] Unable to access the camera.")
    exit()

print("[INFO] Camera is working. Press 'q' to exit.")

# Main loop to capture and display the video feed
while True:
    ret, frame = cap.read()  # Capture frame from the camera

    # If frame is not captured successfully, break the loop
    if not ret:
        print("[ERROR] Failed to capture frame.")
        break

    # Display the captured frame
    cv2.imshow('Camera Test - Press q to Exit', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()
