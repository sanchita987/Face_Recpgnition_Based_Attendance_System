import os

print("Current Working Directory:", os.getcwd())
import threading
from tkinter import *
import tkinter

from PIL import Image, ImageTk
import imageio
from tkvideo import tkvideo

from constants import Constants


class Face_Recognition_Attendance_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x900+0+0")
        self.root.minsize(1440,900)
        self.root.title("Face Recognition system")
        self.root.configure(bg="white")

        # Create an instance of the Shared class
        from shared import Shared
        self.shared_instance_main = Shared(self.root)

        home_img=Image.open("C:\\Users\\ASUS\\Downloads\\FRS\\FRS\\Images\\aceecognitionpps163973557648.png")
        home_img=home_img.resize((1280, 900))

        self.home_img=ImageTk.PhotoImage(home_img)

        home_img_label=Label(image=self.home_img)
        home_img_label.place(x=190,y=0)
        
        

if __name__ == "__main__":
    root = Tk()
    main_obj = Face_Recognition_Attendance_System(root)
    root.mainloop()
