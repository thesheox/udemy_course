import cv2
import mediapipe as mp

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize MediaPipe Drawing module for drawing landmarks
mp_drawing = mp.solutions.drawing_utils

# Open a video capture object (0 for the default camera)
cap = cv2.VideoCapture(0)


def count_fingers(hand_landmarks):
    # List of fingers to check (excluding the thumb)
    finger_tips = [8, 12, 16, 20]

    # List of corresponding finger PIP joints (one joint before the tip)
    finger_pips = [6, 10, 14, 18]

    count = 0

    # Check if fingers are up
    for tip, pip in zip(finger_tips, finger_pips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
            count += 1

    # Check if thumb is up
    if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x:
        count += 1

    return count


while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        continue

    # Convert the frame to RGB format
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect hands
    results = hands.process(frame_rgb)

    # Check if hands are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmarks on the frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Count and print the number of fingers up
            fingers_up = count_fingers(hand_landmarks)
            print(f"Fingers up: {fingers_up}")

    # Display the frame with hand landmarks
    cv2.imshow('Hand Recognition', frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
