from sys import path
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import numpy as np
import cv2
import mysql.connector

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition")
        self.root.geometry("1360x750+0+0")

        # Title
        title_label = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 36, "bold"), bg="light cyan", fg="red")
        title_label.place(x=0, y=0, width=1360, height=50)

        # 1st Image
        img1 = Image.open("Images/face_detector1.jpg")
        img1 = img1.resize((560, 650), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        label_1 = Label(self.root, image=self.photoimg1)
        label_1.place(x=0, y=50, width=560, height=650)

        # 2nd Image
        img2 = Image.open("Images/facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img2 = img2.resize((800, 650), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        label_2 = Label(self.root, image=self.photoimg2)
        label_2.place(x=560, y=50, width=800, height=650)

        # Recognize Face Button
        b_FD = Button(label_2, text="Recognize Face", command=self.face_recog, cursor="hand2", fg="white", font=("times new roman", 16, "bold"), bg="blue")
        b_FD.place(x=300, y=570, width=200, height=40)

    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])

                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(username='root', password='Gaurav@716', host='localhost', database='face_recognition')
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT `Student Name` FROM student WHERE `Student Name`=%s", (str(id),))
                n = my_cursor.fetchone()
                if n is not None:
                    n = "+".join(n)
                else:
                    n = "Unknown"

                my_cursor.execute("SELECT `Roll No.` FROM student WHERE `Student Name`=%s", (str(id),))
                r = my_cursor.fetchone()
                if r is not None:
                    r = "+".join(r)
                else:
                    r = "Unknown"

                my_cursor.execute("SELECT Branch FROM student WHERE `Student Name`=%s", (str(id),))
                b = my_cursor.fetchone()
                if b is not None:
                    b = "+".join(b)
                else:
                    b = "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"Student Name:{n}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Roll No.:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Branch:{b}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Detector",img)

            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()  


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
