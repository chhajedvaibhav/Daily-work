import cv2
import os
from pdf2image import convert_from_path

images = os.listdir('../images')
print(images[0])
for i in range(len(images)):
    images[i] = '../images/' + images[i]

pages = convert_from_path(images[0], 500)

for page in pages:
    page.save('out.jpg', 'JPEG')
print(pages)

image = cv2.imread('out.jpg')
cv2.waitKey(0) 

# Grayscale 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

# Find Canny edges 
edged = cv2.Canny(gray, 30, 200) 
cv2.waitKey(0) 

# Finding Contours 
# Use a copy of the image e.g. edged.copy() 
# since findContours alters the image 
contours, hierarchy = cv2.findContours(edged,  
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
  
cv2.imshow('Canny Edges After Contouring', edged) 
cv2.imwrite('edge.jpg',edged)
#cv2.waitKey(0) 
  
print("Number of Contours found = " + str(len(contours))) 
  
# Draw all contours 
# -1 signifies drawing all contours 
cv2.drawContours(image, contours, -1, (0, 255, 0), 3) 
  
cv2.imshow('Contours', image) 
cv2.imwrite('countours.jpg', image)
#cv2.waitKey(0) 
cv2.destroyAllWindows() 

'''
resize = cv2.resize(img, None, fx=0.3, fy=0.3, interpolation = cv2.INTER_CUBIC)
gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,50,255,cv2.THRESH_BINARY_INV)
_, contours = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    size = cv2.contourArea(cnt)
    if 100 < size < 30000:
        cv2.drawContours(resize, [cnt], 0, (0,255,0), 1)

cv2.imshow('out.jpg', resize)
'''