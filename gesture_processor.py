import cv2
import mediapipe as mp
from gui import get_active_mode
from mouse_control import process_mouse_movement
from media_control import process_media_gestures
from ppt_control import process_ppt_gestures

hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

def process_gestures(frame, landmarks, mode):
    frame_height, frame_width, _ = frame.shape

    process_mouse_movement(frame_width, frame_height, landmarks)

    # Process gestures based on the active mode
    if mode == "PPT":
        process_ppt_gestures(landmarks, frame_width, frame_height)
    elif mode == "Media":
        process_media_gestures(landmarks, frame_width, frame_height)

def run_gesture_controller():
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks

        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(frame, hand)
                active_mode = get_active_mode()
                process_gestures(frame, hand.landmark, active_mode)

        cv2.imshow("Gesture Controller", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
