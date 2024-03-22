from cgitb import text
import imp
import tkinter
from turtle import color, st, width
from click import command
import click
import comm
import customtkinter
import PIL
from PIL import Image,ImageTk
from tkinter import Canvas, PhotoImage, Tk
from tkinter.ttk import Frame,Label,Style
from flask.cli import prepare_import
from numpy import cumsum, imag, size
import pywinstyles
from panel import widget
from referencing import Anchor
from screeninfo import get_monitors
from sqlalchemy import PrimaryKeyConstraint
from sympy import HeuristicGCDFailed, im




app = customtkinter.CTk()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


image = PIL.Image.open("Design/Background.png")                         #Background festlegen           
background_image = customtkinter.CTkImage(image, size=(1280, 720))
bg_lbl = customtkinter.CTkLabel(app, text="", image=background_image)
bg_lbl.place(x=0, y=0)

app.title("Startpage")
app.geometry("1280x720")  #Gröse festlegen 

#app.iconphoto(False, tkinter.PhotoImage(file="Design/Icon.png"))

#Die größen des Monitores einholen 
for data in get_monitors():
    print(str(data))

  
    def Settings():
        print("Settings---->")

    def Store():
        print("Store->")

    def Mygames():
        print("Mygames->")

    def Wishlist():
        print("wishlist->")

    def Notes():
        print("notes->")

    def Profile():
        print("profile->")


#settingsbutton
settings = customtkinter.CTkButton(master=app,
                                        width=200,
                                        height=250,
                                        corner_radius=20,
                                        fg_color="#250454",
                                        bg_color="#000001",
                                        text="",
                                        hover_color="#250454",
                                        command=Settings
                                        )
pywinstyles.set_opacity(settings,color="#000001")
settings.place(x=250,y=370)

settingsimg = PIL.Image.open("Tkinter_GUI/StartseiteIMG/settings.png")
imgsettings = customtkinter.CTkImage(settingsimg,size=(100,100))
settingslbl = customtkinter.CTkLabel(settings,text="",image=imgsettings)
settingslbl.bind("<Button-1>",lambda e,:Settings())
settingslbl.place(x=100,y=90,anchor=tkinter.CENTER)

settingstext = customtkinter.CTkLabel(settings,text="Settings",font=("Arial",25),text_color="#B886F8")
settingstext.place(x=100,y=180,anchor=tkinter.CENTER)
settingstext.bind("<Button-1>",lambda e,:Settings())



#storebutton
store = customtkinter.CTkButton(master=app,
                                 width=200,
                                 height=250,
                                 corner_radius=20,
                                 fg_color="#250454",
                                 bg_color="#000001",text="",
                                 hover_color="#250454",
                                 command=Store
                                    )
pywinstyles.set_opacity(store, color="#000001")
store.place(x=540,y=70)

storeimg = PIL.Image.open("Tkinter_GUI/StartseiteIMG/shopping-cart.png")
imgstore = customtkinter.CTkImage(storeimg,size=(100,100))
storelbl = customtkinter.CTkLabel(store,text="",image=imgstore)
storelbl.bind("<Button-1>",lambda e,:Store())
storelbl.place(x=100,y=90,anchor=tkinter.CENTER)

storetext = customtkinter.CTkLabel(store,text="Store",font=("Arial",25),text_color="#B886F8")
storetext.place(x=100,y=180,anchor=tkinter.CENTER)
storetext.bind("<Button-1>",lambda e,:Store())


#mygamesbutton
mygames = customtkinter.CTkButton(master=app,
                                       width=200,
                                       height=250,
                                       corner_radius=20,
                                       fg_color="#250454",
                                       bg_color="#000001",
                                       text="",
                                       hover_color="#250454",
                                       command=Mygames
                                       )
pywinstyles.set_opacity(mygames, color="#000001")
mygames.place(x=830,y=70)

