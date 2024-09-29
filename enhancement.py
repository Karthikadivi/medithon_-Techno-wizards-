import cv2

# Load the PSP image
image = cv2.imread('psp_image.jpg', 0)  # Ensure this image is in your project folder

# Enhance the constrast
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
enhanced_image = clahe.apply(image)

# Save the enhanced image
cv2.imwrite('enhanced_psp_image.jpg', enhanced_image)

# Show the enhanced image
cv2.imshow('Enhanced Image', enhanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
