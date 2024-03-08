from ast import main
from textwrap import fill
import tkinter
import customtkinter
from numpy import pad
from panel import Row
from pyparsing import White
from sympy import Array, expand, false, root
import tkinterweb
import webview
from PIL import ImageTk, Image


def createSpielcards(web : Array):
    
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")
    

    root_tk = customtkinter.CTk()  # create the Tk window like you normally do
    root_tk.geometry("1000x1000")
    root_tk.title("Spielcards")
     




    root_tk.mainloop()



