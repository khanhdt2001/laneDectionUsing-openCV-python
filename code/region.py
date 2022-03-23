import cv2
import numpy as np
#--------------------lọc ra vùng có làn đường-----------------------# 
def region_of_interest(image):
    height = image.shape[0]
    pollygons = np.array([[(200, height), (1100, height), (550, 250)]]) # lọc theo hình tam giác
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, pollygons, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image