import cv2
import numpy as np
#--------------------lọc ra vùng có làn đường-----------------------# 
def region_of_interest(image):
    height = image.shape[0]
    pollygons = np.array([[(100, height), (650, height), (370, 300),(480, 293)]]) # lọc theo hình thang
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, pollygons, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image