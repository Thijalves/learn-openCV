import cv2 as cv
import numpy as np

lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

video =  cv.VideoCapture('Videos/pikachu.mp4')

while True:
    isTrue, frame = video.read()
    cv.imshow('Video', frame)

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # cv.imshow('HSV', hsv)

    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # cv.imshow('Mask', mask)

    contornos, hierarquias = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for contorno in contornos:
        if cv.contourArea(contorno) > 250:
            x,y,w,h = cv.boundingRect(contorno)
            cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 1)
            cv.putText(frame, 'X: %d  y: %d' % (x, y), (x,y+h+14), cv.FONT_HERSHEY_PLAIN, 1, (0,255,0), 1)

    # result = cv.bitwise_and(hsv, hsv, mask=mask)
    cv.imshow('Resultado',  frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

video.release()
cv.destroyAllWindows()