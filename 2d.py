import cv2
import numpy as np
# Create a blank image

img =  np.zeros((800, 800, 3))

# Draw a square
cv2.rectangle(img, (100, 100), (600, 300), (0, 255, 0), -1)

# Draw a circle
cv2.circle(img, (400, 400), 80, (0, 0, 255), -1)


# Display the image
cv2.imshow("2D Image with Objects", img)
cv2.waitKey(0)