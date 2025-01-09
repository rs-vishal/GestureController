from threading import Thread
from gui import start_gui
from gesture_processor import run_gesture_controller

if __name__ == "__main__":
    Thread(target=start_gui).start()
    run_gesture_controller()
