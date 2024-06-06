from Tkinter_GUI.Sidebar import Sidebar
import tkinter
from customtkinter import *
from PIL import Image
import pywinstyles

class Notes:
    def __init__(self):
        set_appearance_mode("dark")
        self.app = CTk()
        self.app.title("V.E.R.G.A GameLauncher")

        # Zuständig für das zentrieren des Fensters in der Mitte des Monitors
        widh_of_window = 1280
        height_of_window = 720
        scree_widh = self.app.winfo_screenwidth()
        screen_height = self.app.winfo_screenheight()
        x_cordinate = (scree_widh/2)-(widh_of_window/2)
        y_cordinate = (screen_height/2)-(height_of_window/2)
        self.app.geometry("%dx%d+%d+%d" %(widh_of_window,height_of_window,x_cordinate,y_cordinate))

        # Background Image
        image = Image.open("Design/Background.png")
        background_image = CTkImage(image, size=(1280, 720))

        bg_lbl = CTkLabel(self.app, text="", image = background_image)
        bg_lbl.place(x = 0, y = 0)

        # Sidebar wird eingefügt
        sidebar = Sidebar(self.app)

        self.app.mainloop()