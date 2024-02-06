import numpy as np
import cv2

# Create a black canvas
canvas = np.zeros((400, 600, 3), dtype="uint8")

# Draw a pseudo-3D cube
cube_points = np.array([[50, 50], [150, 50], [150, 150], [50, 150],
                        [100, 0], [200, 0], [200, 100], [100, 100]], dtype=np.int32)
cv2.polylines(canvas, [cube_points[:4]], True, (0, 0,255), 2)  # Draw the front face
cv2.polylines(canvas, [cube_points[4:]], True, (0, 0,255), 2)  # Draw the top face
for i in range(4):
    cv2.line(canvas, tuple(cube_points[i]), tuple(cube_points[i + 4]), (0, 0, 255), 2)  # Draw connecting lines

cv2.imshow("3D Image with OpenCV", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
