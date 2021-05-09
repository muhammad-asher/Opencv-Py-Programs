
# importing cv2
import cv2

# path
path = r'F:\SE-Courses\Projects\Python\Opencv-Py-Programs\Gui Features\sun.png'

# Reading an image in default mode
image = cv2.imread(path)

# Window name in which image is displayed
window_name = 'BorderCreation'

# Using cv2.copyMakeBorder() method
image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT)

# Displaying the image
cv2.imshow(window_name, image)
