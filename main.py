import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

#set screen resolution
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dimension = (width,height)

file_name = f"video/Video_{str(time.strftime('%d-%m-%Y %H-%M-%S'))}.mp4"
format = cv2.VideoWriter_fourcc(*"XVID")   #define format here VideoWriter_fourcc method inside cv2 used to define video format which is XVID

output = cv2.VideoWriter(file_name,format,30.0,dimension)

now_start_time = time.time()
duration = 23
end_time = now_start_time + duration

while True:
    image = pyautogui.screenshot()
    frame_1 = np.array(image)
    frame = cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)

    output.write(frame)
    c_time = time.time()

    if c_time > end_time:
        break

output.release()

print("--- END ---")
