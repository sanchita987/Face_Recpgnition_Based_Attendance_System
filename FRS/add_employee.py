import tkinter as tk
from tkinter import Button, Label, LabelFrame, Frame, RIDGE, Radiobutton, Text, ttk
from tkinter import Entry
from PIL import Image, ImageTk
from constants import Constants

class AddEmployee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x900+0+0")
        self.root.minsize(1440, 900)
        self.root.maxsize(1440,900)
        
        #Background Image
        img = Image.open("C:\\Users\\ASUS\\Downloads\\FRS\\FRS\\Images\\splash-bg.png")
        img=img.resize((1280,900), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img= Label(self.root, image=self.photoimg)
        bg_img.place(x=150,y=0, width=1280,height=900)

        #left Frame
        left_frame = LabelFrame(bg_img,bd=10,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,text="Add Employee",relief=RIDGE, font=("times new roman", 18 ))
        left_frame.place(x=45, y=20, width=1227, height=400)

        # instance of shared
        from shared import Shared
        self.shared = Shared(self.root)

        # Full Name
        name_label = Label(left_frame, text="Full Name", font=(Constants.Add_Employee_font, 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        name_label.grid(row=0, column=0, padx=10, pady=15)

        name_entry = Text(left_frame, font=(Constants.Add_Employee_font , 15 ), width=22,height=1,insertbackground="black" ,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,borderwidth=0,highlightbackground="grey",highlightthickness=2 )
        name_entry.grid(row=0, column=1, padx=10, pady=15)

        # Address
        address_label = Label(left_frame, text="Address", font=(Constants.Add_Employee_font, 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        address_label.grid(row=0, column=2, padx=10, pady=15)

        address_entry = Text(left_frame, font=(Constants.Add_Employee_font , 15 ), width=22,height=1,insertbackground="black" ,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,borderwidth=0,highlightbackground="grey",highlightthickness=2 )
        address_entry.grid(row=0, column=3, padx=10, pady=15, sticky=tk.W)

        # Phone Number
        phone_label = Label(left_frame, text="Phone Number", font=(Constants.Add_Employee_font ,15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        phone_label.grid(row=0, column=4, padx=10, pady=15)

        phone_entry = Text(left_frame, font=(Constants.Add_Employee_font , 15 ), width=22,height=1,insertbackground="black" ,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,borderwidth=0,highlightbackground="grey",highlightthickness=2 )
        phone_entry.grid(row=0, column=5, padx=10, pady=15, sticky=tk.W)

        # Email Address
        email_label = Label(left_frame, text="Email Address", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        email_label.grid(row=1, column=0, padx=10, pady=15)

        email_entry = Text(left_frame, font=(Constants.Add_Employee_font , 15 ), width=22,height=1,insertbackground="black" ,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,borderwidth=0,highlightbackground="grey",highlightthickness=2 )
        email_entry.grid(row=1, column=1, padx=10, pady=15, sticky=tk.W)

        # Gender
        gender_label = Label(left_frame, text="Gender", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        gender_label.grid(row=1, column=2, padx=10, pady=15)
        gender_combo = ttk.Combobox(left_frame, font=(Constants.Add_Employee_font , 12, "bold"), width=28, state="readonly")
        gender_combo["values"] = ( "Male", "Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=3, padx=2, pady=15, sticky=tk.W)
        

        # Joined Date
        joined_label = Label(left_frame, text="Joined Date", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        joined_label.grid(row=1, column=4, padx=10, pady=15)

        joined_entry = Text(left_frame, font=(Constants.Add_Employee_font , 15 ), width=22,height=1,insertbackground="black" ,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,borderwidth=0,highlightbackground="grey",highlightthickness=2 )
        joined_entry.grid(row=1, column=5, padx=10, pady=15, sticky=tk.W)

        # Department
        dep_label = Label(left_frame, text="Department", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        dep_label.grid(row=2, column=0, padx=2, pady=15)

        dep_combo = ttk.Combobox(left_frame, font=(Constants.Add_Employee_font ,12, "bold"), width=28, state="readonly")
        dep_combo["values"] = ("select Department", "HR", "IT", "Finance", "Marketing", "Operations")
        dep_combo.current(0)
        dep_combo.grid(row=2, column=1, padx=2, pady=15, sticky=tk.W)

        # Salary
        salary_label = Label(left_frame, text="Salary", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        salary_label.grid(row=2, column=2, padx=10, pady=15)

        salary_entry = Text(left_frame, font=(Constants.Add_Employee_font , 15 ), width=22,height=1,insertbackground="black",bg=Constants.content_background_color,fg=Constants.frame_content_text_color,borderwidth=0,highlightbackground="grey",highlightthickness=2 )
        salary_entry.grid(row=2, column=3, padx=10, pady=15, sticky=tk.W)

        # Emergency Contacts
        emergency_label = Label(left_frame, text="Emergency Contacts", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        emergency_label.grid(row=2, column=4, padx=10, pady=15)

        emergency_entry = Text(left_frame, font=(Constants.Add_Employee_font , 15 ), width=22,height=1,insertbackground="black" ,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,borderwidth=0,highlightbackground="grey",highlightthickness=2 )
        emergency_entry.grid(row=2, column=5, padx=10, pady=15, sticky=tk.W)

        # Educational Background
        education_label = Label(left_frame, text="Educational Background", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        education_label.grid(row=9, column=0, padx=10, pady=15)

        education_entry = Text(left_frame, font=(Constants.Add_Employee_font , 15 ), width=22,height=1,insertbackground="black" ,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,borderwidth=0,highlightbackground="grey",highlightthickness=2 )
        education_entry.grid(row=9, column=1, padx=10, pady=15, sticky=tk.W)

        #radio_buttons1
        radiobtn1=Radiobutton(left_frame,text="Take Photos", font=(Constants.Add_Employee_font ,15),value="yes",bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        radiobtn1.grid(row=10,column=0)

        #radio_buttons1
        radiobtn2=Radiobutton(left_frame,text="No Photos",font=(Constants.Add_Employee_font ,15), value="yes",bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        radiobtn2.grid(row=10,column=1)


        #button_frame
        btn_frame = Frame(left_frame,bg=Constants.content_background_color)
        btn_frame.place(x=40, y=270, width=1200, height=50)

        #save_button
        save_btn=Button(btn_frame, text="Save",font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        save_btn.grid(row=0,column=1)

        #WhiteSpace_between_buttons
        white_space=Label(btn_frame,bg=Constants.content_background_color, width=3)
        white_space.grid(row=0,column=2)

        #update_button
        update_btn=Button(btn_frame, text="Update",font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        update_btn.grid(row=0,column=3)

        #WhiteSpace_between_buttons
        white_space=Label(btn_frame,bg=Constants.content_background_color, width=3)
        white_space.grid(row=0,column=4)

        #delete_btn
        delete_btn=Button(btn_frame, text="Delete",font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        delete_btn.grid(row=0,column=5)

        #WhiteSpace_between_buttons
        white_space=Label(btn_frame,bg=Constants.content_background_color, width=3)
        white_space.grid(row=0,column=6)

        #update_button
        reset_btn=Button(btn_frame, text="Reset",font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        reset_btn.grid(row=0,column=7)

        #WhiteSpace_between_buttons
        white_space=Label(btn_frame,bg=Constants.content_background_color, width=3)
        white_space.grid(row=0,column=8)

         #delete_btn
        delete_btn=Button(btn_frame, text="Take Photo Samples",font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        delete_btn.grid(row=0,column=9)

        #WhiteSpace_between_buttons
        white_space=Label(btn_frame,bg=Constants.content_background_color, width=3)
        white_space.grid(row=0,column=10)

        #update_button
        reset_btn=Button(btn_frame, text="Update Photo Samples",font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        reset_btn.grid(row=0,column=11)


        #Right Frame
        right_frame = LabelFrame(bg_img,bd=10,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,text="Employee Details",relief=RIDGE, font=("times new roman", 18 ))
        right_frame.place(x=45, y=440, width=1227, height=400)

        
        

      


if __name__ == "__main__":
    root = tk.Tk()
    AddEmployee_obj = AddEmployee(root)
    root.mainloop()