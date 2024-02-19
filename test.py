import cv2
import mediapipe as mp
import pyautogui

# Initialize mediapipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Open the default camera (usually the built-in webcam)
cap = cv2.VideoCapture(0)

# Set the screen width and height (adjust as needed)
screen_width, screen_height = pyautogui.size()

# Create a window to display the webcam feed
cv2.namedWindow("Hand Tracking and Clicking")

# Initialize variables for click detection
prev_finger_state = 0

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame using mediapipe hands
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get the coordinates of the index finger
            index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            index_x, index_y = int(index_finger.x * screen_width), int(index_finger.y * screen_height)

            # Move the mouse cursor to the index finger position
            pyautogui.moveTo(index_x, index_y)

            # Draw a circle at the index finger position
            cv2.circle(frame, (index_x, index_y), 15, (0, 255, 0), -1)

            # Check for a click gesture (index finger extended)
            finger_state = 1 if index_finger.y < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y else 0

            if finger_state == 1 and prev_finger_state == 0:
                # Perform a click
                pyautogui.click()

            prev_finger_state = finger_state

    # Display the resulting frame
    cv2.imshow("Hand Tracking and Clicking", frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
