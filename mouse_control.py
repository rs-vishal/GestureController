import pyautogui

prev_index_x, prev_index_y = 0, 0  # For mouse smoothing
smooth_factor = 0.1  # Adjust for smoother movement

def process_mouse_movement(frame_width, frame_height, landmarks):
    global prev_index_x, prev_index_y

    # Get screen dimensions
    screen_width, screen_height = pyautogui.size()

    # Get index finger tip coordinates and scale them to the screen size
    index_x = landmarks[8].x * screen_width / frame_width
    index_y = landmarks[8].y * screen_height / frame_height

    # Smooth movement of the mouse
    smooth_index_x = prev_index_x + (index_x - prev_index_x) * smooth_factor
    smooth_index_y = prev_index_y + (index_y - prev_index_y) * smooth_factor
    pyautogui.moveTo(smooth_index_x, smooth_index_y)

    # Update previous index position for the next frame
    prev_index_x, prev_index_y = smooth_index_x, smooth_index_y
