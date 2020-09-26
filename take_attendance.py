import cv2
import numpy as np
from pyzbar.pyzbar import decode
from playsound import playsound

record = cv2.VideoCapture(0)
record.set(3,640)
record.set(4,480)

present_data=[]

while(1):
    s, img = record.read()
    for qr in decode(img):
        data=qr.data.decode('utf-8')
        #print(data)
        if data not in present_data:
            present_data.append(data)
            #print(10*'\a')
            playsound('beep.mp3')

        #box around
        pts = np.array([qr.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        color=(255,0,255)
        cv2.polylines(img,[pts],1,color,5)

        #display on image
        pts2 = qr.rect
        cv2.putText(img,data,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_PLAIN, 1,color,2)

    cv2.imshow('Result',img)
    key = cv2.waitKey(1)

    #to release camera frame
    if(key==27):
        cv2.destroyWindow("Result")
        record.release()
        break
    
print(present_data)
