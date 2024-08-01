import cv2 
import matplotlib.pyplot as plt 

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml') 

image_path = 'face.jpg' 
image = cv2.imread(image_path) 

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5) 

for (x, y, w, h) in faces: 
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2) 

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 

plt.imshow(image_rgb) 
plt.title('Detected Faces') 
plt.axis('off')  

plt.show()