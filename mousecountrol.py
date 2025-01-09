import cv2
import mediapipe as mp
import pyautogui
import math


# Initialize webcam and MediaPipe Hands model
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

# Get the screen width and height for mapping hand coordinates to screen coordinates
screen_width, screen_height = pyautogui.size()

# Initialize variables for mouse control
index_x, index_y = 0, 0
prev_index_x, prev_index_y = 0, 0  # Previous mouse position for smoothing

# Smoothing factor
smooth_factor = 0.1  # Higher value = smoother, lower value = more responsive

# Proximity threshold for left-click and right-click (in pixels)
click_threshold = 60  # Distance between thumb and index for left-click
right_click_threshold = 50  # Distance between landmarks for right-click


while True:
    # Capture the frame from the webcam
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Flip the frame horizontally (for mirror effect)
    
    # Get the dimensions of the frame
    frame_height, frame_width, _ = frame.shape
    
    # Convert the frame to RGB (as required by Mediapipe)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame to detect hands
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    
    if hands:
        for hand in hands:
            # Draw hand landmarks on the frame
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            
            # Reset positions for each hand
            index_x, index_y = 0, 0
            thumb_x, thumb_y = 0, 0
            
            # Landmark positions for right-click detection
            points = {}
            
            # Iterate through all landmarks (21 points)
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)  # X coordinate of the landmark
                y = int(landmark.y * frame_height)  # Y coordinate of the landmark
                
                # If the landmark is the tip of the index finger (id 8)
                if id == 8:
                    cv2.circle(frame, (x, y), 10, (0, 255, 255), -1)  # Draw a circle at index tip
                    # Scale the index finger position to the screen resolution
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y
                
                # If the landmark is the tip of the thumb (id 4)
                if id == 4:
                    cv2.circle(frame, (x, y), 10, (255, 0, 0), -1)  # Draw a circle at thumb tip
                    # Scale the thumb finger position to the screen resolution
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y
                
                # Store landmarks for right-click detection
                if id in [4, 8, 12, 16, 20]:
                    points[id] = (x, y)
            
            # Calculate the distance between the thumb and the index finger
            distance = math.sqrt((index_x - thumb_x)**2 + (index_y - thumb_y)**2)
            
            # Left-click logic
            if distance < click_threshold:
                pyautogui.click()
                pyautogui.sleep(1)  # Optional: add delay to prevent continuous clicks
            
            # Right-click logic (if all landmarks meet closely)
            if len(points) == 5:
                distances = [
                    math.sqrt((points[4][0] - points[8][0])**2 + (points[4][1] - points[8][1])**2),
                    math.sqrt((points[8][0] - points[12][0])**2 + (points[8][1] - points[12][1])**2),
                    math.sqrt((points[12][0] - points[16][0])**2 + (points[12][1] - points[16][1])**2),
                    math.sqrt((points[16][0] - points[20][0])**2 + (points[16][1] - points[20][1])**2),
                ]
                if all(d < right_click_threshold for d in distances):
                    pyautogui.rightClick()
                    pyautogui.sleep(1)
            
            # Smooth the movement of the mouse cursor
            smooth_index_x = prev_index_x + (index_x - prev_index_x) * smooth_factor
            smooth_index_y = prev_index_y + (index_y - prev_index_y) * smooth_factor
            
            # Move the mouse to the smoothed position
            pyautogui.moveTo(smooth_index_x, smooth_index_y)
            
            # Store the current position as the previous position for the next frame
            prev_index_x, prev_index_y = smooth_index_x, smooth_index_y
    
    # Display the processed frame
    cv2.imshow('Virtual Mouse', frame)
    
    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
