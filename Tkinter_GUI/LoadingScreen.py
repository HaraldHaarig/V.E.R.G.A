
import imp
from itertools import tee
import customtkinter
from tkinter import *
from PIL import Image
import ctypes
import pywinstyles
#from Tkinter_GUI.Startseite import Startpage



class Loadingscreen():
    
    def __init__(self):
        self.app = customtkinter.CTk()

        widh_of_window = 600
        height_of_window = 480
        scree_widh = self.app.winfo_screenwidth()
        screen_height = self.app.winfo_screenheight()
        x_cordinate = (scree_widh/2)-(widh_of_window/2)
        y_cordinate = (screen_height/2)-(height_of_window/2)
        self.app.geometry("%dx%d+%d+%d" %(widh_of_window,height_of_window,x_cordinate,y_cordinate))

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        

        image = Image.open("Design/Background.png")                                  #Image initialitieren
        imagebg = customtkinter.CTkImage(image,size=(1280,720))

        bg_label = customtkinter.CTkLabel(self.app, text="", image=imagebg)                   #backgrund imagelabel
        bg_label.place(x=0,y=0)

        self.app.iconbitmap(default="Design/Icon.png")
        self.app.iconphoto(False, PhotoImage(master=self.app,file="Design/Icon.png"))              #Icon festlegen

        myappid = u'mycompany.myproduct.subproduct.version'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)          #Icon festlegen

        
        self.app.mainloop()

    
    def abbruch(self):
        self.app.destroy()
        
        

    
        
