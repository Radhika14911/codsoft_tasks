import cv2
import csv
from datetime import datetime
import os

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")
attendance_file = "attendance.csv"

if not os.path.exists(attendance_file):
    with open(attendance_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Date", "Time"])

marked_names = set()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:

        face = gray[y:y+h, x:x+w]

        id, confidence = recognizer.predict(face)

        if confidence < 70:
            name = "Radhika"

            if name not in marked_names:
                now = datetime.now()

                date = now.strftime("%d-%m-%Y")
                time = now.strftime("%H:%M:%S")

                with open(attendance_file, "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow([name, date, time])
                    print(f"Attendance Marked: {name}")

                marked_names.add(name)

        else:
            name = "Unknown"

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

        cv2.putText(
            frame,
            name,
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,0),
            2
        )

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()