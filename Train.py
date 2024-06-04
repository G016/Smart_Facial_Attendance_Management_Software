from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import numpy as np
import cv2


class Train:
    def __init__(self, root):
        self.root = root
        self.root.title("Train Datasets")
        self.root.geometry("1360x750+0+0")


    #Title
        title_label = Label(self.root, text="Train Datasets", font=("times new roman", 36, "bold"), bg="light cyan", fg="red")
        title_label.place(x=0, y=0, width=1360, height=50)


    #1st Image
        img1 = Image.open("Images/facialrecognition.png")
        img1 = img1.resize((1360, 300), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        label_1 = Label(self.root, image=self.photoimg1)
        label_1.place(x=0, y=50, width=1360, height=300)


    #2nd Image
        img2 = Image.open("Images/gettyimages-1022573162.jpg")
        img2 = img2.resize((1360, 300), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        label_1 = Label(self.root, image=self.photoimg2)
        label_1.place(x=0, y=400, width=1360, height=300)


    #Train Button
        b_FD = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="spider red", fg="white", font=("times new roman", 16, "bold"), bg="red")
        b_FD.place(x=0, y=350, width=1360, height=50)


    #Train Data
    def train_classifier(self):
        data_dir = "Datasets"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img, "uint8")
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        ids = np.array(ids)


    #Train The Classifier And Save Them
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Datasets Completed")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
