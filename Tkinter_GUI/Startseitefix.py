from distutils.command import build
import imp
import tkinter
import customtkinter
from tkinter import *
from numpy import place
from referencing import Anchor
from screeninfo import get_monitors
from PIL import Image
import ctypes
import pywinstyles
from sympy import im


class Startpage:

    def __init__(self):
        app = customtkinter.CTk()

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        app.geometry("1280x720")
        app.title("Startpage")


        image = Image.open("Design/Background.png")                                  #Image initialitieren
        imagebg = customtkinter.CTkImage(image,size=(1280,720))

        bg_label = customtkinter.CTkLabel(app, text="", image=imagebg)                   #backgrund imagelabel
        bg_label.place(x=0,y=0)

        app.iconbitmap(default="Design/Icon.png")
        app.iconphoto(False, PhotoImage(master=app,file="Design/Icon.png"))              #Icon festlegen

        myappid = u'mycompany.myproduct.subproduct.version'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)          #Icon festlegen


        
        #settingsbutton
        settings = customtkinter.CTkButton(master=app,
                                                width=200,
                                                height=250,
                                                corner_radius=20,
                                                fg_color="#250454",
                                                bg_color="#000001",
                                                text="",
                                                hover_color="#250454",
                                                command=self.Settings
                                                )
        pywinstyles.set_opacity(settings,color="#000001")
        settings.place(x=250,y=370)

        image = Image.open("Tkinter_GUI/StartseiteIMG/settings.png")
        imagesettings = customtkinter.CTkImage(image,size=(100,100))

        settingslbl = customtkinter.CTkLabel(settings,text="",image=imagesettings)
        settingslbl.bind("<Button-1>",lambda e,:self.Settings())
        settingslbl.place(x=100,y=90,anchor=tkinter.CENTER)

        settingstxt = customtkinter.CTkLabel(settings, text="Settings",font=("Arial",25),text_color="#B886F8")
        settingstxt.place(x=100,y=180,anchor=tkinter.CENTER)
        settingstxt.bind("<Button-1>",lambda e, :self.Settings())




        #storebutton
        store = customtkinter.CTkButton(master=app,
                                        width=200,
                                        height=250,
                                        corner_radius=20,
                                        fg_color="#250454",
                                        bg_color="#000001",text="",
                                        hover_color="#250454",
                                        command=self.Store
                                            )
        pywinstyles.set_opacity(store, color="#000001")
        store.place(x=540,y=70)

        image = Image.open("Tkinter_GUI/StartseiteIMG/shopping-cart.png")
        imagestore = customtkinter.CTkImage(image,size=(100,100))

        storelbl = customtkinter.CTkLabel(store,text="",image=imagestore)
        storelbl.bind("<Button-1>",lambda e,:self.Store())
        storelbl.place(x=100,y=90,anchor=tkinter.CENTER)

        storetxt = customtkinter.CTkLabel(store, text="Store",font=("Arial",25),text_color="#B886F8")
        storetxt.place(x=100,y=180,anchor=tkinter.CENTER)
        storetxt.bind("<Button-1>",lambda e, :self.Store())







        app.mainloop()







    def Settings(self):
        print("Settings->")
    
    def Store(self):
        print("Store->")
    
    def Mygames(self):
        print("My games->")
    
    def Wishlist(self):
        print("Wishlist->")
    
    def Notes(self):
        print("Notes->")

    def Profile(self):
        print("profile->")