from customtkinter import* 
#from tkinter import*
import tkinter as tk
from PIL import Image
from ctypes import windll
import ctypes

from pydantic import PositiveInt
from Tkinter_GUI.Spielcards import Spielcards
from API.SteamAPI import getSteamGamesbyID



class Bibliothek:
    def __init__(self, bool, urls,titles,details):
        self.root_tk = CTk()
        self.opened = bool
        # user32 = ctypes.windll.user32
        # screenwidth = user32.GetSystemMetrics(0)
        # screenheight=user32.GetSystemMetrics(1)
        
        # x = int(((screenwidth/40)))
        # y = int(((screenheight/40)))

        #self.root_tk.geometry("%dx%d+%d+%d" % (int(screenwidth),int(screenheight),int(x),int(y)))
        widh_of_window = 1280
        height_of_window = 720
        scree_widh = self.root_tk.winfo_screenwidth()
        screen_height =self.root_tk.winfo_screenheight()
        x_cordinate = (scree_widh/2)-(widh_of_window/2)
        y_cordinate = (screen_height/2)-(height_of_window/2)
        self.root_tk.geometry("%dx%d+%d+%d" %(widh_of_window,height_of_window,x_cordinate,y_cordinate))
        
        self.root_tk.title("Bibliothek")

        #Right side of the libary
        self.mainframe= CTkFrame(self.root_tk, width=920,height=720, fg_color="#555555") #originalfarbe #222234
        self.mainframe.place(anchor=tk.E, relx=1,rely=0.5)

        #Left side of the library
        self.leftframe= CTkFrame(self.root_tk, width=340,height=720, fg_color="#ffffff") 
        self.leftframe.place(anchor=tk.W, relx=0.0,rely=0.5)

        self.spielcards = Spielcards(self.mainframe, self.root_tk)

        if self.opened == False:
            print("test already opened false")
            self.showCards()
        else:
            print("callShowallCards because true")
            self.callshowallCards(urls,titles,details)

        # else:
        #     self.callshowallCards()

        # url,title,details=getSteamGamesbyID("76561199015522225")

        # count=0
        # for s in url:
        #     if s == 0:
        #         url[count]="https://cdn-icons-png.flaticon.com/512/16/16096.png"
        #     count+=1
        # self.spielcards.showallCards(url,title,details)
        # self.spielcards.showCard(url[0],title[0], count)

        #self.showCards()
        
        self.root_tk.mainloop()

    def showCards(self):
        print("showCards opened because bool is False")

        url,title,details=getSteamGamesbyID("76561199015522225")
        count=0
        for s in url:
            if s == 0:
                url[count]="https://cdn-icons-png.flaticon.com/512/16/16096.png"
            count += 1
        self.spielcards.showallCards(url,title,details)
        #self.spielcards.showCard(url[0],title[0], count)
    
    def callshowallCards(self, urls,titles,details):
        print("callshowallCards called becuase bool is True")
        self.spielcards.showallCards(urls,titles,details)

        