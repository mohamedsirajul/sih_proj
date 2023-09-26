import cv2
import numpy as np

# Load the image
image = cv2.imread('captured_image.jpg')

# Convert the image to the HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define a lower and upper threshold for the green color (typical color of trees)
lower_green = np.array([35, 50, 50])
upper_green = np.array([85, 255, 255])

# Create a mask to isolate the green regions
mask = cv2.inRange(hsv, lower_green, upper_green)

# Find contours in the mask
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize a counter for the number of trees
tree_count = 0

# Iterate through the contours and count the trees
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 100:  # Adjust the area threshold as needed
        tree_count += 1
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)  # Draw the contour on the image

# Display the result
cv2.imshow('Result', image)
print(f'Number of trees: {tree_count}')

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
