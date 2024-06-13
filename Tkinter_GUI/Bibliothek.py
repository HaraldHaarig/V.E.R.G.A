from customtkinter import* 
#from tkinter import*
import tkinter as tk
from PIL import Image
from ctypes import windll
import ctypes
from pydantic import PositiveInt
from Tkinter_GUI.Sidebar import Sidebar
from Tkinter_GUI.Spielcards import Spielcards
from API.SteamAPI import getSteamGamesbyID
from API.GameAPI import getAllGames
from tkinter import *


class Bibliothek:
    def __init__(self, open, bool, urls,titles,details):
        self.root_tk = CTk()
        self.opened = bool
        self.open = open

        self.root_tk.iconbitmap(default="Design/Icon.png")
        self.root_tk.iconphoto(False, PhotoImage(master=self.root_tk,file="Design/Icon.png"))

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
        self.mainframe= CTkFrame(self.root_tk, width=940,height=720, fg_color="#555555") #originalfarbe #222234
        self.mainframe.place(anchor=tk.E, relx=1,rely=0.5)

        #Left side of the library
        # self.leftframe= CTkFrame(self.root_tk, width=300,height=720, fg_color="#ffffff") 
        # self.leftframe.place(anchor=tk.W, relx=0.0,rely=0.5)
        self.Sidebar = Sidebar(self.root_tk)

        self.spielcards = Spielcards(self.mainframe, self.root_tk)

        if self.opened == False and self.open == 1:
            print("Open owned Games first time")
            self.showAllOwnedGamesCards()
        elif self.open == True and self.open == 1:
            print("Open owned Games after first time")
            self.callshowallCards(urls,titles,details)
        if self.opened == False and self.open == 2:
            print("Open all Games first time")
            self.showAllGameCards()
        elif self.opened == True and self.open == 2:
            print("Open owned Games after first time")
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

    def showAllOwnedGamesCards(self):
        print("showCards opened because bool is False")

        #fetching the games
        url,title,details=getSteamGamesbyID("76561199015522225")
        count=0
        for s in url:
            if s == 0:
                url[count]="https://cdn-icons-png.flaticon.com/512/16/16096.png"
            count += 1
        #call spielcards Function with the fetched data    
        self.spielcards.showAllOwnedGames(url,title,details)
    
    #function to show the owned Games when data already got fetched
    def callshowallCards(self, urls,titles,details):
        print("callshowallCards called becuase bool is True")
        self.spielcards.showAllOwnedGames(urls,titles,details)

    def showAllGameCards(self):
        title, img, details = getAllGames(1)
        count = 0
        for s in img:
            if s == 0:
                img[count]="https://cdn-icons-png.flaticon.com/512/16/16096.png"
            count += 1
        self.spielcards.showGames(img, title, details)

    def callShowAllGames(self, urls, titles, details):
        self.spielcards.showGames(self, urls, titles, details)


        
