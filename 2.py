import numpy as np
import cv2

# Create a black canvas
canvas = np.zeros((400, 600, 3), dtype=np.uint8)

# Define cube vertices
vertices = [(50, 50), (150, 50), (150, 150), (50, 150),
            (100, 0), (200, 0), (200, 100), (100, 100)]

# Draw the front face of the cube
cv2.rectangle(canvas, vertices[0], vertices[2], (255,0,0), 2)

# Draw the back face of the cube
cv2.rectangle(canvas, vertices[4], vertices[6], (255, 0, 0), 2)

# Draw the connecting lines
for i in range(4):
    cv2.line(canvas, vertices[i], vertices[i + 4], ( 255,0, 0), 2)

# Display the image
cv2.imshow("3D Image with OpenCV", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()