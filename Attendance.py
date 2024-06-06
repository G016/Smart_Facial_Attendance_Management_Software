from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import filedialog
from time import strftime
from datetime import datetime
import mysql.connector
import cv2
import os
import csv


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.title("Attendance Portal")
        self.root.geometry("1360x750+0+0")


    # Text Variables
        self.var_Attendance_ID=StringVar()
        self.var_Student_Name=StringVar()
        self.var_Branch=StringVar()
        self.var_Roll_No=StringVar()
        self.var_Date=StringVar()
        self.var_Time=StringVar()
        self.var_Status=StringVar()


    # 1st Image
        img1=Image.open("Images/AdobeStock_303989091.jpeg")
        img1=img1.resize((680,160),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        label_1=Label(self.root,image=self.photoimg1)
        label_1.place(x=0,y=0,width=680,height=160)


    # 2nd Image
        img2=Image.open("Images/iStock-182059956_18390_t12.jpg")
        img2=img2.resize((856,160),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        label_1=Label(self.root,image=self.photoimg2)
        label_1.place(x=680,y=0,width=680,height=160)


    # Background Image
        img3=Image.open("Images/BG.jpg")
        img3=img3.resize((1360,620),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1360,height=620)

        title_label=Label(bg_img,text="STUDENT ATTENDACE MANAGEMENT",font=("times new  roman",36,"bold"),bg="light cyan",fg="red")
        title_label.place(x=0,y=0,width=1360,height=50)

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl = Label(title_label,font=('times new roman',13,'bold'),background='lightcyan',foreground='black')
        lbl.place(x=0,y=(-8),width=100,height=30)
        time()


    #Frame
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=70,width=1320,height=480)


    #Left Lable Frame
        Lframe = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font = ("times new roman",11,"bold"))
        Lframe.place(x=10,y=5,width=600,height=460)


    #Attendance ID Label
        Atdid_label = Label(Lframe,text="Attendance ID:",bg="white",font = ("times new roman",11,"bold"))
        Atdid_label.grid(row=0,column=0,sticky=W)
        Atdid_label.place(x=10,y=40)

        Atdid_entry=ttk.Entry(Lframe,width=18,textvariable=self.var_Attendance_ID,font = ("times new roman",11,"bold"))
        Atdid_entry.grid(row=0,column=1,sticky=W)
        Atdid_entry.place(x=120,y=40)


    #Student Name Label
        Sdn_label = Label(Lframe,text="Student Name:",bg="white",font = ("times new roman",11,"bold"))
        Sdn_label.grid(row=0,column=2,sticky=W)
        Sdn_label.place(x=320,y=40)

        Sdn_entry=ttk.Entry(Lframe,width=18,textvariable=self.var_Student_Name,font = ("times new roman",11,"bold"))
        Sdn_entry.grid(row=0,column=3,sticky=W)
        Sdn_entry.place(x=430,y=40)


    #Branch Label
        Branch_label = Label(Lframe,text="Branch:",bg="white",font = ("times new roman",11,"bold"))
        Branch_label.grid(row=1,column=0,sticky=W)
        Branch_label.place(x=10,y=100)

        Branch_combo = ttk.Combobox(Lframe,textvariable=self.var_Branch,font = ("times new roman",11,"bold"),state="readonly",width=18)
        Branch_combo["values"]=("Select Branch","Computer Science","IT","Civil","Mechanical","Electronics")
        Branch_combo.current(0) 
        Branch_combo.grid(row=1,column=1,sticky=W)
        Branch_combo.place(x=120,y=100,width=150)


    #Roll No. Label
        Roll_label = Label(Lframe,text="Roll No.:",bg="white",font = ("times new roman",11,"bold"))
        Roll_label.grid(row=1,column=2,sticky=W)
        Roll_label.place(x=320,y=100)

        Roll_entry = ttk.Entry(Lframe,textvariable=self.var_Roll_No,font = ("times new roman",11,"bold"),width=18) 
        Roll_entry.grid(row=2,column=0,sticky=W)
        Roll_entry.place(x=430,y=100,width=150)


    #Date Label
        Date_label = Label(Lframe,text="Date:",bg="white",font = ("times new roman",11,"bold"))
        Date_label.grid(row=2,column=2,sticky=W)
        Date_label.place(x=10,y=160)

        Date_entry=ttk.Entry(Lframe,textvariable=self.var_Date,width=18,font = ("times new roman",11,"bold"))
        Date_entry.grid(row=2,column=1,sticky=W)
        Date_entry.place(x=120,y=160)


    # Time No. Label
        Time_label = Label(Lframe,text="Time:",bg="white",font = ("times new roman",11,"bold"))
        Time_label.grid(row=2,column=2,sticky=W)
        Time_label.place(x=320,y=160)

        Time_entry = ttk.Entry(Lframe,textvariable=self.var_Time,font = ("times new roman",11,"bold"),width=18) 
        Time_entry.grid(row=2,column=3,sticky=W)
        Time_entry.place(x=430,y=160,width=150)


    # Status Label
        Status_label = Label(Lframe,text="Attendance Status:",bg="white",font = ("times new roman",11,"bold"))
        Status_label.grid(row=3,column=0,sticky=W)
        Status_label.place(x=10,y=220)

        Status_combo = ttk.Combobox(Lframe,textvariable=self.var_Status,font = ("times new roman",11,"bold"),state="readonly",width=18)
        Status_combo["values"]=("Select Status","Present","Absent")
        Status_combo.current(0) 
        Status_combo.grid(row=3,column=1,sticky=W)
        Status_combo.place(x=160,y=220,width=150)


    #Button Frame
        btn_frame = Frame(Lframe,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=2,y=320,width=590,height=36)

        import_btn = Button(btn_frame,text="Import CSV",command=self.importcsv,width=21,font=("times new roman",12,"bold"),bg="red",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn = Button(btn_frame,text="Export CSV",command=self.exportcsv,width=21,font=("times new roman",12,"bold"),bg="red",fg="white")
        export_btn.grid(row=0,column=1)

        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=20,font=("times new roman",12,"bold"),bg="red",fg="white")
        reset_btn.grid(row=0,column=3)


    # Right Lable Frame
        Rframe = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Data",font = ("times new roman",11,"bold"))
        Rframe.place(x=620,y=5,width=685,height=460)


    # Table Frame
        table_frame = Frame(Rframe,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=10,y=10,width=660,height=415)

    
    #Scroll Bar
        scroll_x =ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y =ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("Attendance ID","Student Name","Branch","Roll No.","Date","Time","Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("Attendance ID",text="Attendance ID")
        self.AttendanceReportTable.heading("Student Name",text="Student Name")
        self.AttendanceReportTable.heading("Branch",text="Branch")
        self.AttendanceReportTable.heading("Roll No.",text="Roll No.")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Status",text="Status")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("Attendance ID",width=100)
        self.AttendanceReportTable.column("Student Name",width=150)
        self.AttendanceReportTable.column("Branch",width=100)
        self.AttendanceReportTable.column("Roll No.",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Status",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    # Fetch Attendance Data
    def fetchdata(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)


    # Import CSV Button    
    def importcsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)


    # Export CSV Button
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found To Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Data Successfully Exported To"+os.path.basename(fln))
        except Exception as es:
            messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)


    # Get Cursor
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']

        self.var_Attendance_ID.set(rows[0])
        self.var_Student_Name.set(rows[1])
        self.var_Branch.set(rows[2])
        self.var_Roll_No.set(rows[3])
        self.var_Date.set(rows[4])
        self.var_Time.set(rows[5])
        self.var_Status.set(rows[6])


    #Reset Button
    def reset_data(self):
        self.var_Attendance_ID.set("")
        self.var_Student_Name.set("")
        self.var_Branch.set("")
        self.var_Roll_No.set("")
        self.var_Date.set("")
        self.var_Time.set("")
        self.var_Status.set("")


        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()