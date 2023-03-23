import cv2 as cv
import numpy as np

img = cv.imread('Images/demo.jpg')
cv.imshow('Original', img)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

lower_blue = np.array([240, 50, 50])
upper_blue = np.array([130, 255, 255])

mask = cv.inRange(hsv, lower_blue, upper_blue)
# cv.imshow('Mask', mask)

result = cv.bitwise_and(hsv, hsv, mask=mask)
# cv.imshow('Resultado',  cv.cvtColor(result, cv.COLOR_HSV2BGR))

contornos, hierarquias = cv.findContours(mask, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# cv.drawContours(img, contornos, -1, (0,0,0), 2)
# cv.imshow('Contornos encontrados', img)

for contorno in contornos:
    x,y,w,h = cv.boundingRect(contorno)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
    cv.putText(img, 'X: %d  y: %d' % (x, y), (x,y+h+14), cv.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)

cv.imshow('Azul detectado', img)

cv.waitKey(0)
cv.destroyAllWindows()
