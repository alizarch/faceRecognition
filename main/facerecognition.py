import cv2
import numpy as np
import sys
path = r"D:\Ali Zar\Soft Solutions\Internship\Python\Django\virtual_environment\FB projects\Angelica Lacerna\Fase_Recognition\modules"
sys.path.insert(1, path)
from trainer import trainer
from datasetCreator import datasetCreator
from detctor import detector



def main():
    while True:
        print("Enter 1 for create dataset of user")
        print("Enter 2 for train dataset")
        print("Enter 3 for Recognition")
        choise= input("Enter number: ")

        if choise == "1":
            try:
                datasetCreator()
                print("******************Dataset create successfully******************")
            except Exception as a:
                print("ERROR",a)

        elif choise == "2":
            try:
                recognizer = cv2.face.LBPHFaceRecognizer_create()
                dataPath = 'data/dataSet'
                images, labels = trainer(dataPath)
                cv2.imshow('test', images[0])
                cv2.waitKey(1)
                recognizer.train(images, np.array(labels))
                recognizer.save('data/recognizer/trainertrainer.yml')
                cv2.destroyAllWindows()
                print("******************Dataset train successfully******************")
            except Exception as a:
                print("Dataset is empty", a)

        elif choise == "3":
            try:
                detector()
            except Exception as a:
                print("Dataset is empty", a)
        else:
            print("Please choose right choice")


if __name__ == "__main__":
   main()

