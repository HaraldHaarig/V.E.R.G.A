import tkinter
from click import command
from customtkinter import *
from PIL import Image
import fontTools
from matplotlib.backend_bases import cursors
from pyparsing import col
import pywinstyles
import ctypes

set_appearance_mode("dark")

app = CTk()
app.geometry("1280x720")
app.title("V.E.R.G.A GameLauncher")
# app.iconbitmap(default="Design/Icon.png")
# app.iconphoto(False, tkinter.PhotoImage(file="Design/Icon.png"))
# myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
# ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# Der Main Frame wird ein wenig nach links verschoben und ein neues Frame mit Freunden soll generiert werden
def FriendsOut():
    print("Servus")

# Background Image
image = Image.open("Design/Background.png")
background_image = CTkImage(image, size=(1280, 720))

bg_lbl = CTkLabel(app, text="", image = background_image)
bg_lbl.place(x = 0, y = 0)

# Frame für die Profildaten
profile = CTkFrame(master=app,
                   width=350,
                   height=650,
                   corner_radius=20,
                   fg_color="#250454",
                   bg_color="#000001")
pywinstyles.set_opacity(profile, color="#000001")
profile.place(x=640, y=360, anchor=tkinter.CENTER)

# Labels

username_lbl = CTkLabel(profile,
                        text="Username",
                        text_color="White",
                        bg_color="#000001",
                        font=("Arial", 25))
pywinstyles.set_opacity(username_lbl, color="#000001")
username_lbl.place(x=175, y=25, anchor=tkinter.CENTER)


playtime_lbl = CTkLabel(profile,
                        text="Playtime: ",
                        text_color="White",
                        bg_color="#000001",
                        font=("Arial", 22))
pywinstyles.set_opacity(playtime_lbl, color="#000001")
playtime_lbl.place(x=20, y=70, anchor=tkinter.W)

steam_lbl = CTkLabel(profile,
                    text="Steam: ",
                    text_color="White",
                    bg_color="#000001",
                    font=("Arial", 22))
pywinstyles.set_opacity(steam_lbl, color="#000001")
steam_lbl.place(x=20, y=105, anchor=tkinter.W)

riot_lbl = CTkLabel(profile,
                    text="Riot Games: ",
                    text_color="White",
                    bg_color="#000001",
                    font=("Arial", 22))
pywinstyles.set_opacity(riot_lbl, color="#000001")
riot_lbl.place(x=20, y=140, anchor=tkinter.W)

anzahlGames_lbl = CTkLabel(profile,
                           text="Anzahl Games: ",
                           text_color="White",
                           bg_color="#000001",
                           font=("Arial", 22))
pywinstyles.set_opacity(anzahlGames_lbl, color="#000001")
anzahlGames_lbl.place(x=20, y=175, anchor=tkinter.W)

recentlyPlayed_lbl = CTkLabel(profile,
                              text="Recently Played: ",
                              text_color="White",
                              bg_color="#000001",
                              font=("Arial", 22))
pywinstyles.set_opacity(recentlyPlayed_lbl, color="#000001")
recentlyPlayed_lbl.place(x=20, y=210, anchor=tkinter.W)

friends_lbl = CTkLabel(profile,
                       text="Friends: ",
                       text_color="White",
                       bg_color="#000001",
                       font=("Arial", 22))
friends_lbl.bind("<Button-1>", lambda e,:FriendsOut())
pywinstyles.set_opacity(friends_lbl, color="#000001")
friends_lbl.place(x=20, y=245, anchor=tkinter.W)

ban_status_lbl = CTkLabel(profile,
                          text="VAC Ban: ",
                          text_color="White",
                          bg_color="#000001",
                          font=("Arial", 22))
pywinstyles.set_opacity(ban_status_lbl, color="#000001")
ban_status_lbl.place(x=20, y=280, anchor=tkinter.W)

app.mainloop()