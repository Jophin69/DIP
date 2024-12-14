import cv2

# Load the image
image = cv2.imread('joeee.jpg') # Replace with your image file path

# Get image dimensions
height, width, _ = image.shape

# Calculate the center point
center_y, center_x = height // 2, width // 2

# Split the image into quadrants
top_left = image[:center_y, :center_x]
top_right = image[:center_y, center_x:]
bottom_left = image[center_y:, :center_x]
bottom_right = image[center_y:, center_x:]

# Display the quadrants
cv2.imshow('Top Left', top_left)
cv2.imshow('Top Right', top_right)
cv2.imshow('Bottom Left', bottom_left)
cv2.imshow('Bottom Right', bottom_right)

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()