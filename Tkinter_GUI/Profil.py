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

class Profil:
    def __init__(self):
        set_appearance_mode("dark")
        self.app = CTk()
        self.app.geometry("1280x720")
        self.app.title("V.E.R.G.A GameLauncher")
        # app.iconbitmap(default="Design/Icon.png")
        # app.iconphoto(False, tkinter.PhotoImage(file="Design/Icon.png"))
        # myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
        # ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        # Background Image
        image = Image.open("Design/Background.png")
        background_image = CTkImage(image, size=(1280, 720))

        bg_lbl = CTkLabel(self.app, text="", image = background_image)
        bg_lbl.place(x = 0, y = 0)

        self.temp = 0
        self.my_x = 640

        # Mainframe
        self.profile = CTkFrame(master=self.app,
                                width=350,
                                height=650,
                                corner_radius=20,
                                fg_color="#250454",
                                bg_color="#000001")
        pywinstyles.set_opacity(self.profile, color="#000001")
        self.profile.place(x=self.my_x, y=360, anchor=tkinter.CENTER)

        # Überschrifts Label für den Username
        username_lbl = CTkLabel(self.profile,
                                text="Username",
                                text_color="White",
                                bg_color="#000001",
                                font=("Arial", 25))
        pywinstyles.set_opacity(username_lbl, color="#000001")
        username_lbl.place(x=175, y=25, anchor=tkinter.CENTER)

        # Label für die gesamte Playtime des Users
        playtime_lbl = CTkLabel(self.profile,
                                text="Playtime: ",
                                text_color="White",
                                bg_color="#000001",
                                font=("Arial", 22))
        pywinstyles.set_opacity(playtime_lbl, color="#000001")
        playtime_lbl.place(x=20, y=70, anchor=tkinter.W)

        # Label, ob der User mit Steam verbunden ist
        steam_lbl = CTkLabel(self.profile,
                             text="Steam: ",
                             text_color="White",
                             bg_color="#000001",
                             font=("Arial", 22))
        pywinstyles.set_opacity(steam_lbl, color="#000001")
        steam_lbl.place(x=20, y=105, anchor=tkinter.W)

        # Label, ob der User mit Riot Games verbunden ist
        riot_lbl = CTkLabel(self.profile,
                            text="Riot Games: ",
                            text_color="White",
                            bg_color="#000001",
                            font=("Arial", 22))
        pywinstyles.set_opacity(riot_lbl, color="#000001")
        riot_lbl.place(x=20, y=140, anchor=tkinter.W)

        # Label, welches die Anzahl der Games des Users anzeigt
        anzahlGames_lbl = CTkLabel(self.profile,
                                   text="Anzahl Games: ",
                                   text_color="White",
                                   bg_color="#000001",
                                   font=("Arial", 22))
        pywinstyles.set_opacity(anzahlGames_lbl, color="#000001")
        anzahlGames_lbl.place(x=20, y=175, anchor=tkinter.W)

        # Label, welches das zuletzt gespielte Spiel anzeigt
        recentlyPlayed_lbl = CTkLabel(self.profile,
                                      text="Recently Played: ",
                                      text_color="White",
                                      bg_color="#000001",
                                      font=("Arial", 22))
        pywinstyles.set_opacity(recentlyPlayed_lbl, color="#000001")
        recentlyPlayed_lbl.place(x=20, y=210, anchor=tkinter.W)

        # Label, welches anzeigt, ob der Account einen VAC Bann auf Steam hat
        ban_status_lbl = CTkLabel(self.profile,
                                  text="VAC Ban: ",
                                  text_color="White",
                                  bg_color="#000001",
                                  font=("Arial", 22))
        pywinstyles.set_opacity(ban_status_lbl, color="#000001")
        ban_status_lbl.place(x=20, y=245, anchor=tkinter.W)

        # Button, auf dem man klicken kann. Der Klappt dann aus und zeigt im besten Fall die Steam-Freunde an
        friends_lbl = CTkButton(self.profile,
                                width=30,
                                text="Friends: ",
                                text_color="White",
                                fg_color="#250454",
                                bg_color="#000001",
                                font=("Arial", 22))
        friends_lbl.bind("<Button-1>", lambda e,:self.FriendsOut())
        pywinstyles.set_opacity(friends_lbl, color="#000001")
        friends_lbl.place(x=13, y=280, anchor=tkinter.W)

        self.app.mainloop()
    
    # Der Main Frame wird ein wenig nach links verschoben und ein neues Frame mit Freunden soll generiert werden
    def FriendsOut(self):
        if self.my_x > 448:
            self.my_x -= 2
            self.profile.place(x=self.my_x, y=360, anchor=tkinter.CENTER)
            self.app.after(2, self.FriendsOut)
            
        if self.my_x == 448:
            # Das auftauchende Frame für die Freunde
            self.friends = CTkFrame(master=self.app,
                                    width=350,
                                    height=380,
                                    corner_radius=20,
                                    fg_color="#250454",
                                    bg_color="#000001")
            pywinstyles.set_opacity(self.friends, color="#00001")
            self.friends.place(x=830, y=485, anchor=tkinter.CENTER)

            # Labels für das extra Freunde-Frame
            self.friends_heading_lbl = CTkLabel(master=self.friends,
                                                text="Friends",
                                                text_color="White",
                                                bg_color="#000001",
                                                font=("Arial", 25))
            pywinstyles.set_opacity(self.friends_heading_lbl, color="#000001")
            self.friends_heading_lbl.place(x=175, y=25, anchor=tkinter.CENTER)

            self.arrow_img = Image.open("Design/arrow.png")
            self.goBackArrow = CTkImage(self.arrow_img, size=(30, 30))

            self.goBackArrow_lbl = CTkLabel(master=self.friends, text="", image=self.goBackArrow)
            self.goBackArrow_lbl.place(x=10, y=10)
            self.goBackArrow_lbl.bind("<Button-1>", lambda e,:self.FriendsIn())
        
    def FriendsIn(self):
        if self.my_x == 448:
            self.friends_heading_lbl.destroy()              #TODO: Kein neues Frame erstellen, sondern das "Profile" Frame mit den Freunden überschreiben. Heute mochma Schicht. Bruch
            self.goBackArrow_lbl.destroy()
            

        if self.my_x < 640:
            self.my_x += 2
            self.profile.place(x=self.my_x, y=360, anchor=tkinter.CENTER)
            self.app.after(2, self.FriendsIn)