import cv2
from helper import DBHelper
from datetime import date

def detector():
    helper = DBHelper()
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('data/recognizer/trainertrainer.yml')
    faceCascade = cv2.CascadeClassifier('xml_file/aiFace_haarcascade.xml')
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX  # Creates a font
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
        for(x, y, w, h) in faces:
            nbr_predicted , conf = recognizer.predict(gray[y:y+h, x:x+w])

            cv2.rectangle(im, (x-50, y-50), (x+w+50, y+h+50), (225, 0, 0), 2)
            userid = helper.Fetch_by_id(int(nbr_predicted))
            """external_data = {
                "user_id": userid[0],
                "username": userid[1],
            }"""
            #user = User(**external_data)
            if(nbr_predicted == userid[0]):
                nbr_predicted = userid[1]

            cv2.putText(im, str(nbr_predicted),(x, y+h), font,1.1, (0, 255, 0), 2)  # Draw the text
            cv2.imshow('im', im)
            attandance = helper.Fetch_by_id_attendance(nbr_predicted)
            if attandance != date.today():
                helper.insert_attandance(userid[0])
            cv2.waitKey(10) & 0xFF == ord('q')
