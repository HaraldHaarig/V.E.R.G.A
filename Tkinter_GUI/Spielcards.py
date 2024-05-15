from cProfile import label
from cgitb import text
from tkinter import *
import black
from customtkinter import *
from numpy import empty
from panel import Column, Row
from scipy import io
from PIL import Image
import urllib.request
import io
import ctypes
from ctypes import windll


class Spielcards: 

    def __init__(self, parent):
        print("Createt Spielcards")
        set_appearance_mode("dark")
        set_default_color_theme("blue")
        # h = windll.user32.FindWindowA(b'Shell_TrayWnd', None)
        # windll.user32.ShowWindow(h, 0) Taskbar disappears
        # windll.user32.ShowWindow(h, 9) Taskbar reappears

        # self.parent = CTk()  # create the CTk window like you normally do
        # self.parent


        self.parent = parent

        # user32 = ctypes.windll.user32
        # screenwidth = user32.GetSystemMetrics(0)
        # screenheight=user32.GetSystemMetrics(1)
        
        # x = int(((screenwidth/40)))
        # y = int(((screenheight/40)))
        
        self.frame= CTkScrollableFrame(self.parent, width=900,height=700)
        #self.frame.pack()
        self.frame.place(anchor='center', relx=0.5,rely=0.5)
        #self.scrollbar=Scrollbar(self.frame)
        
    def onLabelClicked(e):
        print("Placeholder Spielebeschreibung")
        print(e)


    def showCard(self, url, title,len):
        side_img_data = Image.open("Tkinter_GUI/Images/Background_frfr.png")
        side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
        with urllib.request.urlopen(url) as u:
             raw_data=u.read()
        
        img_data=Image.open(io.BytesIO(raw_data))
        img=CTkImage(dark_image=img_data, light_image=img_data, size=(180,120))
        label=CTkLabel(self.frame,image=img)
        label.bind("<Button-1>",lambda e:self.onLabelClicked())
        if(url=="https://cdn-icons-png.flaticon.com/512/16/16096.png"):
            label.configure(text=title)
        else:
            label.configure(text="")

        label.grid(row=len-(len%4),column=len % 4,pady=(0,10), padx=(0,10))
        print(url, title)
        


    def showallCards(self, url, title):
        count=0
        # self.parent.grid_rowconfigure(2,weight=1)
        # self.parent.columnconfigure(0, weight=1)
        
        self.frame.grid(row=1, column=1,pady=(1,1))

        for temp in url:
            self.showCard(temp,title[count],count)
            count+=1
        



    



