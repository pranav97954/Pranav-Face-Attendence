from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recoginition System")
        
        #-----------Variables---------
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()        
        
        #Set Image
        #image 01
        #for open imagefile 
        img=Image.open(r"C:\Users\Pranav_PC\Desktop\project 01\college_images\face-recognition.png")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        #For making label
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
         #image 02
        #for open imagefile 
        img2=Image.open(r"C:\Users\Pranav_PC\Desktop\project 01\college_images\smart-attendance.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        #For making label
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)
        #image 03
        #for open imagefile 
        img3=Image.open(r"C:\Users\Pranav_PC\Desktop\project 01\college_images\iStock-182059956_18390_t12.jpg")
        img3=img3.resize((500,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        #For making label
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        #For Background image
        #for open imagefile 
        img4=Image.open(r"C:\Users\Pranav_PC\Desktop\project 01\college_images\wp2551980.jpg")
        img4=img4.resize((1400,700),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        #For making label
        bg_lbl=Label(self.root,image=self.photoimg4)
        bg_lbl.place(x=0,y=130,width=1400,height=700)

        title_lbl=Label(bg_lbl,text="STUDENT MANAGEMENT SYSTEAM",font=("times new roman",28,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1400,height=40)
        
        #For making Frame
        main_frame=Frame(bg_lbl,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1200,height=450)

        #Left label Frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=30,y=10,width=500,height=400)
        #For setting image in Left label Frame
        #for open imagefile 
        img12=Image.open(r"C:\Users\Pranav_PC\Desktop\project 01\college_images\AdobeStock_303989091.jpeg")
        img12=img12.resize((495,60),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)
        #For making label
        f_lbl=Label(Left_frame,image=self.photoimg12)
        f_lbl.place(x=1,y=0,width=495,height=60)
        #Current course information
        Current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        Current_course_frame.place(x=1,y=60,width=495,height=80)
        
        #Department
        dep_label=Label(Current_course_frame,text="Deprtment",bg="white",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=5)
        #Department combo Box
        dep_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanicial","Electronic")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,sticky=W)

        #Course
        course_label=Label(Current_course_frame,text="Courses",bg="white",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column=2,padx=5)
        #Department combo Box
        courses_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        courses_combo["values"]=("Select Courses","FE","SE","TE","BE")
        courses_combo.current(0)
        courses_combo.grid(row=0,column=3,padx=2,sticky=W)

        #Year
        year_label=Label(Current_course_frame,text="Year",bg="white",font=("times new roman",12,"bold"))
        year_label.grid(row=1,column=0,padx=5)
        #Department combo Box
        year_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Select year","2022-23","2021-22","2020-21","2019-20")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,sticky=W)

        #Semester
        semester_label=Label(Current_course_frame,text="Semester",bg="white",font=("times new roman",12,"bold"))
        semester_label.grid(row=1,column=2,padx=5)
        #Department combo Box
        semester_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","sem1","sem2","sem3","sem4","sem5","sem6","sem7","sem8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,sticky=W)
        
        #Class student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=1,y=145,width=495,height=230)
        #student id
        studentid_label=Label(class_student_frame,text="StudentID:",bg="white",font=("times new roman",12,"bold"))
        studentid_label.grid(row=0,column=0,padx=5)

        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=15,font=("times new roman",12,"bold"))
        studentid_entry.grid(row=0,column=1,padx=5,sticky=W)
        #student Name
        studentname_label=Label(class_student_frame,text="StudentName:",bg="white",font=("times new roman",12,"bold"))
        studentname_label.grid(row=1,column=0,padx=5)

        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=15,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=1,column=1,padx=5,sticky=W)
        #class division
        class_div_label=Label(class_student_frame,text="Class Division:",bg="white",font=("times new roman",12,"bold"))
        class_div_label.grid(row=0,column=2,padx=5)

        class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        class_div_entry.grid(row=0,column=3,padx=5,sticky=W)
        #roll no
        roll_no_label=Label(class_student_frame,text="Roll No:",bg="white",font=("times new roman",12,"bold"))
        roll_no_label.grid(row=2,column=0,padx=5)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=15,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=2,column=1,padx=5,sticky=W)
        #Gender
        gender_label=Label(class_student_frame,text="Gender:",bg="white",font=("times new roman",12,"bold"))
        gender_label.grid(row=1,column=2,padx=5)

        gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=15,font=("times new roman",12,"bold"))
        gender_entry.grid(row=1,column=3,padx=5,sticky=W)
        #email
        email_label=Label(class_student_frame,text="Email:",bg="white",font=("times new roman",12,"bold"))
        email_label.grid(row=2,column=2,padx=5)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=15,font=("times new roman",12,"bold"))
        email_entry.grid(row=2,column=3,padx=5,sticky=W)
        #Phone Number
        phonenumber_label=Label(class_student_frame,text="Phone Number:",bg="white",font=("times new roman",12,"bold"))
        phonenumber_label.grid(row=3,column=0,padx=5)

        phonenumber_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=15,font=("times new roman",12,"bold"))
        phonenumber_entry.grid(row=3,column=1,padx=5,sticky=W)
        #Teacher Name
        teachername_label=Label(class_student_frame,text="Teacher Name:",bg="white",font=("times new roman",12,"bold"))
        teachername_label.grid(row=4,column=2,padx=5)

        teachername_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=15,font=("times new roman",12,"bold"))
        teachername_entry.grid(row=4,column=3,padx=5,sticky=W)
        #address
        address_label=Label(class_student_frame,text="Address:",bg="white",font=("times new roman",12,"bold"))
        address_label.grid(row=4,column=0,padx=5)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=15,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=5,sticky=W)
        #DOB
        DOB_label=Label(class_student_frame,text="DOB:",bg="white",font=("times new roman",12,"bold"))
        DOB_label.grid(row=3,column=2,padx=5)

        DOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=15,font=("times new roman",12,"bold"))
        DOB_entry.grid(row=3,column=3,padx=5,sticky=W)

        #Radio Button
        self.var_radio1=StringVar()
        radiobutn1=ttk.Radiobutton(class_student_frame,text="Take Photo Sample",textvariable=self.var_radio1,value="Yes")
        radiobutn1.grid(row=5,column=0)

        self.var_radio2=StringVar()
        radiobutn2=ttk.Radiobutton(class_student_frame,text="No Photo Sample",textvariable=self.var_radio2,value="No")
        radiobutn2.grid(row=5,column=1)
        
        #Button Frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=150,width=490,height=60)
        #save
        save_btn=Button(btn_frame,width=13,text="Save",font=("times new roman",11,"bold"),bg="blue")
        save_btn.grid(row=0,column=0)
        #Update
        update_btn=Button(btn_frame,width=13,text="Update",font=("times new roman",11,"bold"),bg="blue")
        update_btn.grid(row=0,column=1)
        #Delete
        delete_btn=Button(btn_frame,width=12,text="Delete",font=("times new roman",11,"bold"),bg="blue")
        delete_btn.grid(row=0,column=2)
        #Reset
        reset_btn=Button(btn_frame,width=12,text="Reset",font=("times new roman",11,"bold"),bg="blue")
        reset_btn.grid(row=0,column=3)
        
        btn_frame1=Frame(btn_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=28,width=490,height=60)
        #Take Photo
        take_photo_btn=Button(btn_frame1,width=26,text="Take Photo",font=("times new roman",11,"bold"),bg="blue")
        take_photo_btn.grid(row=1,column=0)
        #update Photo
        update_photo_btn=Button(btn_frame1,width=26,text="Update Photo",font=("times new roman",11,"bold"),bg="blue")
        update_photo_btn.grid(row=1,column=1)
        

        #Right label Frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=570,y=10,width=600,height=400)
        #for open imagefile 
        img13=Image.open(r"C:\Users\Pranav_PC\Desktop\project 01\college_images\20191204_095506.jpg")
        img13=img13.resize((590,60),Image.ANTIALIAS)
        self.photoimg13=ImageTk.PhotoImage(img13)
        #For making label
        r_lbl=Label(Right_frame,image=self.photoimg13)
        r_lbl.place(x=1,y=0,width=590,height=60)
        #search Systeam
        search_systeam_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search systeam",font=("times new roman",12,"bold"))
        search_systeam_frame.place(x=1,y=60,width=590,height=80)
        #Search
        search_label=Label(search_systeam_frame,text="Search By:",bg="red",font=("times new roman",15,"bold"))
        search_label.grid(row=0,column=0,padx=5)

        search_combo=ttk.Combobox(search_systeam_frame,font=("times new roman",12,"bold"),state="readonly")
        search_combo["values"]=("Select ","Roll no","Phone Number","Student ID")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,sticky=W)
        
        search_entry=ttk.Entry(search_systeam_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,sticky=W)
        #search btn
        search_btn=Button(search_systeam_frame,width=12,text="Search",font=("times new roman",11,"bold"),bg="blue")
        search_btn.grid(row=1,column=1)
        #Show All
        showall_btn=Button(search_systeam_frame,width=12,text="Show All",font=("times new roman",11,"bold"),bg="blue")
        showall_btn.grid(row=1,column=2)
        #Show Table frame
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=1,y=140,width=590,height=200)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student Id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Div")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
               
        self.student_table.pack(fill=BOTH,expand=1)

    #-------------Function Declaration------------
    def add_data(self):
        pass







if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()