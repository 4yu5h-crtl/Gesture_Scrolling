# Gesture Control for Scrolling

This project demonstrates a gesture-controlled scrolling system using a webcam, OpenCV, MediaPipe, and Python. By detecting hand gestures, it simulates keyboard inputs to scroll through content such as PDFs in a browser like Microsoft Edge.

## Features
- **Gesture Recognition**: Detects up and down finger gestures using a webcam.
- **Scrolling Simulation**: Simulates `Arrow Up` and `Arrow Down` key presses to scroll content.
- **Real-Time Processing**: Provides smooth gesture recognition with visual feedback on a live video feed.

## Requirements
Ensure you have the following dependencies installed:
- `opencv-python`
- `mediapipe`
- `numpy`
- `pyautogui`

## Installation

### Using `requirements.txt`
1. Clone the repository or copy the project files.
2. Navigate to the project directory.
3. Install the dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

### Using Batch File
1. Double-click the `install_requirements.bat` file to automatically set up the environment and install dependencies.

## How to Run
1. Open your terminal or command prompt.
2. Navigate to the project directory.
3. Run the Python script:
   ```bash
   python gesture_scrolling.py
   ```
4. Ensure your webcam is connected and active.
5. Open a PDF in Microsoft Edge or any other application where scrolling is needed.

## Usage
1. **Up Gesture**: Raise your index finger to scroll up.
2. **Down Gesture**: Raise both the index and middle fingers to scroll down.
3. **Stopping Scrolling**: Press the `q` key in the OpenCV window to quit the program.

## Files
- **`gesture_control.py`**: Main script containing the implementation.
- **`requirements.txt`**: Dependency list for the project.
- **`install_requirements.bat`**: Batch file to automate environment setup and dependency installation.

## Customization
- Adjust the gesture detection sensitivity by modifying the `threshold` value in the `recognize_gesture` function.
- Extend the functionality by adding gestures for actions like zooming or pausing.

## Dependencies
To manually install the required libraries, run:
```bash
pip install opencv-python mediapipe numpy pyautogui
```

## Troubleshooting
- **Python Not Found**: Ensure Python is installed and added to your system's PATH.
- **Camera Issues**: Check if your webcam is properly connected and not being used by another application.
- **Gesture Recognition Problems**: Ensure your hand is visible in the camera frame and gestures are clear.

## License
This project is open-source and free to use under the MIT License.

## Contributing
Feel free to fork this repository and submit pull requests for any enhancements or bug fixes.

---
Enjoy controlling your applications with gestures! 🚀

