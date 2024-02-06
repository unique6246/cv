import cv2
import numpy as np

# Load the image
image = cv2.imread('indvk.jpg')  # Load as grayscale

# Define the kernel for erosion
kernel = np.ones((5,5), np.uint8)

# Perform erosion
eroded_image = cv2.erode(image, kernel, iterations=1)

# Display the original and eroded images
cv2.imshow('Original Image', image)
cv2.imshow('Eroded Image', eroded_image)
kernel = np.ones((5,5), np.uint8)

# Perform dilation
dilated_image = cv2.dilate(image, kernel, iterations=1)
cv2.imshow('Dilated Image', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()