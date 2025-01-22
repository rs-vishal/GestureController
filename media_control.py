import pyautogui

def process_media_gestures(landmarks, frame_width, frame_height):
    gesture_threshold = 50  # Adjust threshold as needed
    index_y = landmarks[8].y * frame_height
    thumb_y = landmarks[4].y * frame_height

    if thumb_y - index_y > gesture_threshold:
        pyautogui.press("volumeup")  
    elif index_y - thumb_y > gesture_threshold:
        pyautogui.press("volumedown") 
