import cv2
import os
import numpy as np
from PIL import Image


def trainer(datapath):
    faceCascade = cv2.CascadeClassifier('xml_file/aiFace_haarcascade.xml')
    image_paths = [os.path.join(datapath, f) for f in os.listdir(datapath)]
    # images will contains face images
    images = []
    # labels will contains the label that is assigned to the image
    labels = []
    for image_path in image_paths:
        # Read the image and convert to grayscale
        image_pil = Image.open(image_path).convert('L')
        # Convert the image format into numpy array
        image = np.array(image_pil, 'uint8')
        # Get the label of the image
        nbr = int(os.path.split(image_path)[1].split("_")[0].replace("face-", ""))
        # nbr=int(''.join(str(ord(c)) for c in nbr))
        print(nbr)
        # Detect the face in the image
        faces = faceCascade.detectMultiScale(image)
        # If face is detected, append the face to images and the label to labels
        for (x, y, w, h) in faces:
            images.append(image[y: y + h, x: x + w])
            labels.append(nbr)
            cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
            cv2.waitKey(10)
    # return the images list and labels list
    return images, labels
