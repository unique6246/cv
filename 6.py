import cv2

# Read the input image
input_image = cv2.imread("indvk.jpg")

# Check if the image is loaded successfully
if input_image is None:
    print("Error: Could not load the image.")
else:
    # Convert the image from BGR (default color space in OpenCV) to grayscale
    gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # Convert the image from BGR to RGB
    rgb_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

    # Display the original and converted images
    cv2.imshow("Original Image", input_image)
    cv2.imshow("Grayscale Image", gray_image)
    cv2.imshow("RGB Image", rgb_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
