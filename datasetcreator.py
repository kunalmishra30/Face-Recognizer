import cv2
import os
cascPath = "haarcascade_frontalface_alt.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
people = input("Enter the name of the person : ")
os.mkdir('images/'+people)
i=0
video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.3,minSize=(30,30))

    for (x,y,w,h) in faces:
        i = i+1
        temp="images/" + people + "/" + str(i) +".jpg"
        cv2.imwrite(temp, gray[y:y +h, x:x +w])
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.waitKey(1)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) | 0xFF == ord('q'):
          break
        if (i>50):
            break
    if (i>50):
            break
    if cv2.waitKey(1) | 0xFF == ord('q'):
        break
    
video_capture.release()
#cv2.destroyAllWindow()











