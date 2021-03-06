"""
Created on Sat Nov 20 20:16:12 2021

@author: Hoda
"""
import cv2

#create a CascadeClassifier Object
face_cascade =  cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Reading the image as it is 
img = cv2.imread("lena.jpg")

#Reading the image in grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Search the coordinates of the image 
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors=5)

print (type(faces))
print (faces)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 1)
"""
(x,y) start edge of the rectangle
(x+w,y+h) end of rectangle 
w and h are the length of the drawn rectangle

(0,255,0) ==> BGR value of the rectangle outline

1 ==> width of the rectangle
"""

#resized = cv2.resize(img, (int(img.shape[1]*2),int(img.shape[0]*2)))

cv2.imshow ("Lena", img)
cv2.waitKey(0)
cv2.destroyAllwindows()
