import cv2  # Import the OpenCV library for image and video processing

def test_camera():
    # Opens the first connected camera (index 0)
    cap = cv2.VideoCapture(0)

    # Checks if the camera was successfully opened
    if not cap.isOpened():
        print("Could not open the camera.")
        return  # Ends the function if the camera cannot be opened

    print("Press 'q' to close the window.")  # Instructions for the user

    # Starts a loop that continuously captures frames from the camera
    while True:
        ret, frame = cap.read()  # Reads the next frame from the camera
        if not ret:  # If the frame could not be read correctly
            print("Error reading frame.")
            break  # Breaks the loop if there is an issue with reading the frame

        # Displays the captured frame in a window
        cv2.imshow("Camera Test", frame)

        # Waits for 1 millisecond for a key press and checks if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break  # Breaks the loop if the user presses the 'q' key

    # Releases the camera resources once the loop ends
    cap.release()

    # Closes all OpenCV windows
    cv2.destroyAllWindows()

# Starts the camera test function when this script is run directly
if __name__ == "__main__":
    test_camera()
