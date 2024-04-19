from customtkinter import* 
#from tkinter import*
import tkinter as tk
from PIL import Image
from ctypes import windll
import ctypes

class Bibliothek:

    def __init__(self):
        self.root_tk = CTk()
        user32 = ctypes.windll.user32
        screenwidth = user32.GetSystemMetrics(0)
        screenheight=user32.GetSystemMetrics(1)
        
        x = int(((screenwidth/40)))
        y = int(((screenheight/40)))

        self.root_tk.geometry("%dx%d+%d+%d" % (int(screenwidth),int(screenheight),int(x),int(y)))
        
        self.root_tk.title("Bibliothek")

        #Pictures
        leftside_img_data = Image.open("Tkinter_GUI/Images/Background_frfr.png")
        background_img_data = Image.open("Tkinter_GUI/Images/Background_frfr.png")
        #hier weiter machen

        #Right side of the libary
        self.mainframe= CTkFrame(self.root_tk, width=screenwidth,height=screenheight, fg_color="#222234") 
        #self.mainframe.pack()
        self.mainframe.place(anchor=tk.E, relx=1.0,rely=0.5)

        #Left side of the library
        self.leftframe= CTkFrame(self.root_tk, width=screenwidth-1620,height=screenheight, fg_color="#ffffff") 
        #self.leftframe.pack()
        self.leftframe.place(anchor=tk.W, relx=0.0,rely=0.5)

        CTkLabel(master=self.leftframe, text="", image=side_img).pack(expand=True, side="left")

        self.root_tk.mainloop()
        # app = CTk()
        # app.geometry("1280x720")
        # app.resizable(0,0)

        # background = Image.open("Tkinter_GUI/Images/Background_frfr.png")
        # backgroundData = CTkImage(dark_image=background, light_image=background, size=(1280, 720))

        # CTkLabel(master=app, text="", image=backgroundData).pack(expand=True, side="left")

        # app.mainloop()
