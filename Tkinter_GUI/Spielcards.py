from tkinter import *
from customtkinter import *
from panel import Column, Row
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
        self.frame= CTkFrame(self.root_tk, width=800,height=800)
        self.frame.pack()
        self.frame.place(anchor='center', relx=0.5,rely=0.5)
        self.scrollbar=Scrollbar(self.root_tk)
        
        

        

    def showCard(self, url, title,len):
        with urllib.request.urlopen(url) as u:
            raw_data=u.read()
        
        img_data=Image.open(io.BytesIO(raw_data))
        img=CTkImage(dark_image=img_data, light_image=img_data, size=(70, 70))
        label=CTkLabel(self.frame,image=img,text_color='red')
        label.configure(text=title)
        label.grid(row=len,column=0,pady=(0,10))
        print(url, title)
        
        
        

    def showallCards(self, url, title):
        count=0
        self.root_tk.grid_rowconfigure(2,weight=1)
        self.root_tk.columnconfigure(0, weight=1)
        
        self.frame.grid(row=1, column=1,pady=(1,1))

        for temp in url:
            self.showCard(temp,title[count],(len(url)-count))
            count+=1
        
        self.root_tk.mainloop()



    



