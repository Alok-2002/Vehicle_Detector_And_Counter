# Vehicle Counting System

This repository contains a Python script that uses computer vision techniques to count the number of vehicles passing through a specified line in a video. The script utilizes the OpenCV library for image processing and matplotlib for plotting the vehicle count over time.

## Features
- Counts vehicles in a video stream based on their movement across a predefined line.
- Utilizes background subtraction for motion detection.
- Provides real-time visualization of the vehicle count using matplotlib.

## Dependencies
Make sure you have the following dependencies installed:
- OpenCV
- NumPy
- Matplotlib

Install the dependencies using the following command:
```bash
pip install opencv-python numpy matplotlib
```

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/Alok-2002/Vehicle_Detector_And_Counter.git
   cd Vehicle_Detector_And_Counter
   ```

2. Replace '1video.mp4' with the path to your video file in the script.

3. Run the script:
   ```bash
   python main.py
   ```

4. Press 'Enter' or 'Esc' to exit the video stream.

## Snapshot

![image](https://github.com/Alok-2002/Vehicle_Detector_And_Counter/assets/93814546/8df06bc0-11de-40ee-9400-91a042c0ed9a)


## Configuration
You can modify the following parameters in the script according to your requirements:

- `min_width`: Minimum width of a valid contour.
- `min_height`: Minimum height of a valid contour.
- `offset`: Offset for the line position to detect vehicles.
- `line_position`: Y-coordinate of the line where vehicle counting occurs.
- `delay`: Delay in milliseconds between frames.
- `cap = cv2.VideoCapture('1video.mp4')`: Replace '1video.mp4' with the path to your video file.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to contribute or report issues. Happy vehicle counting!
