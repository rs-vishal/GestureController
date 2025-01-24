import pyautogui
import time

prev_hand_x = None  # To track hand movement direction
last_switch_time = 0  # For debouncing slide switches


def process_ppt_gestures(landmarks, frame_width, frame_height):
    """
    Detects gestures to navigate PowerPoint slides using hand movements.
    """
    global prev_hand_x, last_switch_time

    # Thresholds
    swing_threshold = 100  # Distance for hand swing
    debounce_time = 0.5  # Time in seconds to prevent rapid switching

    # Hand position
    index_x = landmarks[8].x * frame_width

    # Detect hand swing left/right
    if prev_hand_x is not None:
        swing_distance = index_x - prev_hand_x

        # Ensure a delay between consecutive gestures
        if time.time() - last_switch_time > debounce_time:
            if swing_distance > swing_threshold:
                pyautogui.press("right")  # Next slide
                last_switch_time = time.time()
            elif swing_distance < -swing_threshold:
                pyautogui.press("left")  # Previous slide
                last_switch_time = time.time()

    # Update previous hand position
    prev_hand_x = index_x
