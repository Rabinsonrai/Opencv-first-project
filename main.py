import cv2
import numpy as np
img = cv2.imread("Screenshot (348).png")
kernel = np.ones((5,5), np.uint8)
print(kernel)
width= 600
height= 300
img = cv2.resize(img,(width, height))
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgblur = cv2.GaussianBlur(imgray,(5,5), 1)
imgcanny = cv2.Canny(img, 100, 200)
imgcan = cv2.Canny(imgblur, 100, 200)
imgdilate = cv2.dilate(imgcan, kernel, iterations= 3)
imgerode = cv2.erode(imgdilate, kernel, iterations= 8)
cv2.imshow("not real", imgerode)
# cv2.imshow("picture", imgcanny)
cv2.waitKey(0)