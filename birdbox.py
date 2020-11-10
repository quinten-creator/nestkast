from picamera import PiCamera
from gpiozero import MotionSensor
from time import sleep

import time
import os

camera = PiCamera()
pir = MotionSensor(4)
teller = 0
recording = 0
camera.exposure_mode = 'nightpreview'

#usb mount
os.system("sudo mount /dev/sda1 /mnt/USBdrive/")
print("USB mounted")
sleep(3)
while True:
        if pir.motion_detected and recording == 0:
                recording = 1
                now = time.strftime("%d_%m_%y_%H_%M_%S")
                camera.start_recording('/mnt/USBdrive/movie' + now + '.h264')
                print('recording')
        if pir.motion_detected == False and recording == 1:
                camera.stop_recording()
                print("stop record")
                recording = 0
        sleep(1)
        teller = teller + 1
        if teller >= 300 and recording == 1 :
                camera.stop_recording()
                now = time.strftime("%d_%m_%y_%H_%M_%S")
                camera.start_recording('/mnt/USBdrive/movie' + now +'.h264')
                print('switch record')
                teller = 0




