import cv2
import os
import numpy as np

dataset_path = "../dataset/Radhika"

faces = []
labels = []

for image_name in os.listdir(dataset_path):

    image_path = os.path.join(dataset_path, image_name)

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    faces.append(img)
    labels.append(1)

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.train(faces, np.array(labels))

recognizer.save("trainer.yml")

print("Model trained successfully!")