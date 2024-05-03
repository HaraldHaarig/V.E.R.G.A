import tkinter
import customtkinter
from tkinter import *
from screeninfo import get_monitors
from PIL import Image
import ctypes
import pywinstyles
from API.GameAPI import getImg
from Tkinter_GUI.Spielcards import Spielcards
from Tkinter_GUI.LoadingScreen import Loadingscreen
from Tkinter_GUI.Profil import Profil
from API.SteamAPI import getSteamGamesbyID



class Startpage:

    def __init__(self):
        self.app = customtkinter.CTk()

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.app.geometry("1280x720")
        self.app.title("Startpage")


        image = Image.open("Design/Background.png")                                  #Image initialitieren
        imagebg = customtkinter.CTkImage(image,size=(1280,720))

        bg_label = customtkinter.CTkLabel(self.app, text="", image=imagebg)                   #backgrund imagelabel
        bg_label.place(x=0,y=0)

        self.app.iconbitmap(default="Design/Icon.png")
        self.app.iconphoto(False, PhotoImage(master=self.app,file="Design/Icon.png"))              #Icon festlegen

        myappid = u'mycompany.myproduct.subproduct.version'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)          #Icon festlegen


        
        #settingsbutton
        settings = customtkinter.CTkButton(master=self.app,
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
        store = customtkinter.CTkButton(master=self.app,
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


        #myGames
        mygames = customtkinter.CTkButton(master=self.app,
                                            width=200,
                                            height=250,
                                            corner_radius=20,
                                            fg_color="#250454",
                                            bg_color="#000001",
                                            text="",
                                            hover_color="#250454",
                                            command=self.Mygames
                                            )
        pywinstyles.set_opacity(mygames, color="#000001")
        mygames.place(x=830,y=70)

        image = Image.open("Tkinter_GUI/StartseiteIMG/joystick.png")
        imagemygames = customtkinter.CTkImage(image,size=(100,100))

        mygameslbl = customtkinter.CTkLabel(mygames,text="",image=imagemygames)
        mygameslbl.bind("<Button-1>",lambda e, :self.Mygames())
        mygameslbl.place(x=100,y=90,anchor=tkinter.CENTER)

        mygamestxt = customtkinter.CTkLabel(mygames,text="Mygames",font=("Arial",25),text_color="#B886F8")
        mygamestxt.place(x=100,y=180,anchor=tkinter.CENTER)
        mygamestxt.bind("<Button-1>",lambda e, :self.Mygames())


         #wishlist
        wishlist = customtkinter.CTkButton(master=self.app,
                                                width=200,
                                                height=250,
                                                corner_radius=20,
                                                fg_color="#250454",
                                                bg_color="#000001",
                                                text="",
                                                hover_color="#250454",
                                                command=self.Wishlist
                                                )
        pywinstyles.set_opacity(wishlist, color="#000001")
        wishlist.place(x=830, y=370) 
    
        image = Image.open("Tkinter_GUI/StartseiteIMG/geschenk.png")
        imagewishlist = customtkinter.CTkImage(image,size=(100,100))

        wishlistlbl = customtkinter.CTkLabel(wishlist,text="",image=imagewishlist)
        wishlistlbl.bind("<Button-1>",lambda e, :self.Wishlist())
        wishlistlbl.place(x=100,y=90,anchor=tkinter.CENTER)

        wishlisttxt = customtkinter.CTkLabel(wishlist,text="Wishlist",font=("Arial",25),text_color="#B886F8")
        wishlisttxt.bind("<Button-1>",lambda e, :self.Wishlist())
        wishlisttxt.place(x=100,y=180,anchor=tkinter.CENTER)

        #notes
        notes= customtkinter.CTkButton(master=self.app,
                                            width=200,
                                            height=250,
                                            corner_radius=20,
                                            fg_color="#250454",
                                            bg_color="#000001",
                                            text="",
                                            hover_color="#250454",
                                            command=self.Notes
                                            )
        pywinstyles.set_opacity(notes, color="#000001")
        notes.place(x=540, y=370)

        image = Image.open("Tkinter_GUI/StartseiteIMG/notes.png")
        imagenotes = customtkinter.CTkImage(image,size=(100,100))

        noteslbl = customtkinter.CTkLabel(notes,text="",image=imagenotes)
        noteslbl.bind("<Button-1>",lambda e, :self.Notes())
        noteslbl.place(x=100,y=90,anchor=tkinter.CENTER)

        notestxt = customtkinter.CTkLabel(notes,text="Notes",font=("Arial",25),text_color="#B886F8")
        notestxt.bind("<Button-1>",lambda e, :self.Notes())
        notestxt.place(x=100,y=180,anchor=tkinter.CENTER)


        #profile
        profile = customtkinter.CTkButton(master=self.app,
                                            width=200,
                                            height=250,
                                            corner_radius=20,
                                            fg_color="#250454",
                                            bg_color="#000001",
                                            text="",
                                            hover_color="#250454",
                                            command=self.Profile
                                            )
        pywinstyles.set_opacity(profile, color="#000001")
        profile.place(x=250, y=70)

        image = Image.open("Tkinter_GUI/StartseiteIMG/user.png")
        imageprofile = customtkinter.CTkImage(image,size=(100,100))

        profilelbl = customtkinter.CTkLabel(profile,text="",image=imageprofile)
        profilelbl.bind("<Button-1>",lambda e, :self.Profile())
        profilelbl.place(x=100,y=90,anchor=tkinter.CENTER)

        profiletxt = customtkinter.CTkLabel(profile,text="Profile",font=("Arial",25),text_color="#B886F8")
        profiletxt.bind("<Button-1>",lambda e, :self.Profile())
        profiletxt.place(x=100,y=180,anchor=tkinter.CENTER)
        
        

        self.app.mainloop()







    def Settings(self):
        print("Settings->") 
        
    
    def Store(self):
        print("Store->")
        #self.app.destroy()
    
    def Mygames(self):
        print("My games->") # Temporär bis Bibliothek fertig ist
        self.app.destroy()
        spielcard=Spielcards()
        
        url,title,details=getSteamGamesbyID("76561199015522225")


        count=0
        for s in url:
            if s == 0:
                url[count]=getImg(title[count])
                if(url[count]==0):
                    url[count]="https://cdn-icons-png.flaticon.com/512/16/16096.png"
            count+=1
        spielcard.showallCards(url,title,details)
    
    
    def Wishlist(self):
        print("Wishlist->")
        #self.app.destroy()
    
    def Notes(self):
        print("Notes->")
        #self.app.destroy()

    def Profile(self):
        print("profile->")
        self.app.destroy()
        profil = Profil()