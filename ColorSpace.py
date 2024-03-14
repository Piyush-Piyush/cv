import cv2

# Load an image
image = cv2.imread('6_ColorSpace\input_image.jpg')

# Convert from BGR to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert from BGR to RGB
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert from BGR to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Display the original and converted images
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('RGB Image', rgb_image)
cv2.imshow('HSV Image', hsv_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
