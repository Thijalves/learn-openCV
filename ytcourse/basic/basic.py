import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Original', img)

#converter para escala de cinza
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

#blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

#edge cascade (inserir uma imagem borrada melhra o efeito)
canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges' , canny)

#Dialating the image
dilated = cv.dilate(canny, (7,7), 3)
# cv.imshow('Dilated', dilated)

#eroding
eroded = cv.erode(dilated, (7,7), 3)
# cv.imshow('Eroded', eroded)

#resize
resized = cv.resize(img, (500, 500))
# cv.imshow('Resized', resized)

#crop
cropped = img[50:200, 200:400]
# cv.imshow('Crpopped', cropped)

cv.waitKey(0)
