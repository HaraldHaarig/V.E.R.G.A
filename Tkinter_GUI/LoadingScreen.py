import customtkinter
from tkinter import *
from PIL import Image
import ctypes
import pywinstyles


class Loadingscreen():
    
    def __init__(self):
        app = customtkinter.CTk()

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        app.geometry("600x480")

        image = Image.open("Design/Background.png")                                  #Image initialitieren
        imagebg = customtkinter.CTkImage(image,size=(1280,720))

        bg_label = customtkinter.CTkLabel(app, text="", image=imagebg)                   #backgrund imagelabel
        bg_label.place(x=0,y=0)

        app.iconbitmap(default="Design/Icon.png")
        app.iconphoto(False, PhotoImage(master=app,file="Design/Icon.png"))              #Icon festlegen

        myappid = u'mycompany.myproduct.subproduct.version'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)          #Icon festlegen
 

        app.mainloop()