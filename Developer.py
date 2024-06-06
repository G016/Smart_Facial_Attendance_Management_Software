from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.title("Developer")
        self.root.geometry("1360x750+0+0")

    #Title
        title_label = Label(self.root, text="DEVELOPER", font=("times new roman", 36, "bold"), bg="light cyan", fg="black")
        title_label.place(x=0, y=0, width=1360, height=50)


    #1st Image
        img1 = Image.open("Images/developer.jpg")
        img1 = img1.resize((1360, 700), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        label_1 = Label(self.root, image=self.photoimg1)
        label_1.place(x=0, y=50, width=1360, height=700)


    # Frame
        main_frame = Frame(label_1,bd=2,bg="white")
        main_frame.place(x=920,y=-2,width=440,height=200)

        img2 = Image.open("Images/ME.jpg")
        img2 = img2.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        label_2 = Label(main_frame, image=self.photoimg2)
        label_2.place(x=235, y=-2, width=200, height=200)

        me_label = Label(main_frame,text="Hello! I am Gaurav Kumar Verma",bg="white",font = ("times new roman",11,"bold"))
        me_label.place(x=0,y=2)








if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()