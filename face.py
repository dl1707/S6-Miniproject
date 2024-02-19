import cv2

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
video=cv2.VideoCapture(0)
def facebox(vid):
    gray_img=cv2.cvtColor(vid,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_img, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces

while True:
    result, video_frame = video.read()  # read frames from the video
    if result is False:
        break  # terminate the loop if the frame is not read successfully

    faces = facebox(video_frame)  # apply the function we created to the video frame

    cv2.imshow("My Face Detection Project", video_frame)  # display the processed frame in a window named "My Face Detection Project"

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()

#Hand recognition
'''
import cv2
import mediapipe as mp
# Initialize mediapipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
# Open the default camera (usually the built-in webcam)
cap = cv2.VideoCapture(0)
cv2.namedWindow("Hand Gesture Recognition")    # Create a window to display the webcam feed
while True:
    ret, frame = cap.read()    # Capture frame-by-frame
    frame = cv2.flip(frame, 1)    # Flip the frame horizontally for a later selfie-view display
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)    # Convert the BGR image to RGB
    results = hands.process(rgb_frame)    # Process the frame using mediapipe hands
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the frame
            for landmark in hand_landmarks.landmark:
                height, width, _ = frame.shape
                x, y = int(landmark.x * width), int(landmark.y * height)
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

            # Count fingers based on hand landmarks
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
            middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
            ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
            pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y

            finger_count = sum(1 for tip in [thumb_tip, index_tip, middle_tip, ring_tip, pinky_tip] if tip < 0.7)

            # Display the finger count
            cv2.putText(frame, f"Fingers: {finger_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow("Hand Gesture Recognition", frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
'''

#Moving cursor using hands
'''
import cv2
import mediapipe as mp
import pyautogui

# Initialize mediapipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
cap = cv2.VideoCapture(0)   # Open the default camera (usually the built-in webcam)
screen_width, screen_height = pyautogui.size()  # Set the screen width and height (adjust as needed)
cv2.namedWindow("Hand Tracking for Mouse Control")  # Create a window to display the webcam feed
while True:
    ret, frame = cap.read() # Capture frame-by-frame
    frame = cv2.flip(frame, 1)  # Flip the frame horizontally for a later selfie-view display
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert the BGR image to RGB
    results = hands.process(rgb_frame)  # Process the frame using mediapipe hands
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get the coordinates of the index finger
            index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            index_x, index_y = int(index_finger.x * screen_width), int(index_finger.y * screen_height)

            # Move the mouse cursor to the index finger position
            pyautogui.moveTo(index_x, index_y)

            # Draw a circle at the index finger position
            cv2.circle(frame, (index_x, index_y), 15, (0, 255, 0), -1)

    # Display the resulting frame
    cv2.imshow("Hand Tracking for Mouse Control", frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
'''
