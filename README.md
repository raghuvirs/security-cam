***Security Camera Application***
<br/>
<br/>
This Python application uses PyQt5 and OpenCV to create a simple security camera system that monitors your webcam's feed. It detects motion in the camera's field of view and saves images when significant motion is detected.
<br/>
<br/>

![Screenshot 2023-12-01 113159](https://github.com/biswadeep-roy/security-cam/assets/74821633/e24aa55d-16e4-47c7-9056-9543f944a9ca)

***Features***
Motion Detection: The application continuously captures frames from the webcam and detects motion using image differencing and contour analysis.

Image Capture: When motion is detected, the application captures the frame and saves it with a timestamp in the specified directory.

Audio Alert: An audio alert is triggered when motion is detected.

Adjustable Sensitivity: You can adjust the sensitivity level to control the minimum motion size required to trigger an alert.

Audio Volume Control: You can adjust the volume of the audio alert.
<br/>
<br/>
**Usage**
Launch the application by running python security_camera.py.

Click the "Start Monitoring" button to begin monitoring your webcam feed.

Adjust the sensitivity level using the slider. A higher sensitivity value will detect smaller motions.

To adjust the audio volume, click the "Set Audio Volume" button and use the slider.

Click the "Exit" button to close the application.

When motion is detected, an alert sound is played, and the captured image is saved in the specified directory.
<br/>
<br/>
**Configuration**
You can choose the directory where captured images are saved by clicking the "Choose Save Location" button and selecting a folder.
<br/>
<br/>
**Requirements**
Python 3.x
PyQt5
OpenCV
numpy
winsound

<br/>
<br/>
**Installation**

Clone this repository:

`git clone https://github.com/biswadeep-roy/security-cam.git`

Install the required dependencies:


`pip install PyQt5 opencv-python numpy`

Run the application:

`python security_camera.py`


License
This project is licensed under the MIT License. See the _LICENSE_ file for details.
# security-cam
