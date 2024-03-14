import cv2
import numpy as np

# Create a black canvas
canvas = np.zeros((800, 800, 3), dtype=np.uint8)

# Triangle vertices
triangle_points = np.array([[400, 100], [100, 700], [700, 700]], np.int32)

# Function to calculate centroid of a triangle
def centroid(triangle):
    x = int((triangle[0][0] + triangle[1][0] + triangle[2][0]) / 3)
    y = int((triangle[0][1] + triangle[1][1] + triangle[2][1]) / 3)
    return (x, y)

# Draw triangle
cv2.polylines(canvas, [triangle_points], isClosed=True, color=(255, 255, 255), thickness=2)

# Get centroid
center = centroid(triangle_points)

# Display centroid
cv2.circle(canvas, center, 5, (255, 255, 255), -1)

# Display window
cv2.imshow('Canvas', canvas)

# Function to change color on mouse click
def change_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        r = np.random.randint(0, 256)
        g = np.random.randint(0, 256)
        b = np.random.randint(0, 256)
        cv2.polylines(canvas, [triangle_points], isClosed=True, color=(b, g, r), thickness=2)
        cv2.circle(canvas, center, 5, (255, 255, 255), -1)
        cv2.imshow('Canvas', canvas)

# Set mouse callback
cv2.setMouseCallback('Canvas', change_color)

# Wait for any key press to exit
cv2.waitKey(0)
cv2.destroyAllWindows()
