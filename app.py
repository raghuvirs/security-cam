from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import cv2
import winsound
import numpy as np
import datetime

ui, _ = loadUiType('security_cam.ui')

class SecurityCameraApp(QMainWindow, ui):
    audio_volume = 500

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.start_button.clicked.connect(self.start_monitoring)
        self.volume_button.clicked.connect(self.set_audio_volume)
        self.exit_button.clicked.connect(self.close_window)
        self.volume_slider.setVisible(False)
        self.volume_slider.valueChanged.connect(self.set_audio_volume_level)
        self.sensitivity_slider.setVisible(True)
        self.sensitivity_slider.setMinimum(1)
        self.sensitivity_slider.setMaximum(10)
        self.sensitivity_slider.setSingleStep(1)
        self.sensitivity_slider.setPageStep(1)
        self.sensitivity_slider.setValue(5)
        self.sensitivity_slider.valueChanged.connect(self.set_sensitivity)
        self.sensitivity_level_label.setText("5")
        self.save_path = None
        self.sensitivity = 5

    def start_monitoring(self):
        print("Start monitoring button clicked")
        webcam = cv2.VideoCapture(0)
        while True:
            _, frame1 = webcam.read()
            _, frame2 = webcam.read()
            diff = cv2.absdiff(frame1, frame2)
            gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
            dilated = cv2.dilate(thresh, None, iterations=3)
            contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            for c in contours:
                if cv2.contourArea(c) < 5000 * self.sensitivity:
                    continue
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Save the captured image with a timestamp
                if self.save_path:
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
                    image_path = f"{self.save_path}/captured_{timestamp}.jpg"
                    cv2.imwrite(image_path, frame1)

                height, width, channel = frame1.shape
                bytes_per_line = 3 * width
                q_image = QImage(frame1.data, width, height, bytes_per_line, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(q_image)
                self.camera_view.setPixmap(pixmap)
                winsound.Beep(self.audio_volume, 100)
            cv2.imshow("Security-Camera", frame1)

            key = cv2.waitKey(10)
            if key == 27:
                break
        webcam.release()
        cv2.destroyAllWindows()

    def set_audio_volume(self):
        self.volume_slider.setVisible(True)
        print("Set audio volume button clicked")

    def close_window(self):
        self.close()

    def set_audio_volume_level(self):
        self.volume_level_label.setText(str(self.volume_slider.value() // 10))
        self.audio_volume = self.volume_slider.value() * 10
        cv2.waitKey(1000)
        self.volume_slider.setVisible(False)

    def set_sensitivity(self):
        self.sensitivity = self.sensitivity_slider.value()
        self.sensitivity_level_label.setText(str(self.sensitivity))

    def choose_save_location(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly | QFileDialog.ReadOnly
        folder_path = QFileDialog.getExistingDirectory(self, "Select Save Location", "", options=options)
        if folder_path:
            self.save_path = folder_path

def main():
    app = QApplication(sys.argv)
    window = SecurityCameraApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
