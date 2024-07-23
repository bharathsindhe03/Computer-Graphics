import cv2 
import numpy as np 
import matplotlib.pyplot as plt  # Importing matplotlib.pyplot 

# Read the image 
img = cv2.imread("rnsit.jpg") 

# Get the height and width of the image 
height, width = img.shape[:2]

# Split the image into four quadrants 
quad1 = img[:height//2, :width//2] # slices the image to get the top-left quadrant. 
quad2 = img[:height//2, width//2:] #slices the image to get the top-right quadrant. 
quad3 = img[height//2:, :width//2] #slices the image to get the bottom-left quadrant. 
quad4 = img[height//2:, width//2:] #slices the image to get the bottom-right quadrant. 

plt.figure(figsize=(10, 5)) 
plt.subplot(1, 2, 1) 
plt.imshow(cv2.cvtColor(quad1, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB 
plt.title("1") 
plt.axis("off") 

plt.subplot(1, 2, 2) 
plt.imshow(cv2.cvtColor(quad2, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB 
plt.title("2") 
plt.axis("off") 

plt.figure(figsize=(10, 5)) 
plt.subplot(1, 2, 1) 
plt.imshow(cv2.cvtColor(quad3, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB 
plt.title("3") 
plt.axis("off") 

plt.subplot(1, 2, 2) 
plt.imshow(cv2.cvtColor(quad4, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB 
plt.title("4") 
plt.axis("off") 

plt.show()