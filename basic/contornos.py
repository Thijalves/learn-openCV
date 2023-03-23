import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Original', img)

blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow('Blank', blank)

#transformamos em ciza
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Cinza', gray)

#borramos
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#extraimos as bordas
canny = cv.Canny(blur, 125, 175)
cv.imshow('Bordas', canny)

#pegamos os contornos
contornos, hierarquias = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

#printa a quantidade de contornos
print(f'{len(contornos)} contornos encontrados!')

cv.drawContours(blank, contornos, -1, (0,255,0), 1)
# cv.imshow('Contornos encontrados', blank)

cv.waitKey(0)