from tkinter import *
from customtkinter import *
from scipy import io
from PIL import Image
import urllib.request
import io

from sympy import false, true
from Tkinter_GUI.Spielbeschreibung import spielbeschreibung_main
from Tkinter_GUI.Login import Login

class Spielcards: 

    def __init__(self, parent, bibliothek_root,login:Login):
        print("Createt Spielcards")
        set_appearance_mode("dark")
        set_default_color_theme("blue")
        self.owned=false
        self.login=login
        
        self.bibliothek_root = bibliothek_root

        self.parent = parent
        self.images = []
        
        self.frame= CTkScrollableFrame(self.parent, width=940,height=720)
        self.frame.place(anchor='center', relx=0.5,rely=0.5)

        # Background Image
        # image = Image.open("Design/Background.png")
        # background_image = CTkImage(image, size=(1280, 10000))
        # #Background Image Label
        # bg_lbl = CTkLabel(self.frame, text="", image = background_image)
        # bg_lbl.place(x = 0, y = 0)
        
    def onLabelClicked(self,title,details,restore_detail,restore_titles,restore_urls):
        self.bibliothek_root.destroy()
        print(self.owned)
        try:
            x = len(details)
            print(x)
        except:
            spielbeschreibung_main(title,"N/A", "N/A", "N/A", "N/A", 0, "N/A", "N/A", "N/A", restore_detail,restore_titles,restore_urls,self.owned,self.login)

        if(x == 9):
            spielbeschreibung_main(title,details[2],(details[1]/60),details[5],details[6],details[0],details[4],details[3],details[7],restore_detail,restore_titles,restore_urls,self.owned,self.login)
        else:
            spielbeschreibung_main(title,details[4], "N/A", details[0], details[1], 0, details[5], details[3], details[2], restore_detail,restore_titles,restore_urls,self.owned,self.login)


    def showCard(self, url, title,len,details,spielbeschreibung_details,spielbeschreibung_title,spielbeschreibung_url):
        side_img_data = Image.open("Tkinter_GUI/Images/Background_frfr.png")
        side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
        with urllib.request.urlopen(url) as u:
             raw_data=u.read()
        
        img_data=Image.open(io.BytesIO(raw_data))
        img=CTkImage(dark_image=img_data, light_image=img_data, size=(180,120))
        self.images.append(img)
        
        label=CTkLabel(self.frame,image=img)
        label.bind("<Button-1>",lambda e:self.onLabelClicked(title,details,spielbeschreibung_details,spielbeschreibung_title,spielbeschreibung_url))
        if(url=="https://cdn-icons-png.flaticon.com/512/16/16096.png"):
            label.configure(text=title)
        else:
            label.configure(text="")

        label.grid(row=len-(len%4),column=len % 4,pady=(0,10), padx=(0,10))
        print(url, title)
        

 
    def showAllOwnedGames(self, url, title,details):
        count=0
        self.frame.grid(row=1, column=1,pady=(1,1))
        self.owned=true 

        for tempurl in url:
            self.showCard(tempurl,title[count],count,details[count],details,title,url)
            count+=1

    def showGames(self, url, title,details):
        count=0
        self.frame.grid(row=1, column=1,pady=(1,1))
        self.owned=false 

        for temp in url:
            self.showCard(temp,title[count],count,details[count],details,title,url)
            count+=1
        

    def showALLWishlistGames(self, url, title,details):
        count=0
        self.frame.grid(row=1, column=1,pady=(1,1))
        self.owned=None

        for temp in url:
            self.showCard(temp,title[count],count,details[count],details,title,url)
            count+=1    



