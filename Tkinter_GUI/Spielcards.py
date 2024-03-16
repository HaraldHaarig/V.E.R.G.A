from tkinter import *
from customtkinter import *
from scipy import io
from PIL import Image
import urllib.request
import io


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
        

        

    def showCard(self, url, title):
        with urllib.request.urlopen(url) as u:
            raw_data=u.read()
        
        img_data=Image.open(io.BytesIO(raw_data))
        img=CTkImage(dark_image=img_data, light_image=img_data, size=(150, 200))
        label=CTkLabel(self.frame,image=img,text_color='red')
        label.configure(text=title)
        label.pack()
        
        self.root_tk.mainloop()





    



