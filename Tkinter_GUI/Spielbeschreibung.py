import tkinter
from customtkinter import *
from PIL import Image

set_appearance_mode("dark")

app = CTk()
app.geometry("1280x720")

# Background Image
image = Image.open("Design/Background.png")
background_image = CTkImage(image, size=(1280, 720))

bg_lbl = CTkLabel(app, text="", image = background_image)
bg_lbl.place(x = 0, y = 0)

# Experimenteller Frame
frame = CTkFrame(master=app,
                 width=200,
                 height=200,
                 corner_radius=20,
                 fg_color="#7728F5")
frame.pack(padx=20, pady=20)

app.title("V.E.R.G.A GameLauncher")
# app.overrideredirect(True)            Remove Titlebar
app.mainloop()