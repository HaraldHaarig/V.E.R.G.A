from cgitb import text
from gc import disable
import tkinter
import arrow
from click import command
from customtkinter import *
from PIL import Image
import fontTools
from matplotlib.backend_bases import cursors
from pyparsing import col
import pywinstyles
import ctypes
from sympy import false, im
from Tkinter_GUI.Sidebar import Sidebar
from Tkinter_GUI.Login import Login
from API.SteamAPI import getSteamProfile

class Profil:
    def __init__(self, login:Login):
        
        set_appearance_mode("dark")
        self.app = CTk()
        self.app.title("V.E.R.G.A GameLauncher")
        username,recPlayed,playtime,vac_ban,counter,sincelastban,steamlvl,id=getSteamProfile(login.getSteamId())
        # Zuständig für das zentrieren des Fensters in der Mitte des Monitors
        widh_of_window = 1280
        height_of_window = 720
        scree_widh = self.app.winfo_screenwidth()
        screen_height = self.app.winfo_screenheight()
        x_cordinate = (scree_widh/2)-(widh_of_window/2)
        y_cordinate = (screen_height/2)-(height_of_window/2)
        self.app.geometry("%dx%d+%d+%d" %(widh_of_window,height_of_window,x_cordinate,y_cordinate))

        # app.iconbitmap(default="Design/Icon.png")
        # app.iconphoto(False, tkinter.PhotoImage(file="Design/Icon.png"))
        # myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
        # ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        # Background Image
        image = Image.open("Design/Background.png")
        background_image = CTkImage(image, size=(1280, 720))

        bg_lbl = CTkLabel(self.app, text="", image = background_image)
        bg_lbl.place(x = 0, y = 0)

        sidebar = Sidebar(self.app,login)
        
        # Mainframe
        self.profile = CTkFrame(master=self.app,
                                width=350,
                                height=650,
                                corner_radius=20,
                                fg_color="#250454",
                                bg_color="#000001")
        pywinstyles.set_opacity(self.profile, color="#000001")
        self.profile.place(x=790, y=360, anchor=tkinter.CENTER)

        # Überschrifts Label für den Username
        self.username_lbl = CTkLabel(self.profile,
                                text=username,
                                text_color="White",
                                bg_color="#000001",
                                font=("Arial", 25))
        pywinstyles.set_opacity(self.username_lbl, color="#000001")
        self.username_lbl.place(x=175, y=25, anchor=tkinter.CENTER)

        # Label für die gesamte Playtime des Users
        self.playtime_lbl = CTkLabel(self.profile,
                                text="Playtime: "+str(round(playtime))+" h",
                                text_color="White",
                                bg_color="#000001",
                                font=("Arial", 22))
        pywinstyles.set_opacity(self.playtime_lbl, color="#000001")
        self.playtime_lbl.place(x=20, y=70, anchor=tkinter.W)

        # # Label, ob der User mit Steam verbunden ist
        # steam_lbl = CTkLabel(self.profile,
        #                      text="Steam: ",
        #                      text_color="White",
        #                      bg_color="#000001",
        #                      font=("Arial", 22))
        # pywinstyles.set_opacity(steam_lbl, color="#000001")
        # steam_lbl.place(x=20, y=105, anchor=tkinter.W)

        # # Label, ob der User mit Riot Games verbunden ist
        # riot_lbl = CTkLabel(self.profile,
        #                     text="Riot Games: ",
        #                     text_color="White",
        #                     bg_color="#000001",
        #                     font=("Arial", 22))
        # pywinstyles.set_opacity(riot_lbl, color="#000001")
        # riot_lbl.place(x=20, y=140, anchor=tkinter.W)

        # Label, welches die Anzahl der Games des Users anzeigt
        self.anzahlGames_lbl = CTkLabel(self.profile,
                                   text="Anzahl Games: "+str(counter),
                                   text_color="White",
                                   bg_color="#000001",
                                   font=("Arial", 22))
        pywinstyles.set_opacity(self.anzahlGames_lbl, color="#000001")
        self.anzahlGames_lbl.place(x=20, y=105, anchor=tkinter.W)

        # Label, welches das zuletzt gespielte Spiel anzeigt
        self.recentlyPlayed_lbl = CTkLabel(self.profile,
                                      text="Recently Played: "+str(recPlayed['games'][0]['name']),
                                      text_color="White",
                                      bg_color="#000001",
                                      font=("Arial", 22))
        pywinstyles.set_opacity(self.recentlyPlayed_lbl, color="#000001")
        self.recentlyPlayed_lbl.place(x=20, y=140, anchor=tkinter.W)

        # Label, welches anzeigt, ob der Account einen VAC Bann auf Steam hat
        self.ban_status_lbl = CTkLabel(self.profile,
                                  text="VAC Ban: "+str(vac_ban),
                                  text_color="White",
                                  bg_color="#000001",
                                  font=("Arial", 22))
        pywinstyles.set_opacity(self.ban_status_lbl, color="#000001")
        self.ban_status_lbl.place(x=20, y=175, anchor=tkinter.W)

        # Button, auf dem man klicken kann. Der Klappt dann aus und zeigt im besten Fall die Steam-Freunde an
        self.daysSinceLastBan_lbl = CTkLabel(self.profile,
                                width=30,
                                text="Days since last ban: "+str(sincelastban),
                                text_color="White",
                                fg_color="#250454",
                                bg_color="#000001",
                                font=("Arial", 22),
                                cursor="hand2")
        pywinstyles.set_opacity(self.daysSinceLastBan_lbl, color="#000001")
        self.daysSinceLastBan_lbl.place(x=13, y=210, anchor=tkinter.W)

        self.steamLVL_lbl = CTkLabel(self.profile,
                            width=30,
                            text="SteamLVL: "+str(steamlvl),
                            text_color="White",
                            fg_color="#250454",
                            bg_color="#000001",
                            font=("Arial", 22),
                            cursor="hand2")
        pywinstyles.set_opacity(self.steamLVL_lbl, color="#000001")
        self.steamLVL_lbl.place(x=13, y=245, anchor=tkinter.W)

        self.steamID_lbl = CTkLabel(self.profile,
                            width=30,
                            text="SteamID: "+str(id),
                            text_color="White",
                            fg_color="#250454",
                            bg_color="#000001",
                            font=("Arial", 22),
                            cursor="hand2")
        pywinstyles.set_opacity(self.steamID_lbl, color="#000001")
        self.steamID_lbl.place(x=13, y=280, anchor=tkinter.W)


        self.app.mainloop()
    
    
   

    

        
