import cv2 as cv

#ler e abrir imagens =========================
# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat', img)
# cv.waitKey(0)
#=============================================

#ler e abrir videos ==========================
# capture = cv.VideoCapture('Videos/dog.mp4')

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)

#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()
#=============================================

#redimensionar imagens =======================
# img = cv.imread('Photos/cat_large.jpg')

# def rescaleFrame(frame, scale = 0.5):
#     height = int(frame.shape[0] * scale)
#     width = int(frame.shape[1] * scale)
#     dimensions = (width, height)
#     return cv.resize(frame, dimensions)

# cv.imshow('Cat', rescaleFrame(img))
# cv.waitKey(0)
#=============================================