mygamesimg = PIL.Image.open("Tkinter_GUI/StartseiteIMG/joystick.png")
imgmygames = customtkinter.CTkImage(mygamesimg,size=(100,100))
mygameslbl = customtkinter.CTkLabel(mygames,text="",image=imgmygames)
mygameslbl.bind("<Button-1>",lambda e,:Mygames())
mygameslbl.place(x=100,y=90,anchor=tkinter.CENTER)

mygamestext = customtkinter.CTkLabel(mygames,text="My Games",font=("Arial",25),text_color="#B886F8")
mygamestext.place(x=100,y=180,anchor=tkinter.CENTER)
mygamestext.bind("<Button-1>",lambda e,:Mygames())


#wishlistbutton
wishlist = customtkinter.CTkButton(master=app,
                                        width=200,
                                        height=250,
                                        corner_radius=20,
                                        fg_color="#250454",
                                        bg_color="#000001",
                                        text="",
                                        hover_color="#250454",
                                        command=Wishlist
                                        )
pywinstyles.set_opacity(wishlist, color="#000001")
wishlist.place(x=830, y=370)

wishlistimg = PIL.Image.open("Tkinter_GUI/StartseiteIMG/geschenk.png")
imgwishlist = customtkinter.CTkImage(wishlistimg,size=(100,100))
wishlistlbl = customtkinter.CTkLabel(wishlist,text="",image=imgwishlist)
wishlistlbl.bind("<Button-1>",lambda e,:Wishlist())
wishlistlbl.place(x=100,y=100,anchor=tkinter.CENTER)

wishlisttxt = customtkinter.CTkLabel(wishlist,text="Wishlist", font=("Arial",25), text_color="#B886F8")
wishlisttxt.place(x=100,y=180,anchor=tkinter.CENTER)
wishlisttxt.bind("<Button-1>",lambda e,:Wishlist())


#notesbutton
notes= customtkinter.CTkButton(master=app,
                                    width=200,
                                    height=250,
                                    corner_radius=20,
                                    fg_color="#250454",
                                    bg_color="#000001",
                                    text="",
                                    hover_color="#250454",
                                    command=Notes
                                    )
pywinstyles.set_opacity(notes, color="#000001")
notes.place(x=540, y=370)

notesimg = PIL.Image.open("Tkinter_GUI/StartseiteIMG/notes.png")
imgnotes = customtkinter.CTkImage(notesimg,size=(100,100))
noteslbl = customtkinter.CTkLabel(notes,text="",image=imgnotes)
noteslbl.bind("<Button-1>",lambda e,:Notes())
noteslbl.place(x=100,y=100,anchor=tkinter.CENTER)

notestxt = customtkinter.CTkLabel(notes,text="Notes",font=("Arial",25),text_color="#B886F8")
notestxt.place(x=100,y=180,anchor=tkinter.CENTER)
notestxt.bind("<Button-1>",lambda e,:Notes())

#profilebutton
profile = customtkinter.CTkButton(master=app,
                                       width=200,
                                       height=250,
                                       corner_radius=20,
                                       fg_color="#250454",
                                       bg_color="#000001",
                                       text="",
                                       hover_color="#250454",
                                       command=Profile
                                       )
pywinstyles.set_opacity(profile, color="#000001")
profile.place(x=250, y=70)

profileimg = PIL.Image.open("Tkinter_GUI/StartseiteIMG/user.png")
imgprofile = customtkinter.CTkImage(profileimg,size=(100,100))
profilelbl = customtkinter.CTkLabel(profile,text="",image=imgprofile)
profilelbl.bind("<Button-1>",lambda e,:Profile())
profilelbl.place(x=100,y=100,anchor=tkinter.CENTER)

profiletext = customtkinter.CTkLabel(profile,text="Profile",font=("Arial",25),text_color="#B886F8")
profiletext.place(x=100,y=180,anchor=tkinter.CENTER)
profiletext.bind("<Button-1>",lambda e,:Profile())





app.mainloop()
