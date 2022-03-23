import cv2
import numpy as np
import matplotlib.pyplot as plt
from canny import *
from region import *
from makeLine import *
from makePath import *
from findPath import *

cap = cv2.VideoCapture("./assets/curveVideo.mp4")

while(cap.isOpened()):
    _, frame = cap.read()
    canny_image = canny(frame)
    cropped_image = region_of_interest(canny_image)
    lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=20, maxLineGap=255)
    averaged_lines = average_slope_intercept(frame, lines)
    line_image = display_line(frame, averaged_lines)
    combine_image= cv2.addWeighted(frame, 0.8, line_image, 1, 1)
    cv2.imshow("result",combine_image)
    cv2.imshow("canny", canny_image)
    if cv2.waitKey(25) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()