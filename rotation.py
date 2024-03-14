import cv2
import numpy as np
import math

# Create a window
cv2.namedWindow("Rotating 3D Prism", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Rotating 3D Prism", 800, 600)

# Set prism parameters
prism_size = 100
prism_color = (255, 0, 0)  # Blue color
prism_thickness = 2

# Define prism vertices in 3D space (rectangular prism)
vertices = np.array([[-1, -1, -1],
                     [1, -1, -1],
                     [1, 1, -1],
                     [-1, 1, -1],
                     [-1, -1, 1],
                     [1, -1, 1],
                     [1, 1, 1],
                     [-1, 1, 1]], dtype=np.float32)

# Define prism edges
edges = [(0, 1), (1, 2), (2, 3), (3, 0),
         (4, 5), (5, 6), (6, 7), (7, 4),
         (0, 4), (1, 5), (2, 6), (3, 7)]

# Create a rotation matrix
angle = 0
while True:
    rotation_matrix = np.array([[math.cos(angle), -math.sin(angle), 0],
                                [math.sin(angle), math.cos(angle), 0],
                                [0, 1, 1]], dtype=np.float32)

    # Rotate the prism vertices in 3D space
    rotated_vertices = np.dot(vertices, rotation_matrix)

    # Project the 3D points to 2D
    projected_vertices = (rotated_vertices[:, :2] * prism_size + np.array([400, 300])).astype(int)

    # Create a black image
    frame = np.zeros((600, 800, 3), dtype=np.uint8)

    # Draw prism edges
    for edge in edges:
        pt1 = tuple(projected_vertices[edge[0]])
        pt2 = tuple(projected_vertices[edge[1]])
        cv2.line(frame, pt1, pt2, prism_color, prism_thickness)

    # Display the frame
    cv2.imshow("Rotating 3D Prism", frame)

    # Wait for a moment and update the angle
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

    angle += 0.02

# Release the window
cv2.destroyAllWindows()
