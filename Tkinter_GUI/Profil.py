import tkinter
from customtkinter import *
from PIL import Image
import fontTools
from pyparsing import col
import pywinstyles

set_appearance_mode("dark")

app = CTk()
app.geometry("1280x720")
app.title("V.E.R.G.A GameLauncher")

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

username_lbl = CTkLabel(app,
                        text="Username",
                        text_color="White",
                        bg_color="#000001",
                        font=("Arial", 25))
pywinstyles.set_opacity(username_lbl, color="#000001")
username_lbl.place(x=640, y=60, anchor=tkinter.CENTER)


playtime_lbl = CTkLabel(app,
                        text="Playtime: ",
                        text_color="White",
                        bg_color="#000001",
                        font=("Arial", 22))
pywinstyles.set_opacity(playtime_lbl, color="#000001")
playtime_lbl.place(x=475, y=100, anchor=tkinter.W)

steam_lbl = CTkLabel(app,
                    text="Steam: ",
                    text_color="White",
                    bg_color="#000001",
                    font=("Arial", 22))
pywinstyles.set_opacity(steam_lbl, color="#000001")
steam_lbl.place(x=475, y=140, anchor=tkinter.W)

riot_lbl = CTkLabel(app,
                    text="Riot Games: ",
                    text_color="White",
                    bg_color="#000001",
                    font=("Arial", 22))
pywinstyles.set_opacity(riot_lbl, color="#000001")
riot_lbl.place(x=475, y=180, anchor=tkinter.W)

anzahlGames_lbl = CTkLabel(app,
                           text="Anzahl Games: ",
                           text_color="White",
                           bg_color="#000001",
                           font=("Arial", 22))
pywinstyles.set_opacity(anzahlGames_lbl, color="#000001")
anzahlGames_lbl.place(x=475, y=220, anchor=tkinter.W)

recentlyPlayed_lbl = CTkLabel(app,
                              text="Recently Played: ",
                              text_color="White",
                              bg_color="#000001",
                              font=("Arial", 22))
pywinstyles.set_opacity(recentlyPlayed_lbl, color="#000001")
recentlyPlayed_lbl.place(x=475, y=260, anchor=tkinter.W)

friends_lbl = CTkLabel(app,
                    text="Friends: ",
                    text_color="White",
                    bg_color="#000001",
                    font=("Arial", 22))
pywinstyles.set_opacity(friends_lbl, color="#000001")
friends_lbl.place(x=475, y=300, anchor=tkinter.W)

app.mainloop()