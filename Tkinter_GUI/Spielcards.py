from ast import main
from textwrap import fill
import tkinter
from tkinter.ttk import Label
from typing import Self
from customtkinter import *
from numpy import pad
from panel import Row
from pyparsing import White
from sympy import Array, expand, false, root
import tkinterweb
import webview
from PIL import ImageTk, Image


class Spielcards: 

    def __init__(self):
        print("Createt Spielcards")
        set_appearance_mode("dark")
        set_default_color_theme("blue")
        

        self.root_tk = CTk()  # create the Tk window like you normally do
        self.root_tk.geometry("1000x1000")
        self.root_tk.title("Spielcards")
        self.frame= CTkFrame(self.root_tk, width=200,height=200)
        self.frame.pack()
        self.frame.place(anchor='center', relx=0.5,rely=0.5)
        img_data=Image.open("Design/Background.png")
        img=CTkImage(dark_image=img_data, light_image=img_data, size=(200, 200))
        label=CTkLabel(self.frame,image=img)
        label.pack()

    def showCard(self):
        
        
        self.root_tk.mainloop()





    



