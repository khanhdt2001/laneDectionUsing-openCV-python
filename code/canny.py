import cv2
import numpy as np
def canny(image):
    # hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # low_yellow = np.array([18, 94, 140])
    # up_yellow = np.array([48, 255, 255])
    # maskY = cv2.inRange(hsv, low_yellow, up_yellow)
    # cv2.imshow("yellow", maskY)
    
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # chuyển về kênh màu sám
    blur = cv2.GaussianBlur(gray, (5,5), 0) # làm mịn theo ô 5-5 
    # cv2.imshow("blur",blur)
    canny = cv2.Canny(blur, 0, 150) # canny làm tách biệt 2 khoảng màu nhạt và đậm 
    return canny