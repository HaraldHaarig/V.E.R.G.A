from ast import main
from textwrap import fill
import tkinter
import customtkinter
from numpy import pad
from panel import Row
from sympy import Array, expand, false, root
import tkinterweb


def createSpielcards(web : Array):
    
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")
    

    root_tk = customtkinter.CTk()  # create the Tk window like you normally do
    root_tk.geometry("1000x1000")
    root_tk.title("Spielcards")
    # mainframe = customtkinter.CTkFrame(master=root_tk,width=700,height=700)
    # mainframe.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    
    rows=0
    columns=1
    background= tkinterweb.HtmlFrame(root_tk,messages_enabled=false,vertical_scrollbar=false, height=1,width=1)
    for index in web:      
        
        background.load_website(index) #load a website
        print(rows, columns)
        root_tk.columnconfigure(1, weight=1)
        root_tk.rowconfigure(1, weight=1)
        background.grid(row=rows,column=columns)
        if columns % 2 == 0 and columns>0: 
            rows+=1
            columns=0
        columns+=1
        




    root_tk.mainloop()



