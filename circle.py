import numpy as np
import cv2

# Create a blank image with a black background
image = np.zeros((400, 400, 3), dtype=np.uint8)

# Set the center coordinates and radius of the circle
center = (0, 0)
radius = 100

# Set the color of the circle (white in this case)
color = (255, 255, 255)

# Draw the circle on the image
cv2.circle(image, center, radius, color, thickness=-1)

# Display the image
cv2.imshow("White Circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
