import tkinter
import customtkinter
from tkinterweb import HtmlFrame

def createSpielcards(count,web):
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    root_tk = customtkinter.CTk()  # create the Tk window like you normally do
    root_tk.geometry("1000x1000")
    root_tk.title("Spielcards")

    for i in range(count):
        frame = customtkinter.CTkFrame(master=root_tk,width=400,height=400)
        frame.pack(padx=20,pady=20)

        background= HtmlFrame(frame)
        background.load_website(web[i]) #load a website
        background.pack(fill="both", expand=True)















    root_tk.mainloop()



