import numpy as np
import cv2

# Create a white canvas
canvas = np.ones((400, 600, 3)) 

# Draw a red square
cv2.rectangle(canvas, (50, 50), (200, 250), (0, 0, 255), -1)

# Draw a blue circle
cv2.circle(canvas, (400, 200), 100, (255, 0, 0), -1)

# Display the image
cv2.imshow("2D Image with OpenCV", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
