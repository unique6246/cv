import cv2
import matplotlib.pyplot as plt

# Read the image
image_path = '5.jpg'
original_image = cv2.imread(image_path)

# Convert from BGR to RGB (OpenCV uses BGR by default)
rgb_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

# Display the original and converted images using matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 2)
plt.imshow(original_image)
plt.title('Converted Image (BGR)')
plt.axis('off')

plt.subplot(1, 2, 1)
plt.imshow(rgb_image)
plt.title('Original Image (RGB)')
plt.axis('off')

plt.show()
