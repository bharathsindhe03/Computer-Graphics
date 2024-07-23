import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

# Load the image in grayscale 
img = cv2.imread("rnsit.jpg", cv2.IMREAD_GRAYSCALE) 

# Apply Gaussian blur (blurring) 
gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0) 

# Apply bilateral filter (smoothening) 
bilateral_blur = cv2.bilateralFilter(img, 9, 75, 75) 

# Display the original, blurred, and smoothened images using matplotlib 
plt.figure(figsize=(25, 10)) 
plt.subplot(1, 3, 1) 
plt.imshow(img, cmap='gray') 
plt.title("Original Grayscale Image") 
plt.axis("off") 

plt.subplot(1, 3, 2) 
plt.imshow(gaussian_blur, cmap='gray') 
plt.title("Blurred Image (Gaussian Blur)") 
plt.axis("off") 

plt.subplot(1, 3, 3) 
plt.imshow(bilateral_blur, cmap='gray') 
plt.title("Smoothened Image (Bilateral Filter)") 
plt.axis("off") 

plt.show()