import numpy as np
def make_coordinates(image, line_parameters):
    # if line_parameters is not None:
        slope, intercept = line_parameters
        y1 = image.shape[0]
        y2 = int(y1*(3/5)) # giới hạn độ dài đoạn 
        x1 = int((y1 - intercept)/ slope)
        x2 = int((y2 - intercept)/ slope)
        return np.array([x1, y1, x2, y2])