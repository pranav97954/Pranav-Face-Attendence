from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student

class Face_Recoginition_Systeam:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recoginition System")
        #Set Image
        #image 01
        #for open imagefile 
        img=Image.open(r"C:\Users\Pranav_PC\Desktop\project 01\college_images\Stanford.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        #For making label
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
         #image 02
        #for open imagefile 
        img2=Image.open(r"C:\Users\Pranav_PC\Desktop\project 01\college_images\facialrecognition.png")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        #For making label
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)
        #image 03
        #for open imagefile 
        img3=Image.open(r"C:\Users\Pranav_PC\Desktop\project 01\college_images\u.jpg")
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

        title_lbl=Label(bg_lbl,text="FACE RECOGINITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",28,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=40)
        
        #For Student Button
        #button 01
        #for open imagefile 
        img5=Image.open(r"C:\Users\Pranav_PC\Desktop\project 01\college_images\gettyimages-1022573162.jpg")
        img5=img5.resize((220,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_lbl,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=70,width=220,height=200)
        #for adding text in button
        b1_1=Button(bg_lbl,text="Student Details",cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="green")
        b1_1.place(x=100,y=240,width=220,height=40)
        
        #For DectFace Button
        #button 2
        #for open imagefile 
        img6=Image.open(r"C:\Users\Pranav_PC\Desktop\project 01\college_images\face_detector1.jpg")
        img6=img6.resize((220,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b2=Button(bg_lbl,image=self.photoimg6,cursor="hand2")
        b2.place(x=360,y=70,width=220,height=200)
        #for adding text in button
        b2_2=Button(bg_lbl,text="Face Recognition",cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="green")
        b2_2.place(x=360,y=240,width=220,height=40)

        #For Attendance Button
        #button 3
        #for open imagefile 
        img7=Image.open(r"C:\Users\Pranav_PC\Desktop\project 01\college_images\report.jpg")
        img7=img7.resize((220,200),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b3=Button(bg_lbl,image=self.photoimg7,cursor="hand2")
        b3.place(x=620,y=70,width=220,height=200)
        #for adding text in button
        b3_3=Button(bg_lbl,text="Attendance",cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="green")
        b3_3.place(x=620,y=240,width=220,height=40)

        #For DectFace Button
        #button 4
        #for open imagefile 
        img8=Image.open(r"C:\Users\Pranav_PC\Desktop\project 01\college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img8=img8.resize((220,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b4=Button(bg_lbl,image=self.photoimg8,cursor="hand2")
        b4.place(x=870,y=70,width=220,height=200)
        #for adding text in button
        b4_4=Button(bg_lbl,text="Help Desk",cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="green")
        b4_4.place(x=870,y=240,width=220,height=40)

        #For Student Button
        #button 05
        #for open imagefile 
        img9=Image.open(r"C:\Users\Pranav_PC\Desktop\project 01\college_images\Train.jpg")
        img9=img9.resize((220,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b5=Button(bg_lbl,image=self.photoimg9,cursor="hand2")
        b5.place(x=100,y=300,width=220,height=200)
        #for adding text in button
        b5_5=Button(bg_lbl,text="Train Data",cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="green")
        b5_5.place(x=100,y=460,width=220,height=40)
        #button 06
        #for open imagefile 
        img10=Image.open(r"C:\Users\Pranav_PC\Desktop\project 01\college_images\opencv_face_reco_more_data.jpg")
        img10=img10.resize((220,200),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b6=Button(bg_lbl,image=self.photoimg10,cursor="hand2")
        b6.place(x=360,y=300,width=220,height=200)
        #for adding text in button
        b6_6=Button(bg_lbl,text="Photo",cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="green")
        b6_6.place(x=360,y=460,width=220,height=40)
        #button 07
        #for open imagefile 
        img11=Image.open(r"C:\Users\Pranav_PC\Desktop\project 01\college_images\Team-Management-Software-Development.jpg")
        img11=img11.resize((220,200),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b7=Button(bg_lbl,image=self.photoimg11,cursor="hand2")
        b7.place(x=620,y=300,width=220,height=200)
        #for adding text in button
        b7_7=Button(bg_lbl,text="Developer",cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="green")
        b7_7.place(x=620,y=460,width=220,height=40)
        #button 08
        #for open imagefile 
        img12=Image.open(r"C:\Users\Pranav_PC\Desktop\project 01\college_images\exit.jpg")
        img12=img12.resize((220,200),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)
        
        b8=Button(bg_lbl,image=self.photoimg12,cursor="hand2")
        b8.place(x=870,y=300,width=220,height=200)
        #for adding text in button
        b8_8=Button(bg_lbl,text="Exit",cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="green")
        b8_8.place(x=870,y=460,width=220,height=40)
    #-----------Function Button------------#
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recoginition_Systeam(root)
    root.mainloop() 
