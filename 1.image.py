import cv2
import numpy as np

# Define the dimensions of the black image (width and height)
width = 640  # You can change this to your desired width
height = 480  # You can change this to your desired height

# Create a black image
black_image = np.zeros((height, width, 3), dtype=np.uint8)

# Display the black image (optional)
cv2.imshow('Black Image', black_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
