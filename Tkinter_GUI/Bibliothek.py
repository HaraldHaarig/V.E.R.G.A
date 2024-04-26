from customtkinter import* 
#from tkinter import*
import tkinter as tk
from PIL import Image
from ctypes import windll
import ctypes
from Tkinter_GUI.Spielcards import Spielcards
from API.SteamAPI import getSteamGamesbyID



class Bibliothek:

    def __init__(self):
        self.root_tk = CTk()
        user32 = ctypes.windll.user32
        screenwidth = user32.GetSystemMetrics(0)
        screenheight=user32.GetSystemMetrics(1)
        
        x = int(((screenwidth/40)))
        y = int(((screenheight/40)))

        self.root_tk.geometry("%dx%d+%d+%d" % (int(screenwidth),int(screenheight),int(x),int(y)))
        
        self.root_tk.title("Bibliothek")

        #Pictures
        leftside_img_data = Image.open("Tkinter_GUI/Images/Background_frfr.png")
        background_img_data = Image.open("Tkinter_GUI/Images/Background_frfr.png")
        #hier weiter machen

        #Right side of the libary
        self.mainframe= CTkFrame(self.root_tk, width=screenwidth,height=screenheight, fg_color="#222234") 
        #self.mainframe.pack()
        self.mainframe.place(anchor=tk.E, relx=1.0,rely=0.5)
        self.scrollbar = tk.Scrollbar(self.mainframe, orient=tk.VERTICAL)

        #Left side of the library
        self.leftframe= CTkFrame(self.root_tk, width=screenwidth-1620,height=screenheight, fg_color="#ffffff") 
        #self.leftframe.pack()
        self.leftframe.place(anchor=tk.W, relx=0.0,rely=0.5)

        self.spielcards = Spielcards(self.mainframe)

        url,title=getSteamGamesbyID("76561199015522225")


        # print(len(url), len(title) )
        count=0
        for s in url:
            if s == 0:
                url[count]="https://cdn-icons-png.flaticon.com/512/16/16096.png"
            count+=1
        self.spielcards.showallCards(url,title)
        self.spielcards.showCard(url[0],title[0], count)

        print("Verga")

        #self.showCards()
        
        self.root_tk.mainloop()

    def showCards(self):
        print("hallo")
        url,title=getSteamGamesbyID("76561199015522225")
        count=0
        for s in url:
            if s == 0:
                url[count]="https://cdn-icons-png.flaticon.com/512/16/16096.png"
                count+=1
        self.spielcards.showallCards(url,title, count)

        
