from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student")
        self.root.geometry("1360x750+0+0")


    #Text Vraiables
        self.var_Branch = StringVar()
        self.var_Session = StringVar()
        self.var_Year = StringVar()
        self.var_Semester = StringVar()
        self.var_Student_Name = StringVar()
        self.var_Roll_No = StringVar()
        self.var_Gender = StringVar()
        self.var_DOB = StringVar()
        self.var_Email = StringVar() 
        self.var_Mobile_No = StringVar()
        self.var_Photo_Sample_Status = StringVar()


    # 1st Image
        img1=Image.open("D:/Study Materials/Projects/Smart Facial Attendance System/Images/college_images/AdobeStock_303989091.jpeg")
        img1=img1.resize((456,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        label_1=Label(self.root,image=self.photoimg1)
        label_1.place(x=0,y=0,width=456,height=130)


    # 2nd Image
        img2=Image.open("D:/Study Materials/Projects/Smart Facial Attendance System/Images/college_images/student-portal_1.jpg")
        img2=img2.resize((456,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        label_1=Label(self.root,image=self.photoimg2)
        label_1.place(x=440,y=0,width=456,height=130)


    # 3rd Image
        img3=Image.open("D:/Study Materials/Projects/Smart Facial Attendance System/Images/college_images/facial-recognition_0.jpg")
        img3=img3.resize((456,130),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        label_1=Label(self.root,image=self.photoimg3)
        label_1.place(x=900,y=0,width=456,height=130)


    # Background Image
        img4=Image.open("D:/Study Materials/Projects/Smart Facial Attendance System/Images/college_images/BG.jpg")
        img4=img4.resize((1360,620),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1360,height=620)

        title_label=Label(bg_img,text="Student Management System",font=("times new roman",36,"bold"),bg="light cyan",fg="red")
        title_label.place(x=0,y=0,width=1360,height=50)


    #Frame
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=70,width=1360,height=480)


    #Left Lable Frame
        Lframe = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font = ("times new roman",11,"bold"))
        Lframe.place(x=10,y=5,width=600,height=460)


    #Current Course Frame
        CC_frame = LabelFrame(Lframe,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font = ("times new roman",11,"bold"))
        CC_frame.place(x=15,y=10,width=565,height=150)

    
    #Branch Label
        Br_label = Label(CC_frame,text="Branch:",bg="white",font = ("times new roman",11,"bold"))
        Br_label.grid(row=0,column=0,sticky=W)
        Br_label.place(x=10,y=20)

        Br_combo = ttk.Combobox(CC_frame,textvariable=self.var_Branch,font = ("times new roman",11,"bold"),state="readonly",width=18)
        Br_combo["values"]=("Select Branch","Computer Science","IT","Civil","Mechanical","Electronics")
        Br_combo.current(0)
        Br_combo.grid(row=0,sticky=W)
        Br_combo.place(x=80,y=20)

    
    #Session Label
        Ss_label = Label(CC_frame,text="Session:",bg="white",font = ("times new roman",11,"bold"))
        Ss_label.grid(row=0,column=2,sticky=W)
        Ss_label.place(x=250,y=20)

        Ss_combo = ttk.Combobox(CC_frame,textvariable=self.var_Session,font = ("times new roman",11,"bold"),state="readonly",width=18)
        Ss_combo["values"]=("Select Session","2020-2024","2021-2025","2022-2026","2023-2027")
        Ss_combo.current(0)
        Ss_combo.grid(row=0,column=3,sticky=W)
        Ss_combo.place(x=320,y=20)


    #Year Label
        Yr_label = Label(CC_frame,text="Year:",bg="white",font = ("times new roman",11,"bold"))
        Yr_label.grid(row=1,column=0,sticky=W)
        Yr_label.place(x=10,y=75)

        Yr_combo = ttk.Combobox(CC_frame,textvariable=self.var_Year,font = ("times new roman",11,"bold"),state="readonly",width=18)
        Yr_combo["values"]=("Select Year","1st","2nd","3rd","4th")
        Yr_combo.current(0)
        Yr_combo.grid(row=1,column=1,sticky=W)
        Yr_combo.place(x=80,y=75)


    #Semester Label
        Sem_label = Label(CC_frame,text="Semester:",bg="white",font = ("times new roman",11,"bold"))
        Sem_label.grid(row=1,column=2,sticky=W)
        Sem_label.place(x=250,y=75)

        Sem_combo = ttk.Combobox(CC_frame,textvariable=self.var_Semester,font = ("times new roman",11,"bold"),state="readonly",width=18)
        Sem_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        Sem_combo.current(0)
        Sem_combo.grid(row=1,column=3,sticky=W)
        Sem_combo.place(x=320,y=75)


    #Student Information Frame
        Cs_frame = LabelFrame(Lframe,bd=2,bg="white",relief=RIDGE,text="Student Information",font = ("times new roman",11,"bold"))
        Cs_frame.place(x=15,y=170,width=565,height=248)


    #Student Name Label
        StdN_label = Label(Cs_frame,text="Student Name:",bg="white",font = ("times new roman",11,"bold"))
        StdN_label.grid(row=0,column=0,sticky=W)
        StdN_label.place(x=10,y=20)

        StdN_entry=ttk.Entry(Cs_frame,textvariable=self.var_Student_Name,width=18,font = ("times new roman",11,"bold"))
        StdN_entry.grid(row=0,column=1,sticky=W)
        StdN_entry.place(x=115,y=20)


    #Roll No. Label
        RollNo_label = Label(Cs_frame,text="Roll No.:",bg="white",font = ("times new roman",11,"bold"))
        RollNo_label.grid(row=0,column=2,sticky=W)
        RollNo_label.place(x=300,y=20)

        RollNo_entry=ttk.Entry(Cs_frame,textvariable=self.var_Roll_No,width=18,font = ("times new roman",11,"bold"))
        RollNo_entry.grid(row=0,column=3,sticky=W)
        RollNo_entry.place(x=390,y=20)


    #Gender Label
        Gd_label = Label(Cs_frame,text="Gender:",bg="white",font = ("times new roman",11,"bold"))
        Gd_label.grid(row=1,column=0,sticky=W)
        Gd_label.place(x=10,y=60)

        Gd_combo = ttk.Combobox(Cs_frame,textvariable=self.var_Gender,font = ("times new roman",11,"bold"),state="readonly",width=18)
        Gd_combo["values"]=("Select Gender","Male","Female","Others")
        Gd_combo.current(0)   
        Gd_combo.grid(row=1,column=1,sticky=W)
        Gd_combo.place(x=115,y=60,width=150)


    #DOB Label
        DOB_label = Label(Cs_frame,text="DOB:",bg="white",font = ("times new roman",11,"bold"))
        DOB_label.grid(row=1,column=2,sticky=W)
        DOB_label.place(x=300,y=60)

        DOB_entry=ttk.Entry(Cs_frame,textvariable=self.var_DOB,width=18,font = ("times new roman",11,"bold"))
        DOB_entry.grid(row=1,column=3,sticky=W)
        DOB_entry.place(x=390,y=100)


      #Email Label
        Email_label = Label(Cs_frame,text="Email:",bg="white",font = ("times new roman",11,"bold"))
        Email_label.grid(row=2,column=0,sticky=W)
        Email_label.place(x=10,y=100)

        Email_entry=ttk.Entry(Cs_frame,textvariable=self.var_Email,width=18,font = ("times new roman",11,"bold"))
        Email_entry.grid(row=2,column=1,sticky=W)
        Email_entry.place(x=115,y=100)
        

    #Mobile No. Label
        Mobno_label = Label(Cs_frame,text="Mobile No.:",bg="white",font = ("times new roman",11,"bold"))
        Mobno_label.grid(row=2,column=2,sticky=W)
        Mobno_label.place(x=300,y=100)
        Mobno_entry=ttk.Entry(Cs_frame,textvariable=self.var_Mobile_No,width=18,font = ("times new roman",11,"bold"))
        Mobno_entry.grid(row=2,column=3,sticky=W)
        Mobno_entry.place(x=390,y=60)
    

    #Radio Buttons
        self.var_Rbtn1=StringVar()
        Rbtn1=ttk.Radiobutton(Cs_frame,variable=self.var_Rbtn1,text="Take Photo Sample",value="Yes")
        Rbtn1.grid(row=3,column=0)
        Rbtn1.place(x=10,y=133)

        Rbtn2=ttk.Radiobutton(Cs_frame,variable=self.var_Rbtn1,text="No Photo Sample",value="No")
        Rbtn2.grid(row=3,column=1)
        Rbtn2.place(x=170,y=133)
    

    #Button Frame
        btn_frame = Frame(Cs_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=-2,y=160,width=565,height=36)

        save_btn = Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman",11,"bold"),bg="red",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame,text="Update",command=self.update_data,width=14,font=("times new roman",11,"bold"),bg="red",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame,text="Delete",command=self.delete_data,width=14,font=("times new roman",11,"bold"),bg="red",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("times new roman",11,"bold"),bg="red",fg="white")
        reset_btn.grid(row=0,column=3)

        

        btn_frame1 = Frame(Cs_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=-2,y=190,width=565,height=40)

        photo_sample_btn = Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=31,font=("times new roman",12,"bold"),bg="red",fg="white")
        photo_sample_btn.grid(row=0,column=0)

        update_photo_btn = Button(btn_frame1,text="Update Photo Sample",width=30,font=("times new roman",12,"bold"),bg="red",fg="white")
        update_photo_btn.grid(row=0,column=1)

        
    #Right Lable Frame
        Rframe = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font = ("times new roman",11,"bold"))
        Rframe.place(x=620,y=5,width=720,height=460)


    #Search System Frame
        Ss_frame = LabelFrame(Rframe,bd=2,bg="white",relief=RIDGE,text="Search System",font = ("times new roman",11,"bold"))
        Ss_frame.place(x=15,y=10,width=685,height=70)  


    #Search By Label
        Sb_label = Label(Ss_frame,text="Search By:",bg="black",fg="white",font = ("times new roman",12,"bold"))
        Sb_label.grid(row=2,column=2,sticky=W)
        Sb_label.place(x=10,y=10)

        Sb_combo = ttk.Combobox(Ss_frame,font = ("times new roman",11,"bold"),state="readonly",width=18)
        Sb_combo["values"]=("Select","Roll No.","Phone No.")
        Sb_combo.current(0)
        Sb_combo.grid(row=0,column=1,sticky=W)
        Sb_combo.place(x=100,y=10)

        Sb_entry=ttk.Entry(Ss_frame,width=20,font = ("times new roman",11,"bold"))
        Sb_entry.grid(row=0,column=2,sticky=W)
        Sb_entry.place(x=280,y=10)

        Search_btn = Button(Ss_frame,text="Search",width=8,font=("times new roman",12,"bold"),bg="black",fg="white")
        Search_btn.grid(row=0,column=3)
        Search_btn.place(x=460,y=8)

        Showall_btn = Button(Ss_frame,text="Show All",width=8,font=("times new roman",12,"bold"),bg="black",fg="white")
        Showall_btn.grid(row=0,column=4)
        Showall_btn.place(x=550,y=8)


    #Table Frame
        table_frame = Frame(Rframe,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=15,y=90,width=685,height=330)
    
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("Branch","Session","Year","Semester","Student Name","Roll No.","Gender","DOB","Email","Mobile No.","Photo Sample Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Branch",text="Branch")
        self.student_table.heading("Session",text="Session")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Student Name",text="Student Name")
        self.student_table.heading("Roll No.",text="Roll_No.")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Mobile No.",text="Mobile No.")
        self.student_table.heading("Photo Sample Status",text="Photo Sample Status")
        self.student_table["show"]="headings"

    #Column Width Adjustments
        self.student_table.column("Branch",width=100)
        self.student_table.column("Session",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Student Name",width=100)
        self.student_table.column("Roll No.",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Mobile No.",width=100)
        self.student_table.column("Photo Sample Status",width=150)
                
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #Function Declaration
    def add_data(self):
        if self.var_Branch.get()=="Select Department" or self.var_Session.get()=="Select Session" or self.var_Year.get()=="Select Year" or self.var_Semester.get()=="Select Semester" or self.var_Student_Name.get()=="" or self.var_Roll_No.get()=="" or self.var_Gender.get()=="" or self.var_DOB.get()=="" or self.var_Email.get()=="" or self.var_Mobile_No.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Gaurav@716",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_Branch.get(),
                                                                                                  self.var_Session.get(),
                                                                                                  self.var_Year.get(),
                                                                                                  self.var_Semester.get(),
                                                                                                  self.var_Student_Name.get(),
                                                                                                  self.var_Roll_No.get(),
                                                                                                  self.var_Gender.get(),
                                                                                                  self.var_DOB.get(),
                                                                                                  self.var_Email.get(),
                                                                                                  self.var_Mobile_No.get(),
                                                                                                  self.var_Rbtn1.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details Has Been Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    #Fetching The Data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Gaurav@716",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close

    #Get Cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_Branch.set(data[0]),
        self.var_Session.set(data[1]),
        self.var_Year.set(data[2]),
        self.var_Semester.set(data[3]),
        self.var_Student_Name.set(data[4]),
        self.var_Roll_No.set(data[5]),
        self.var_Gender.set(data[6]),
        self.var_DOB.set(data[7]),
        self.var_Email.set(data[8]),
        self.var_Mobile_No.set(data[9]),
        self.var_Rbtn1.set(data[10])


    #Update Details
    def update_data(self):
        if self.var_Branch.get()=="Select Department" or self.var_Session.get()=="Select Session" or self.var_Year.get()=="Select Year" or self.var_Semester.get()=="Select Semester" or self.var_Student_Name.get()=="" or self.var_Roll_No.get()=="" or self.var_Gender.get()=="" or self.var_DOB.get()=="" or self.var_Email.get()=="" or self.var_Mobile_No.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do You Want To Update This Student Details?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Gaurav@716",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("UPDATE student SET Branch=%s, Session=%s, Year=%s, Semester=%s, `Roll No.`=%s, Gender=%s, DOB=%s, Email=%s, `Mobile No.`=%s, `Photo Sample Status`=%s WHERE `Student Name`=%s",(self.var_Branch.get(),
                                                                                                                                                                                                                       self.var_Session.get(),
                                                                                                                                                                                                                       self.var_Year.get(),
                                                                                                                                                                                                                       self.var_Semester.get(),
                                                                                                                                                                                                                       self.var_Roll_No.get(),
                                                                                                                                                                                                                       self.var_Gender.get(),
                                                                                                                                                                                                                       self.var_DOB.get(),
                                                                                                                                                                                                                       self.var_Email.get(),
                                                                                                                                                                                                                       self.var_Mobile_No.get(),
                                                                                                                                                                                                                       self.var_Photo_Sample_Status.get(),
                                                                                                                                                                                                                       self.var_Rbtn1.get(),
                                                                                                                                                                                                                       self.var_Student_Name.get()
                                                                                                                                                                                                                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Details Successfully Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)
                

    #Delete Details   
    def delete_data(self):
        if self.var_Student_Name.get() == "":
            messagebox.showerror("Error", "Student Name is Required!")
        else:
            try:
                Delete = messagebox.askyesno("Student Details Delete","Are You Sure You Want To Delete This Student?")
                if Delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Gaurav@716", database="face_recognition")
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM student WHERE `Student Name`=%s"
                    val = (self.var_Student_Name.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not Delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student Details Has Been Deleted Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}")

            
    #Reset Details
    def reset_data(self):
        self.var_Branch.set("Select Branch")
        self.var_Session.set("Select Session")
        self.var_Year.set("Select Year")
        self.var_Semester.set("Select Semester")
        self.var_Student_Name.set("")
        self.var_Roll_No.set("")
        self.var_Gender.set("Select Gender")
        self.var_DOB.set("")
        self.var_Email.set("")
        self.var_Mobile_No.set("")
        self.var_Photo_Sample_Status.set("No")

        self.fetch_data()


    #Take Photo Sample and Generating Datasets
    def generate_dataset(self):
        if self.var_Branch.get()=="Select Department" or self.var_Session.get()=="Select Session" or self.var_Year.get()=="Select Year" or self.var_Semester.get()=="Select Semester" or self.var_Student_Name.get()=="" or self.var_Roll_No.get()=="" or self.var_Gender.get()=="" or self.var_DOB.get()=="" or self.var_Email.get()=="" or self.var_Mobile_No.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Gaurav@716",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("SELECT * FROM student")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("UPDATE student SET Branch=%s, Session=%s, Year=%s, Semester=%s, `Roll No.`=%s, Gender=%s, DOB=%s, Email=%s, `Mobile No.`=%s, `Photo Sample Status`=%s WHERE `Student Name`=%s",(self.var_Branch.get(),
                                                                                                                                                                                                                       self.var_Session.get(),
                                                                                                                                                                                                                       self.var_Year.get(),
                                                                                                                                                                                                                       self.var_Semester.get(),
                                                                                                                                                                                                                       self.var_Roll_No.get(),
                                                                                                                                                                                                                       self.var_Gender.get(),
                                                                                                                                                                                                                       self.var_DOB.get(),
                                                                                                                                                                                                                       self.var_Email.get(),
                                                                                                                                                                                                                       self.var_Mobile_No.get(),
                                                                                                                                                                                                                       self.var_Rbtn1.get(),
                                                                                                                                                                                                                       self.var_Student_Name.get()==id+1
                                                                                                                                                                                                                    )) 
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


    #Loading Datasets XML file from opencv
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)

                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap = cv2.VideoCapture(0)
                img_id = 0

                while True:
                    ret,myframe=cap.read()
                    if face_cropped(myframe) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(myframe),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path = "Datasets/user."+str(id) + "."+str(img_id) + ".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1) == 12 or int(img_id) == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Taking Photo Samples Completed")
            
            except Exception as es:
                messagebox.showinfo("Error",f"Due To: {str(es)}",parent=self.root)



































if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()