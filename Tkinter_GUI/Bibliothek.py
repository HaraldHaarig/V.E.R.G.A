from customtkinter import* 
from PIL import Image

app = CTk()
app.geometry("1280x720")
app.resizable(0,0)

background = Image.open("Tkinter_GUI/Images/Background_frfr.png")
backgroundData = CTkImage(dark_image=background, light_image=background, size=(1280, 720))

CTkLabel(master=app, text="", image=backgroundData).pack(expand=True, side="left")

app.mainloop()
