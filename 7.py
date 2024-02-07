import cv2
import numpy as np

# Global variables
triangle_vertices = np.array([[100, 100], [300, 100], [200, 300]], np.int32)
centroid = np.mean(triangle_vertices, axis=0, dtype=np.int32)
color = (0, 255, 0)  # Initial color (green)

def draw_triangle(image):
    cv2.polylines(image, [triangle_vertices], isClosed=True, color=color, thickness=2)
    cv2.circle(image, tuple(centroid), 3, color, -1)

def change_color(event, x, y, flags, param):
    global color
    if event == cv2.EVENT_LBUTTONDOWN:
        color = np.random.randint(0, 256, (3,), dtype=np.uint8).tolist()
        draw_triangle(image)
        cv2.imshow("Triangle with Centroid", image)

def handle_keyboard_input(key):
    global color
    if key == ord('c') or key == 32:  # Press 'c' to change color using keyboard
        color = np.random.randint(0, 256, (3,), dtype=np.uint8).tolist()
        draw_triangle(image)
        cv2.imshow("Triangle with Centroid", image)

# Create a black image
image = np.zeros((400, 400, 3), dtype=np.uint8)

# Draw the initial triangle and centroid
draw_triangle(image)

# Display the image
cv2.imshow("Triangle with Centroid", image)
cv2.setMouseCallback("Triangle with Centroid", change_color)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Press 'Esc' to exit
        break
    handle_keyboard_input(key)

cv2.destroyAllWindows()
