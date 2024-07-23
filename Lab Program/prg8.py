import cv2 
import numpy as np 
import matplotlib.pyplot as plt

def translate_image(image, dx, dy): 
    rows, cols = image.shape[:2] 
    translation_matrix = np.float32([[1, 0, dx], [0, 1, dy]]) 
    translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows)) 
    return translated_image 

# Read the image 
image = cv2.imread("rnsit.jpg") 

# Convert the image from BGR to RGB for correct color display in matplotlib 
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 

# Get image dimensions 
height, width = image.shape[:2] 

# Calculate the center coordinates of the image 
center = (width // 2, height // 2) 

# Get rotation and scaling values from the user 
rotation_value = int(input("Enter the degree of Rotation (between -180 and 180): ")) 
while rotation_value < -180 or rotation_value > 180: 
    rotation_value = int(input("Invalid input. Enter the degree of Rotation (between -180 and 180): ")) 
scaling_value = float(input("Enter the zooming factor (between 0.1 and 10): ")) 

while scaling_value < 0.1 or scaling_value > 10: 
    scaling_value = float(input("Invalid input. Enter the zooming factor (between 0.1 and 10): ")) 

# Create the 2D rotation matrix 
rotated = cv2.getRotationMatrix2D(center=center, angle=rotation_value, scale=1) 
rotated_image = cv2.warpAffine(src=image, M=rotated, dsize=(width, height)) 

# Create the 2D scaling matrix 
scaled = cv2.getRotationMatrix2D(center=center, angle=0, scale=scaling_value) 
scaled_image = cv2.warpAffine(src=rotated_image, M=scaled, dsize=(width, height)) 

# Get translation values from the user 
h = int(input("How many pixels you want the image to be translated horizontally? ")) 
v = int(input("How many pixels you want the image to be translated vertically? ")) 

# Translate the image 
translated_image = translate_image(scaled_image, dx=h, dy=v) 

# Convert the final transformed image from BGR to RGB 
translated_image_rgb = cv2.cvtColor(translated_image, cv2.COLOR_BGR2RGB) 

# Save the final transformed image 
cv2.imwrite('Final_image.png', translated_image) 

# Display the original and final transformed images using subplots 
plt.figure(figsize=(10, 5)) 
# Display the original image 
plt.subplot(1, 2, 1) 
plt.imshow(image_rgb) 
plt.title("Original Image") 
plt.axis("off") 

# Display the final transformed image 
plt.subplot(1, 2, 2) 
plt.imshow(translated_image_rgb) 
plt.title("Final Transformed Image") 
plt.axis("off") 
plt.show() 