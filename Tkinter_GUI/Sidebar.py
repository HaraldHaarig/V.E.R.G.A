import tkinter
from customtkinter import *
from PIL import Image
from numpy import size
import pywinstyles

class Sidebar:
    def __init__(self, app):
        image_geschenk = CTkImage(Image.open("Tkinter_GUI/StartseiteIMG/geschenk.png"), size=(30, 30))
        image_joystick = CTkImage(Image.open("Tkinter_GUI/StartseiteIMG/joystick.png"), size=(30, 30))
        image_notes = CTkImage(Image.open("Tkinter_GUI/StartseiteIMG/notes.png"), size=(30, 30))
        image_shoppingcart = CTkImage(Image.open("Tkinter_GUI/StartseiteIMG/shopping-cart.png"), size=(30, 30))
        image_user = CTkImage(Image.open("Tkinter_GUI/StartseiteIMG/user.png"), size=(30, 30))
        image_icon = CTkImage(Image.open("./Design/LogoNEW2.png"), size=(100, 124))

        self.sidebar = CTkFrame(master=app,
                                width=300,
                                height=720,
                                fg_color="#250454",
                                bg_color="#000001")
        pywinstyles.set_opacity(self.sidebar, color="#000001")
        self.sidebar.place(x=0, y=0)

        self.icon = CTkLabel(master=self.sidebar,
                             text="",
                             image=image_icon)
        self.icon.place(x=150, y=100, anchor=tkinter.CENTER)

        self.store_btn = CTkButton(master=self.sidebar,
                                   image=image_shoppingcart,
                                   text="Store",
                                   width=100,
                                   height=60,
                                   fg_color="#000001",
                                   cursor="hand2",
                                   font=("Arial", 35))
        pywinstyles.set_opacity(self.store_btn, color="#000001")
        self.store_btn.place(x=150, y=220, anchor=tkinter.CENTER)

        self.mygames_btn = CTkButton(master=self.sidebar,
                                     image=image_joystick,
                                     text="My Games",
                                     width=100,
                                     height=60,
                                     fg_color="#000001",
                                     cursor="hand2",
                                     font=("Arial", 35))
        pywinstyles.set_opacity(self.mygames_btn, color="#000001")
        self.mygames_btn.place(x=150, y=310, anchor=tkinter.CENTER)

        self.notes_btn = CTkButton(master=self.sidebar,
                                   image=image_notes,
                                   text="Notes",
                                   width=100,
                                   height=60,
                                   fg_color="#000001",
                                   cursor="hand2",
                                   font=("Arial", 35))
        pywinstyles.set_opacity(self.notes_btn, color="#000001")
        self.notes_btn.place(x=150, y=400, anchor=tkinter.CENTER)

        self.wishlist_btn = CTkButton(master=self.sidebar,
                                      image=image_geschenk,
                                      text="Wishlist",
                                      width=100,
                                      height=60,
                                      fg_color="#000001",
                                      cursor="hand2",
                                      font=("Arial", 35))
        pywinstyles.set_opacity(self.wishlist_btn, color="#000001")
        self.wishlist_btn.place(x=150, y=490, anchor=tkinter.CENTER)

        self.profile_btn = CTkButton(master=self.sidebar,
                                     image=image_user,
                                     text="Profile",
                                     width=100,
                                     height=60,
                                     fg_color="#000001",
                                     cursor="hand2",
                                     font=("Arial", 35))
        pywinstyles.set_opacity(self.profile_btn, color="#000001")
        self.profile_btn.place(x=150, y=580, anchor=tkinter.CENTER)