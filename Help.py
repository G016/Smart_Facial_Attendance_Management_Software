from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.title("Help")
        self.root.geometry("1360x750+0+0")

    #Title
        title_label = Label(self.root, text="HELP DESK", font=("times new roman", 36, "bold"), bg="black", fg="white")
        title_label.place(x=0, y=0, width=1360, height=50)


    #1st Image
        img = Image.open("Images/Developer.jpeg")
        img = img.resize((1360, 700), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        label = Label(self.root, image=self.photoimg)
        label.place(x=0, y=50, width=1360, height=700)

        help_label = Label(label,text="g.pverma716@gmail.com",bg="gray15",fg="white",font = ("times new roman",16,"bold"))
        help_label.place(x=500,y=170,width=360,height=40)




if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()