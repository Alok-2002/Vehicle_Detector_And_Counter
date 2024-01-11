import cv2
import numpy as np
from time import sleep
import matplotlib.pyplot as plt

min_width = 80
min_height = 80
offset = 6
line_position = 550
delay = 60
detections = []
cars = 0
vehicle_count_history = []

def get_center(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy

cap = cv2.VideoCapture('1video.mp4')
subtraction = cv2.bgsegm.createBackgroundSubtractorMOG()

plt.ion()

while True:
    ret, frame1 = cap.read()
    if not ret:
        break
    time = float(1/delay)
    sleep(time)
    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 5)
    img_sub = subtraction.apply(blur)
    dilate = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilated = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)
    dilated = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame1, (25, line_position), (1200, line_position), (255, 127, 0), 3)
    for (i, c) in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(c)
        valid_contour = (w >= min_width) and (h >= min_height)
        if not valid_contour:
            continue

        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        center = get_center(x, y, w, h)
        detections.append(center)
        cv2.circle(frame1, center, 4, (0, 0, 255), -1)

        for (x, y) in detections:
            if y < (line_position + offset) and y > (line_position - offset):
                cars += 1
                cv2.line(frame1, (25, line_position), (1200, line_position), (0, 127, 255), 3)
                detections.remove((x, y))
                vehicle_count_history.append(cars)

    cv2.putText(frame1, "VEHICLE COUNT: " + str(cars), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)

    plt.plot(vehicle_count_history, label='Vehicle Count')
    plt.xlabel('Frame')
    plt.ylabel('Count')
    plt.title('Vehicle Count Over Time')
    plt.legend()
    plt.draw()
    plt.pause(0.01)
    plt.clf()

    cv2.imshow("Original Video", frame1)

    key = cv2.waitKey(1)
    if key == 13 or key == 27:
        break

plt.ioff()
plt.plot(vehicle_count_history, label='Vehicle Count')
plt.xlabel('Frame')
plt.ylabel('Count')
plt.title('Vehicle Count Over Time')
plt.legend()
plt.show()
ryy
cv2.destroyAllWindows()
cap.release()
