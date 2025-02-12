# GestureController

GestureController is a gesture-based control system that leverages computer vision techniques to recognize hand gestures in real time and translate them into system commands. Using a webcam to capture live video input, the project processes the feed to detect predefined hand gestures and maps them to specific actions on your computer.

## Overview

This project enables users to interact with their computer using intuitive hand movements. By integrating advanced hand tracking and gesture recognition with automation libraries, GestureController provides a seamless way to control applications or perform system operations using gestures. The system is built with Python and incorporates a robust tech stack for efficient real-time processing.

## Features

- **Real-Time Gesture Detection**: Utilizes a webcam to capture live video and detect hand gestures on the fly.
- **Accurate Gesture Recognition**: Employs MediaPipe for reliable hand tracking and gesture recognition.
- **System Automation**: Uses PyAutoGUI to translate recognized gestures into system commands (e.g., mouse and keyboard actions).
- **Customizable Gesture Mappings**: Easily modify or add gesture-to-command mappings based on your needs.
- **User-Friendly Interface**: Displays visual feedback to indicate detected gestures and corresponding actions.

## Tech Stack

- **Python**: The primary programming language used for development.
- **PyAutoGUI**: Automates mouse and keyboard control to execute system commands.
- **MediaPipe**: Provides advanced hand tracking and gesture recognition capabilities.
- **OpenCV**: Handles image processing tasks and video capture from the webcam.

## Prerequisites

Before running the project, ensure that you have the following installed:

- Python 3.x
- A working webcam (integrated or external)
- Basic familiarity with running Python scripts via the command line

## Installation

Follow these steps to set up and run GestureController locally:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/rs-vishal/GestureController.git
   cd GestureController
2. ** Create a Virtula Enironment**
   ```bash
   python -m venv venv
   source venv/bin/activate 
3. **Install the required Packages**
   ```bash
     pip install -r requirements.txt

## Usage
1. **Start the Application**
   ```bash
     python main.py
2.**Interact with the System**
  The application will launch and access your webcam, displaying a live video feed.
   Perform the predefined hand gestures in front of the camera.
   The system will recognize the gesture and execute the corresponding command.
3.**Customization**
  To modify the gesture-to-command mappings, edit the configuration sections in the source code as needed.

## Acknowledgements
 MediaPipe: For providing robust real-time hand tracking solutions.
 OpenCV: For powerful image processing and computer vision capabilities.
 PyAutoGUI: For enabling seamless automation of system commands.
  

   
