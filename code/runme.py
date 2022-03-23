import cv2
import numpy as np
import matplotlib.pyplot as plt
from canny import *
from region import *
from displayLine import *
from makeCoordinates import *
from averageSloveIntercept import *

cap = cv2.VideoCapture("./assets/curveVideo.mp4")

while(cap.isOpened()):
    _, frame = cap.read()
    canny_image = canny(frame)
    cropped_image = region_of_interest(canny_image)
    lines = cv2.HoughLinesP(cropped_image, 1, np.pi/180, 50, np.array([]), minLineLength=40, maxLineGap=50)
    averaged_lines = average_slope_intercept(frame, lines)
    # line_image = display_line(frame, averaged_lines)
    line_image = display_line(frame, lines)

    combine_image= cv2.addWeighted(frame, 0.8, line_image, 1, 1)
    cv2.imshow("result",combine_image)
    cv2.imshow("canny", line_image)
    if cv2.waitKey(25) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()