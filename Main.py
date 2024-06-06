from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
from Student import Student
from Train import Train
from Face_Recognition import Face_Recognition
from Attendance import Attendance
from Developer import Developer
from Help import Help
from datetime import datetime
from time import strftime
import os
import tkinter


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Face Recognition System")
        self.root.geometry("1360x750+0+0")


    # 1st Image
        img1=Image.open("Images/2-AI-invades-automobile-industry-in-2019.jpeg")
        img1=img1.resize((456,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        label_1=Label(self.root,image=self.photoimg1)
        label_1.place(x=0,y=0,width=456,height=130)


    # 2nd Image
        img2=Image.open("Images/u.jpg")
        img2=img2.resize((456,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        label_1=Label(self.root,image=self.photoimg2)
        label_1.place(x=450,y=0,width=456,height=130)


    # 3rd Image
        img3=Image.open("Images/images.jpg")
        img3=img3.resize((458,130),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        label_1=Label(self.root,image=self.photoimg3)
        label_1.place(x=900,y=0,width=458,height=130)


    # Background Image
        img4=Image.open("Images/BG.jpg")
        img4=img4.resize((1360,620),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1360,height=620)

        title_label=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",36,"bold"),bg="light cyan",fg="red")
        title_label.place(x=0,y=0,width=1360,height=50)

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl = Label(bg_img,font=('times new roman',13,'bold'),background='lightcyan',foreground='black')
        lbl.place(x=0,y=50,width=100,height=30)
        time()


    # Student Button
        img5=Image.open("Images/student1.jpg")
        img5=img5.resize((160,160),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="spider red")
        b1.place(x=200,y=100,width=160,height=160)

        b1_SD = Button(bg_img,text="Student Details",command=self.student_details,cursor="spider red",font=("times new roman",11,"bold"),bg="light cyan")
        b1_SD.place(x=200,y=250,width=160,height=20)


     # Detect Face Button
        img6=Image.open("Images/Face_detecter.jpg")
        img6=img6.resize((160,160),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b2 = Button(bg_img,image=self.photoimg6,cursor="spider red",command=self.face_data)
        b2.place(x=460,y=100,width=160,height=160)

        b2_FD = Button(bg_img,text="Detect Face",cursor="spider red",command=self.face_data,font=("times new roman",11,"bold"),bg="light cyan")
        b2_FD.place(x=460,y=250,width=160,height=20)


    # Attendance Button
        img7=Image.open("Images/iStock-182059956_18390_t12.jpg")
        img7=img7.resize((160,160),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b2 = Button(bg_img,image=self.photoimg7,command=self.attend,cursor="spider red")
        b2.place(x=720,y=100,width=160,height=160)

        b2_FD = Button(bg_img,text="Attendance",command=self.attend,cursor="spider red",font=("times new roman",11,"bold"),bg="light cyan")
        b2_FD.place(x=720,y=250,width=160,height=20)


    # Help Button
        img8=Image.open("Images/HELP.png")
        img8=img8.resize((160,160),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b2 = Button(bg_img,command=self.help,image=self.photoimg8,cursor="spider red")
        b2.place(x=980,y=100,width=160,height=160)

        b2_FD = Button(bg_img,text="Help",command=self.help,cursor="spider red",font=("times new roman",11,"bold"),bg="light cyan")
        b2_FD.place(x=980,y=250,width=160,height=20)


    # Train Data Button
        img9=Image.open("Images/Train Data.jpg")
        img9=img9.resize((160,160),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b2 = Button(bg_img,image=self.photoimg9,command=self.train_data,cursor="spider red")
        b2.place(x=200,y=330,width=160,height=160)

        b2_FD = Button(bg_img,text="Train Data",command=self.train_data,cursor="spider red",font=("times new roman",11,"bold"),bg="light cyan")
        b2_FD.place(x=200,y=480,width=160,height=20)


     # Photos Button
        img10=Image.open("Images/Photos.png")
        img10=img10.resize((160,160),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b2 = Button(bg_img,image=self.photoimg10,cursor="spider red",command=self.open_img)
        b2.place(x=460,y=330,width=160,height=160)

        b2_FD = Button(bg_img,text="Photos",cursor="spider red",command=self.open_img,font=("times new roman",11,"bold"),bg="light cyan")
        b2_FD.place(x=460,y=480,width=160,height=20)


     # Developer Button
        img11=Image.open("Images/Developer.jpeg")
        img11=img11.resize((160,160),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b2 = Button(bg_img,command=self.dev,image=self.photoimg11,cursor="spider red")
        b2.place(x=720,y=330,width=160,height=160)

        b2_FD = Button(bg_img,text="Developer",command=self.dev,cursor="spider red",font=("times new roman",11,"bold"),bg="light cyan")
        b2_FD.place(x=720,y=480,width=160,height=20)


     # Exit Button
        img12=Image.open("Images/Exit.png")
        img12=img12.resize((160,160),Image.Resampling.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b2 = Button(bg_img,command=self.exit,image=self.photoimg12,cursor="spider red")
        b2.place(x=980,y=330,width=160,height=160)

        b2_FD = Button(bg_img,command=self.exit,text="Exit",cursor="spider red",font=("times new roman",11,"bold"),bg="light cyan")
        b2_FD.place(x=980,y=480,width=160,height=20)


    #Open Photo Sample File
    def open_img(self):
        os.startfile("Datasets")

    
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition","Are You Sure To Exit?",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return

    
    #Function Buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)


    def attend(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)


    def dev(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)


    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()