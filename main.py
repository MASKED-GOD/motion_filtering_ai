import cv2 as cv

video = cv.VideoCapture(0)
substractor = cv.createBackgroundSubtractorMOG2(300,20)

while True:
    ret ,frame = video.read()

    if ret:
        mask = substractor.apply(frame)
        cv.imshow('mask',mask)

        if cv.waitKey(5) == ord('q'):
            break
    else:
        print("failed to capture frame")

cv.destroyAllWindows()
video.release()