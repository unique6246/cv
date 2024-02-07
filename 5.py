import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image
image = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)

# Define a kernel (structuring element)
kernel = np.ones((10, 10), np.uint8)

# Perform erosion
erosion_result = cv2.erode(image, kernel, iterations=1)

# Perform dilation
dilation_result = cv2.dilate(image, kernel, iterations=1)

# Display the results
plt.subplot(131), plt.imshow(image, cmap='gray'), plt.title('Original')
plt.subplot(132), plt.imshow(erosion_result, cmap='gray'), plt.title('Erosion')
plt.subplot(133), plt.imshow(dilation_result, cmap='gray'), plt.title('Dilation')

plt.show()
