import tkinter
import customtkinter
from sympy import Array
from tkinterweb import HtmlFrame

def createSpielcards(count,web : Array):
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    root_tk = customtkinter.CTk()  # create the Tk window like you normally do
    root_tk.geometry("1000x1000")
    root_tk.title("Spielcards")
    counter=0

    for index in web:
        frame = customtkinter.CTkFrame(master=root_tk,width=50,height=50)
        frame.pack(padx=20,pady=20)

        background= HtmlFrame(frame)
        background.load_website(index) #load a website
        background.pack(fill="both", expand=True)
        counter+=1














    root_tk.mainloop()



