#mouse_control.py
import pyautogui

prev_index_x, prev_index_y = 0, 0 
smooth_factor = 0.1
scroll_sensitivity = 5  
def process_mouse_movement_and_scroll(frame_width, frame_height, landmarks):
    global prev_index_x, prev_index_y

    screen_width, screen_height = pyautogui.size()

    index_x = landmarks[8].x * screen_width / frame_width
    index_y = landmarks[8].y * screen_height / frame_height

    
    smooth_index_x = prev_index_x + (index_x - prev_index_x) * smooth_factor
    smooth_index_y = prev_index_y + (index_y - prev_index_y) * smooth_factor
    pyautogui.moveTo(smooth_index_x, smooth_index_y)

    prev_index_x, prev_index_y = smooth_index_x, smooth_index_y

    index_y_raw = landmarks[8].y
    middle_y_raw = landmarks[12].y

    vertical_distance = middle_y_raw - index_y_raw

    if abs(vertical_distance) > 0.02:  
        pyautogui.scroll(-vertical_distance * scroll_sensitivity)

