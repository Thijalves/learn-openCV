import cv2 as cv
import time

lastTime = 0
currentTime = 0

capture = cv.VideoCapture(0)
haar_cascade = cv.CascadeClassifier('haar_face.xml')

while True:

    currentTime = time.time()

    #getFrame
    isTrue, frame = capture.read()

    #change to gray
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #detect faces
    faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # draw rectangle
    for (x,y,w,h) in faces:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 4)
        cv.putText(frame, 'X: %d  y: %d' % (x, y), (x,y+h+14), cv.FONT_HERSHEY_PLAIN, 1, (0,255,0), 1)

    #FPS
    cv.putText(frame, 'FPS: %d' % (1/(currentTime-lastTime)), (100,100), cv.FONT_HERSHEY_PLAIN, 2, (0,255,0), 1)

    cv.imshow('Rostos Encontrados', frame)

    lastTime = currentTime

    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()