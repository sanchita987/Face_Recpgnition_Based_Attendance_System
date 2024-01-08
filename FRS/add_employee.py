import tkinter as tk
from tkinter import Label, LabelFrame, Frame, RIDGE, ttk
from tkinter import Entry, Radiobutton, IntVar


class AddEmployee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x900+0+0")
        main_Frame = Frame(root, bd=2)
        main_Frame.place(x=140, y=0, width=2000, height=1000)
        left_frame = LabelFrame(main_Frame, bd=2, bg="white", relief=RIDGE, text="Employee Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=50, y=5, width=1060, height=900)
        

        # instance of shared
        from shared import Shared
        self.shared = Shared(self.root)

        # Full Name
        name_label = Label(left_frame, text="Full Name", font=("times new roman", 12, "bold"))
        name_label.grid(row=0, column=0, padx=10, pady=15)

        name_entry = Entry(left_frame, font=("times New roman", 12, "bold"), width=17)
        name_entry.grid(row=0, column=1, padx=10, pady=15, sticky=tk.W)

        # Address
        address_label = Label(left_frame, text="Address", font=("times new roman", 12, "bold"))
        address_label.grid(row=1, column=0, padx=10, pady=15)

        address_entry = Entry(left_frame, font=("times New roman", 12, "bold"), width=17)
        address_entry.grid(row=1, column=1, padx=10, pady=15, sticky=tk.W)

        # Phone Number
        phone_label = Label(left_frame, text="Phone Number", font=("times new roman", 12, "bold"))
        phone_label.grid(row=2, column=0, padx=10, pady=15)

        phone_entry = Entry(left_frame, font=("times New roman", 12, "bold"), width=17)
        phone_entry.grid(row=2, column=1, padx=10, pady=15, sticky=tk.W)

        # Email Address
        email_label = Label(left_frame, text="Email Address", font=("times new roman", 12, "bold"))
        email_label.grid(row=3, column=0, padx=10, pady=15)

        email_entry = Entry(left_frame, font=("times New roman", 12, "bold"), width=17)
        email_entry.grid(row=3, column=1, padx=10, pady=15, sticky=tk.W)

        # Gender
        gender_label = Label(left_frame, text="Gender", font=("times new roman", 12, "bold"))
        gender_label.grid(row=4, column=0, padx=10, pady=15)

        gender_combo = ttk.Combobox(left_frame, font=("times new roman", 12, "bold"), width=17)
        gender_combo["values"] = ("select Gender", "Male", "Female")
        gender_combo.current(0)
        gender_combo.grid(row=4, column=1, padx=2, pady=15, sticky=tk.W)

        # Joined Date
        joined_label = Label(left_frame, text="Joined Date", font=("times new roman", 12, "bold"))
        joined_label.grid(row=5, column=0, padx=10, pady=15)

        joined_entry = Entry(left_frame, font=("times New roman", 12, "bold"), width=17)
        joined_entry.grid(row=5, column=1, padx=10, pady=15, sticky=tk.W)

        # Department
        dep_label = Label(left_frame, text="Department", font=("times new roman", 12, "bold"))
        dep_label.grid(row=6, column=0, padx=2, pady=15)

        dep_combo = ttk.Combobox(left_frame, font=("times new roman", 12, "bold"), width=17)
        dep_combo["values"] = ("select Department", "HR", "IT", "Finance", "Marketing", "Operations")
        dep_combo.current(0)
        dep_combo.grid(row=6, column=1, padx=2, pady=15, sticky=tk.W)

        # Salary
        salary_label = Label(left_frame, text="Salary", font=("times new roman", 12, "bold"))
        salary_label.grid(row=7, column=0, padx=10, pady=15)

        salary_entry = Entry(left_frame, font=("times New roman", 12, "bold"), width=17)
        salary_entry.grid(row=7, column=1, padx=10, pady=15, sticky=tk.W)

        # Emergency Contacts
        emergency_label = Label(left_frame, text="Emergency Contacts", font=("times new roman", 12, "bold"))
        emergency_label.grid(row=8, column=0, padx=10, pady=15)

        emergency_entry = Entry(left_frame, font=("times New roman", 12, "bold"), width=17)
        emergency_entry.grid(row=8, column=1, padx=10, pady=15, sticky=tk.W)

        # Educational Background
        education_label = Label(left_frame, text="Educational Background", font=("times new roman", 12, "bold"))
        education_label.grid(row=9, column=0, padx=10, pady=15)

        education_entry = Entry(left_frame, font=("times New roman", 12, "bold"), width=17)
        education_entry.grid(row=9, column=1, padx=10, pady=15, sticky=tk.W)

        # Work History
        work_history_label = Label(left_frame, text="Work History", font=("times new roman", 12, "bold"))
        work_history_label.grid(row=10, column=0, padx=10, pady=15)

        work_history_entry = Entry(left_frame, font=("times New roman", 12, "bold"), width=17)
        work_history_entry.grid(row=10, column=1, padx=10, pady=15, sticky=tk.W)
       # Take Photo Sample Radio Button
        take_photo_var = IntVar()
        take_photo_button = Radiobutton(left_frame, text="Take Photo Sample", variable=take_photo_var, value=1, font=("times new roman", 12, "bold"))
        take_photo_button.grid(row=11, column=0, padx=10, pady=15, sticky=tk.W)

        # No Photo Sample Radio Button
        no_photo_var = IntVar()
        no_photo_button = Radiobutton(left_frame, text="No Photo Sample", variable=no_photo_var, value=2, font=("times new roman", 12, "bold"))
        no_photo_button.grid(row=11, column=1, padx=10, pady=15, sticky=tk.W)

if __name__ == "__main__":
    root = tk.Tk()
    AddEmployee_obj = AddEmployee(root)
    root.mainloop()

       