import numpy as np
import cv2 as cv
cap = cv.VideoCapture('finish.mov') # change to the name of the video you want to process
h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
middle = int(cap.get(cv.CAP_PROP_FRAME_WIDTH)/2) # may need to add an offset if the LEDs are not perfectly in the centre of the video
w = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
slice=16 # adjust to get a good picture of the LEDs with as little waste as possible
buf = np.zeros((h,w*slice,3),np.uint8)
f = w-1 # Assume that the camera is on the right (outside) of the track and the LEDs are on the left (inside) of the track so the photofinish is filled from the right hand side
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    buf[:,f*slice:f*slice+slice,:]=frame[::,middle-int(slice/2):middle+int(slice/2),:]
    f-=1; # fills the photofinish from the right hand side
    if cv.waitKey(1) == ord('q'):
        break
cv.imshow("finish",buf)
cv.waitKey(0)
cv.imwrite("photfin.jpg",buf) # change to the desired output name and format
cap.release()
cv.destroyAllWindows()