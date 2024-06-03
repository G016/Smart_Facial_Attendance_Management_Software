    def Update_data(self):
        if self.var_Branch.get() == "Select Branch" or self.var_Session.get() == "" or self.var_Year.get() == "Select Year" or self.var_Semester.get() == "Select Semester" or self.var_Student_Name.get() == "" or self.var_Roll_No.get() == "" or self.var_Gender.get() == "Select Gender" or self.var_DOB.get() == "" or self.var_Email.get() == "" or self.var_Mobile_No.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Gaurav@716", database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("Update Student set Branch=%s, Session=%s, Year=%s, Semester=%s, Student_Name=%s, Roll_No=%s, Gender=%s, DOB=%s, Email=%s, Mobile_No=%s, Photo_Sample_Status=%s WHERE Student_id=%s", (
                    self.var_Branch.get(),
                    self.var_Session.get(),
                    self.var_Year.get(),
                    self.var_Semester.get(),
                    self.var_Student_Name.get(),
                    self.var_Roll_No.get(),
                    self.var_Gender.get(),
                    self.var_DOB.get(),
                    self.var_Email.get(),
                    self.var_Mobile_No.get(),
                    self.var_Photo_Sample_Status.get(),
                    self.var_Rbtn1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details updated successfully")
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}")