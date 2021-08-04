import numpy as np
import cv2
#0 is for camera1 (if there  are multiple cameras)
vid=cv2.VideoCapture(0)

while(True):
    #capture the video frame by frame
    ret,frame=vid.read()
    #if frame is read correctly 'ret' is true
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #display the resulting frame
    cv2.imshow('Color Frame',gray)

    #just if you want to save it(not required in this program)
    #cv2.imwrite("./123/pic1.png",gray)



    #the 'q' button is set as the quitting button
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break


vid.release()

#destroy all the windows
cv2.destroyAllWindows()

#If you notice, it's a gray image(camera opens and shows)
#presssing on 'q' it closes