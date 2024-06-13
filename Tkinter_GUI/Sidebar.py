import tkinter
from turtle import bgcolor
from customtkinter import *
from PIL import Image
from matplotlib.backend_bases import cursors
from numpy import imag, size
from pyparsing import col
import pywinstyles
from sympy import true
from Tkinter_GUI.Login import Login

class Sidebar:
    def __init__(self, app,login:Login):
        
        # Images
        image_home = CTkImage(Image.open("Tkinter_GUI/StartseiteIMG/home.png"), size=(30, 30))
        image_geschenk = CTkImage(Image.open("Tkinter_GUI/StartseiteIMG/geschenk.png"), size=(30, 30))
        image_joystick = CTkImage(Image.open("Tkinter_GUI/StartseiteIMG/joystick.png"), size=(30, 30))
        image_notes = CTkImage(Image.open("Tkinter_GUI/StartseiteIMG/notes.png"), size=(30, 30))
        image_shoppingcart = CTkImage(Image.open("Tkinter_GUI/StartseiteIMG/shopping-cart.png"), size=(30, 30))
        image_user = CTkImage(Image.open("Tkinter_GUI/StartseiteIMG/user.png"), size=(30, 30))
        image_icon = CTkImage(Image.open("./Design/LogoNEW2.png"), size=(100, 124))
        
        # Sidebar Frame
        self.sidebar = CTkFrame(master=app,
                                width=300,
                                height=720,
                                fg_color="#250454",
                                bg_color="#000001")
        pywinstyles.set_opacity(self.sidebar, color="#000001")
        self.sidebar.place(x=0, y=0)

        # Das Logo ganz oben in der Sidebar
        self.icon = CTkLabel(master=self.sidebar,
                             text="",
                             image=image_icon)
        self.icon.place(x=150, y=100, anchor=tkinter.CENTER)

        # Home Button
        self.home_btn = CTkButton(master=self.sidebar,
                                  image=image_home,
                                  text="Home",
                                  width=100,
                                  height=60,
                                  fg_color="#000001",
                                  cursor="hand2",
                                  font=("Arial", 35))
        self.home_btn.bind("<Button-1>", lambda e,:openHome())
        pywinstyles.set_opacity(self.home_btn, color="#000001")
        self.home_btn.place(x=150, y=220, anchor=tkinter.CENTER)

        # Profile Button
        self.profile_btn = CTkButton(master=self.sidebar,
                                     image=image_user,
                                     text="Profile",
                                     width=100,
                                     height=60,
                                     fg_color="#000001",
                                     cursor="hand2",
                                     font=("Arial", 35))
        self.profile_btn.bind("<Button-1>", lambda e,:openProfile())
        self.profile_btn.bind("<Button-1>", lambda e,:openProfile())
        pywinstyles.set_opacity(self.profile_btn, color="#000001")
        self.profile_btn.place(x=150, y=310, anchor=tkinter.CENTER)

        # Store Button
        self.store_btn = CTkButton(master=self.sidebar,
                                   image=image_shoppingcart,
                                   text="Store",
                                   width=100,
                                   height=60,
                                   fg_color="#000001",
                                   cursor="hand2",
                                   font=("Arial", 35))
        self.store_btn.bind("<Button-1>", lambda e,:openStore())
        pywinstyles.set_opacity(self.store_btn, color="#000001")
        self.store_btn.place(x=150, y=400, anchor=tkinter.CENTER)

        # My Games Button
        self.mygames_btn = CTkButton(master=self.sidebar,
                                     image=image_joystick,
                                     text="My Games",
                                     width=100,
                                     height=60,
                                     fg_color="#000001",
                                     cursor="hand2",
                                     font=("Arial", 35))
        self.mygames_btn.bind("<Button-1>", lambda e,:openMyGames())
        pywinstyles.set_opacity(self.mygames_btn, color="#000001")
        self.mygames_btn.place(x=150, y=490, anchor=tkinter.CENTER)

        # Wishlist Button
        self.wishlist_btn = CTkButton(master=self.sidebar,
                                      image=image_geschenk,
                                      text="Wishlist",
                                      width=100,
                                      height=60,
                                      fg_color="#000001",
                                      cursor="hand2",
                                      font=("Arial", 35))
        self.wishlist_btn.bind("<Button-1>", lambda e,:openHome())
        pywinstyles.set_opacity(self.wishlist_btn, color="#000001")
        self.wishlist_btn.place(x=150, y=580, anchor=tkinter.CENTER)

        # Notes Button
        self.notes_btn = CTkButton(master=self.sidebar,
                                   image=image_notes,
                                   text="Notes",
                                   width=100,
                                   height=60,
                                   fg_color="#000001",
                                   cursor="hand2",
                                   font=("Arial", 35))
        self.notes_btn.bind("<Button-1>", lambda e,:openNotes())
        pywinstyles.set_opacity(self.notes_btn, color="#000001")
        self.notes_btn.place(x=150, y=670, anchor=tkinter.CENTER)

        #Each function for each button

        def openHome():
            from Tkinter_GUI.Startseite import Startpage
            app.destroy()
            startpage = Startpage()

        def openProfile():
            from Tkinter_GUI.Profil import Profil
            app.destroy()
            profil = Profil()

        def openStore():
            from Tkinter_GUI.Bibliothek import Bibliothek
            app.destroy()
            bibliothek = Bibliothek()

        def openMyGames():
            from Tkinter_GUI.Bibliothek import Bibliothek
            app.destroy()
            home = Startpage(login)
        
        def openNotes():
            from Tkinter_GUI.Notes import Notes # Pfusch 4
            app.destroy()
            notes = Notes(login)

        def openProfile():
            from Tkinter_GUI.Profil import Profil # Pfusch 5
            app.destroy()
            profile = Profil(login)
