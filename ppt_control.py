import pyautogui

def process_ppt_gestures(landmarks, frame_width, frame_height):
    gesture_threshold = 50  # Adjust threshold as needed
    index_x = landmarks[8].x * frame_width
    thumb_x = landmarks[4].x * frame_width

    if thumb_x - index_x > gesture_threshold:
        pyautogui.press("right")  # Next slide
    elif index_x - thumb_x > gesture_threshold:
        pyautogui.press("left")  # Previous slide
