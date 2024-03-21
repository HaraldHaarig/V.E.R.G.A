from cgitb import text
import tkinter
from tkinter.font import Font
from turtle import color
from customtkinter import *
from PIL import Image
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

# Frame für die Spielbeschreibung
description = CTkFrame(master=app,
                 width=700,
                 height=400,
                 corner_radius=20,
                 fg_color="#250454",
                 bg_color="#000001")
pywinstyles.set_opacity(description, color="#000001")
description.place(x=425, y=450, anchor=tkinter.CENTER)

# Frame für die Game Stats
stats = CTkFrame(master=app,
                 width=400,
                 height=400,
                 corner_radius=20,
                 fg_color="#250454",
                 bg_color="#000001")
pywinstyles.set_opacity(stats, color="#000001")
stats.place(x=1005, y=450, anchor=tkinter.CENTER)

# Label für die Game Beschreibung
description_lbl = CTkLabel(app, 
                           text="Game Beschreibung", 
                           text_color="White", 
                           bg_color="#000001", 
                           font=("Arial", 25))
pywinstyles.set_opacity(description_lbl, color="#000001")
description_lbl.place(x=425, y=275, anchor=tkinter.CENTER)

# Label für die Game "Stats"
stats_lbl = CTkLabel(app, 
                     text="Game Stats", 
                     text_color="White", 
                     bg_color="#000001", 
                     font=("Arial", 25))
pywinstyles.set_opacity(stats_lbl, color="#000001")
stats_lbl.place(x=1005, y=275, anchor=tkinter.CENTER)

# Label für die Playtime
playtime_lbl = CTkLabel(app, 
                        text="Playtime: ",
                        text_color="White",
                        bg_color="#000001",
                        font=("Arial", 22))
pywinstyles.set_opacity(playtime_lbl, color="#000001")
playtime_lbl.place(x=825, y=325, anchor=tkinter.W)

# Label für den Publisher
publisher_lbl = CTkLabel(app, 
                        text="Publisher: ",
                        text_color="White",
                        bg_color="#000001",
                        font=("Arial", 22))
pywinstyles.set_opacity(publisher_lbl, color="#000001")
publisher_lbl.place(x=825, y=360, anchor=tkinter.W)

# Label für den Developer
developer_lbl = CTkLabel(app, 
                        text="Developer: ",
                        text_color="White",
                        bg_color="#000001",
                        font=("Arial", 22))
pywinstyles.set_opacity(developer_lbl, color="#000001")
developer_lbl.place(x=825, y=395, anchor=tkinter.W)

# Label für das Erscheinungsdatum
releasedate_lbl = CTkLabel(app, 
                        text="Release Date: ",
                        text_color="White",
                        bg_color="#000001",
                        font=("Arial", 22))
pywinstyles.set_opacity(releasedate_lbl, color="#000001")
releasedate_lbl.place(x=825, y=430, anchor=tkinter.W)

# app.overrideredirect(True)            Remove Titlebar (mehr oder weniger)
app.mainloop()