import pyautogui

play_pause_triggered = False  # Cooldown state for play/pause gesture


def detect_gesture(hand_landmarks):
    """
    Detects specific gestures for media control based on hand landmarks.
    """
    global play_pause_triggered
    fingers = []

    # Thumb
    fingers.append(1 if hand_landmarks[4].x < hand_landmarks[3].x else 0)

    # Index Finger
    fingers.append(1 if hand_landmarks[8].y < hand_landmarks[6].y else 0)

    # Middle Finger
    fingers.append(1 if hand_landmarks[12].y < hand_landmarks[10].y else 0)

    # Ring Finger
    fingers.append(1 if hand_landmarks[16].y < hand_landmarks[14].y else 0)

    # Pinky Finger
    fingers.append(1 if hand_landmarks[20].y < hand_landmarks[18].y else 0)

    # Play/Pause Gesture (Index Finger Up, Others Down)
    if fingers == [0, 1, 0, 0, 0] and not play_pause_triggered:
        pyautogui.press("playpause")
        play_pause_triggered = True
    elif fingers != [0, 1, 0, 0, 0]:
        play_pause_triggered = False

    # Volume Up Gesture (All Fingers Up)
    if fingers == [1, 1, 1, 1, 1]:
        pyautogui.press("volumeup")

    # Volume Down Gesture (Thumb and Pinky Up)
    if fingers == [1, 0, 0, 0, 1]:
        pyautogui.press("volumedown")


def process_media_gestures(landmarks, frame_width, frame_height):
    """
    Controls volume based on the relative vertical position of the thumb and index finger.
    """
    index_y = landmarks[8].y * frame_height
    thumb_y = landmarks[4].y * frame_height
    threshold = 50  # Adjust for sensitivity

    if thumb_y - index_y > threshold:
        pyautogui.press("volumeup")
    elif index_y - thumb_y > threshold:
        pyautogui.press("volumedown")
