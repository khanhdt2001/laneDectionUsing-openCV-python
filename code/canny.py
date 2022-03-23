import cv2

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # chuyển về kênh màu sám
    blur = cv2.GaussianBlur(gray, (5,5), 0) # làm mịn theo ô 5-5 
    canny = cv2.Canny(blur, 0, 150) # canny làm tách biệt 2 khoảng màu nhạt và đậm 
    return canny