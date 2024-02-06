import cv2
import numpy as np

# Initialize global variables
triangle_color = (0, 255, 0)  # Initial color: Green

def draw_triangle(image):
    # Define vertices of the triangle
    triangle_points = np.array([[100, 300], [300, 300], [200, 100]], np.int32)
    
    # Draw the triangle
    cv2.polylines(image, [triangle_points], isClosed=True, color=triangle_color, thickness=2)
    
    # Calculate centroid of the triangle
    centroid = np.mean(triangle_points, axis=0, dtype=np.int32)
    
    # Draw the centroid as a small circle
    cv2.circle(image, tuple(centroid), radius=3, color=triangle_color, thickness=-1)

def change_color(event, x, y, flags, param):
    global triangle_color
    
    # Check if the event is a left mouse button click
    if event == cv2.EVENT_LBUTTONDOWN:
        # Change the color of the triangle randomly
        triangle_color = np.random.randint(0, 256, size=3).tolist()
        print("Color changed to:", triangle_color)

def main():
    # Create a black canvas
    canvas = np.zeros((400, 400, 3), dtype=np.uint8)

    while True:
        # Draw the triangle on the canvas
        draw_triangle(canvas)

        # Display the image
        cv2.imshow("Triangle with Centroid", canvas)

        # Check for keyboard input
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Set up the mouse callback function
    cv2.namedWindow("Triangle with Centroid")
    cv2.setMouseCallback("Triangle with Centroid", change_color)
    
    # Run the main function
    main()
