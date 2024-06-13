import tkinter
from customtkinter import *
from PIL import Image
import re
import pywinstyles
from sympy import false
from GameStarter import startGame
from DB_Service.Wishlist import addToWishlist


def spielbeschreibung_main(title,gamedescription, playtime, reldate, metascore, price, controller, reqage, platforms,restore_details,restore_titles,restore_urls,owned,login):

    set_appearance_mode("dark")

    app = CTk()
    app.geometry("1280x720")
    app.title("V.E.R.G.A GameLauncher")
    
    # Background Image
    image = Image.open("Design/Background.png")
    background_image = CTkImage(image, size=(1280, 720))
    #Background Image Label
    bg_lbl = CTkLabel(app, text="", image = background_image)
    bg_lbl.place(x = 0, y = 0)
    
    backimg= Image.open("Design/back.png")
    
    gobackimg=CTkImage(backimg,size=(50,50))
    
    back = CTkLabel(app,text="",image=gobackimg)
    back.place(x=1230,y=0)
    back.bind("<Button-1>",lambda e:goback(app,restore_details,restore_titles,restore_urls,login))

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

    # Label für den Überpunkt "Game Beschreibung"
    description_title_lbl = CTkLabel(app, 
                            text="Game Beschreibung", 
                            text_color="White", 
                            bg_color="#000001", 
                            font=("Arial", 25))
    pywinstyles.set_opacity(description_title_lbl, color="#000001")
    description_title_lbl.place(x=425, y=275, anchor=tkinter.CENTER)

    # Label für den Überpunkt "Stats"
    stats_lbl = CTkLabel(app, 
                        text="Game Stats", 
                        text_color="White", 
                        bg_color="#000001", 
                        font=("Arial", 25))
    pywinstyles.set_opacity(stats_lbl, color="#000001")
    stats_lbl.place(x=1005, y=275, anchor=tkinter.CENTER)

    #RegEx für Beschreibung weil sonst lore
    cleanedDescription = re.sub(r'</?p>', '', gamedescription)

    # Leeres Label für die Spielbeschreibungen
    description_lbl = CTkLabel(description,
                            text=cleanedDescription,
                            text_color="White",
                            bg_color="#000001",
                            font=("Arial", 22),
                            wraplength=690)
    pywinstyles.set_opacity(description_lbl, color="#000001")
    description_lbl.place(x=10, y=105, anchor=tkinter.W)

    try:
        time = "{:.2f}".format(playtime)
    except (ValueError, TypeError):
        time = "N/A"

    #time = "{:.2f}".format(playtime) # Runden der playtime sonst zu lang
    # Label für die Playtime
    playtime_lbl = CTkLabel(stats, 
                            text="Playtime: "+str(time)+" h",
                            text_color="White",
                            bg_color="#000001",
                            font=("Arial", 22))
    pywinstyles.set_opacity(playtime_lbl, color="#000001")
    playtime_lbl.place(x=20, y=70, anchor=tkinter.W)

    # Label für das Release Date
    release_lbl = CTkLabel(stats, 
                        text="Release Date: "+str(reldate),
                        text_color="White",
                        bg_color="#000001",
                        font=("Arial", 22))
    pywinstyles.set_opacity(release_lbl, color="#000001")
    release_lbl.place(x=20, y=105, anchor=tkinter.W)

    # Label für den Metacrit Score
    metacrit_lbl = CTkLabel(stats, 
                            text="Metacrit Score: "+str(metascore),
                            text_color="White",
                            bg_color="#000001",
                            font=("Arial", 22))
    pywinstyles.set_opacity(metacrit_lbl, color="#000001")
    metacrit_lbl.place(x=20, y=140, anchor=tkinter.W)

    # Label für den Preis
    price_lbl = CTkLabel(stats, 
                        text="Price: "+str(price),
                        text_color="White",
                        bg_color="#000001",
                        font=("Arial", 22))
    pywinstyles.set_opacity(price_lbl, color="#000001")
    price_lbl.place(x=20, y=175, anchor=tkinter.W)

    # Label für Controller Support
    controller_lbl = CTkLabel(stats, 
                            text="Controller: "+str(controller),
                            text_color="White",
                            bg_color="#000001",
                            font=("Arial", 22))
    pywinstyles.set_opacity(controller_lbl, color="#000001")
    controller_lbl.place(x=20, y=210, anchor=tkinter.W)

    # Label für das Erforderliche Alter
    age_lbl = CTkLabel(stats, 
                    text="Required Age: "+str(reqage),
                    text_color="White",
                    bg_color="#000001",
                    font=("Arial", 22))
    pywinstyles.set_opacity(age_lbl, color="#000001")
    age_lbl.place(x=20, y=245, anchor=tkinter.W)

    # Label für die verfügbaren Plattformen
    platforms_lbl = CTkLabel(stats, 
                            text="Platforms: "+str(platforms),
                            text_color="White",
                            bg_color="#000001",
                            font=("Arial", 22),
                            wraplength=300)
    pywinstyles.set_opacity(platforms_lbl, color="#000001")
    try:
        if(len(platforms)>4):
            platforms_lbl.place(x=20, y=320, anchor=tkinter.W)
        else:
            platforms_lbl.place(x=20, y=280,anchor=tkinter.W)
    except TypeError:
        platforms_lbl.place(x=20,y=280,anchor=tkinter.W)
    #app.overrideredirect(True)            Remove Titlebar (mehr oder weniger)
    print(owned)
    if(owned):
        startGameBtn=CTkButton(master=stats, text="Start Game", command= lambda title=title:startGame(title), font=("Arial",22))
        startGameBtn.place(x=250,y=375, anchor=tkinter.W)
    elif owned == false:
        wishListBtn=CTkButton(master=stats, text="Add to Wishlist",font=("Arial",22),command= lambda title=title:addToWishlist(title,login)) #TODO: add command add to Wishlist
        wishListBtn.place(x=250, y=375, anchor=tkinter.W)    
    else:
        print("Nothing happens")

    app.mainloop()

def goback(app:CTk,details,titles,urls,login):
    from Tkinter_GUI.Spielcards import Spielcards #PFUSCH
    from Tkinter_GUI.Bibliothek import Bibliothek #pfusch 2?
    from Tkinter_GUI.Login import Login
    app.destroy()
    print("goback clicked")
    bibliothek = Bibliothek(2, True,urls,titles,details,login)
 