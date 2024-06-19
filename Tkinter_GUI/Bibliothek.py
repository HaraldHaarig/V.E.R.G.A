from customtkinter import* 
import tkinter as tk
from Tkinter_GUI.Sidebar import Sidebar
from Tkinter_GUI.Spielcards import Spielcards
from API.SteamAPI import getSteamGamesbyID
from API.GameAPI import getAllGames
from tkinter import *
from Tkinter_GUI.Login import Login
from DB_Service.Wishlist import getWishlist
from LoadingScreen import Loadingscreen


class Bibliothek:
    def __init__(self, open, bool, urls,titles,details,login:Login):
        self.root_tk = CTk()
        self.opened = bool
        self.open = open

        self.root_tk.iconbitmap(default="Design/Icon.png")
        self.root_tk.iconphoto(False, PhotoImage(master=self.root_tk,file="Design/Icon.png"))

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
        self.Sidebar = Sidebar(self.root_tk,login)

        self.spielcards = Spielcards(self.mainframe, self.root_tk,login)

        #self.loading = Loadingscreen()

        if self.opened == False and self.open == 1:
            print("Open owned Games first time")
            self.showAllOwnedGamesCards(login)
        elif self.open == True and self.open == 1:
            print("Open owned Games after first time")
            self.callshowallCards(urls,titles,details)
        if self.opened == False and self.open == 2:
            print("Open all Games first time")
            self.showAllGameCards()
        elif self.opened == True and self.open == 2:
            print("Open owned Games after first time")
            self.callshowallCards(urls,titles,details)
        if self.opened == False and self.open == 3:
            print("Open Wishlisted Games first time")
            self.showWishlistGames(login)
        elif self.opened == True and self.open == 3:
            print("Open Wishlisted Games after first time")    
            self.callShowWishlistGames(urls,titles,details)
        
        self.root_tk.mainloop()

    def showAllOwnedGamesCards(self,login:Login):
        print("showCards opened because bool is False")

        #fetching the games
        url,title,details=getSteamGamesbyID(login.getSteamId())
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

    def showWishlistGames(self,login):
        print("showCards opened because bool is False")

        #fetching the games
        url,title,details=getWishlist(login)
        count=0
        for s in url:
            if s == 0:
                url[count]="https://cdn-icons-png.flaticon.com/512/16/16096.png"
            count += 1
        #call spielcards Function with the fetched data    
        self.spielcards.showALLWishlistGames(url,title,details)

    def callShowWishlistGames(self, urls, titles, details):
        self.spielcards.showALLWishlistGames(urls,titles,details)
