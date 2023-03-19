import cv2 as cv
import numpy as np

#criando a imagem
blank = np.zeros((500, 500,3), dtype='uint8')
cv.imshow('blank Page', blank)

#1. pintar de alguma cor
# blank[:] = 0,0,255
# cv.imshow('pagina pintada', blank)

#2.retangulo
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness = 2)
# cv.imshow('Retangulo', blank)

#ciculo
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 50, (255, 0, 0), -1)
# cv.imshow('circulo', blank)

#linha...

#texto
cv.putText(blank, 'Hello World', (200, 255), cv.FONT_HERSHEY_TRIPLEX, 0.75, (255,255,255), 2)
cv.imshow('texto', blank)

cv.waitKey(0)