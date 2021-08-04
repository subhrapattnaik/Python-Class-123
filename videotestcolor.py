import cv2
#0 is for camera1 (if there  are multiple cameras)
vid=cv2.VideoCapture(0)

while(True):
    #capture the video frame by frame
    ret,frame=vid.read()

    #display the resulting frame
    cv2.imshow('Color Frame',frame)

    #the 'q' button is set as the quitting button
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break


vid.release()

#destroy all the windows
cv2.destroyAllWindows()

#If you notice, it's a colour image(camera opens and shows)
#presssing on 'q' it closes