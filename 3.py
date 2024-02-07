import cv2
import numpy as np

# Read an image from file
image = cv2.imread('1.JPG')

# Specify the new dimensions (width, height)
new_width = 300
new_height = 200

# Resize the image using cv2.resize
resized_image = cv2.resize(image, (new_width, new_height))

# Display the original and resized images
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
