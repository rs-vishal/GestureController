import pyautogui

prev_index_x, prev_index_y = 0, 0  # For mouse smoothing
smooth_factor = 0.1  # Adjust for smoother movement
scroll_sensitivity = 5  # Adjust sensitivity for scrolling

def process_mouse_movement_and_scroll(frame_width, frame_height, landmarks):
    global prev_index_x, prev_index_y

    # Get screen dimensions
    screen_width, screen_height = pyautogui.size()

    # Calculate mouse position from index finger tip (point 8)
    index_x = landmarks[8].x * screen_width / frame_width
    index_y = landmarks[8].y * screen_height / frame_height

    # Smooth mouse movement
    smooth_index_x = prev_index_x + (index_x - prev_index_x) * smooth_factor
    smooth_index_y = prev_index_y + (index_y - prev_index_y) * smooth_factor
    pyautogui.moveTo(smooth_index_x, smooth_index_y)

    # Update previous index position for the next frame
    prev_index_x, prev_index_y = smooth_index_x, smooth_index_y

    # Two-finger scroll operation using points 8 (index) and 12 (middle)
    index_y_raw = landmarks[8].y
    middle_y_raw = landmarks[12].y

    # Calculate vertical distance between index and middle finger tips
    vertical_distance = middle_y_raw - index_y_raw

    # Perform scrolling based on vertical distance
    if abs(vertical_distance) > 0.02:  # Threshold to avoid accidental scrolling
        pyautogui.scroll(-vertical_distance * scroll_sensitivity)

