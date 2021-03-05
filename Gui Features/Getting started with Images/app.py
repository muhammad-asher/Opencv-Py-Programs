import cv2
import numpy as np
#Load Image
img = cv2.imread("./Images-Videos/sun.png")
# with 0 => gray scale image
#Display Image
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()