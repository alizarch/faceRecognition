import cv2
from helper import DBHelper
from pydantic import BaseModel

class User(BaseModel):
    user_id : int
    username : str

def datasetCreator():
    helper = DBHelper()
    vid_cam = cv2.VideoCapture(0)
    face_detector = cv2.CascadeClassifier('xml_file/aiFace_haarcascade.xml')
    id = input("enter user ID: ")
    username  = input('Enter Username: ')
    external_data = {
        "user_id" : id,
        "username" : username,
    }
    user = User(**external_data)
    helper.insert_user(user.user_id,user.username)
    count = 0
    while(True):
        ret, image_frame = vid_cam.read()
        gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            #image, start_point, end_point, color, thickness
            cv2.rectangle(image_frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
            count += 1
            file_name = "data/dataset/" + id + "_" + str(count) + ".jpg"
            cv2.imwrite(file_name, gray[y:y+h, x:x+w])
            cv2.imshow('frame', image_frame)
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break
        elif count > 10:
            break
    vid_cam.release()
    cv2.destroyAllWindows()