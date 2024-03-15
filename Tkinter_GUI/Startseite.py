import imp
import customtkinter
import PIL
from PIL import Image,ImageTk
from tkinter import Canvas, PhotoImage, Tk
from tkinter.ttk import Frame,Label,Style




app = customtkinter.CTk()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


image = PIL.Image.open("Design/Background.png")                         #Background festlegen           
background_image = customtkinter.CTkImage(image, size=(1280, 720))
bg_lbl = customtkinter.CTkLabel(app, text="", image=background_image)
bg_lbl.place(x=0, y=0)

app.title("Startpage")
app.geometry("1280x720")  #Gröse festlegen 


from screeninfo import get_monitors    #Die größen des Monitores einholen 
for data in get_monitors():
    print(str(data))
    

framesettings = customtkinter.CTkFrame(master=app, width=200, height=250,corner_radius=20, fg_color="#250454",bg_color="black")
framesettings.place(x=250, y=70)
#tkimg = PhotoImage(file="C:\Users\Tobias Hirzenberger\OneDrive\Desktop\3AHINF\SYP\V.E.R.G.A\Design\settings.png")
#Canvas.create_image(0,0,anchor="nw",image=tkimg)

framestore = customtkinter.CTkFrame(master=app, width=200, height=250,corner_radius=20, fg_color="#250454",bg_color="black")
framestore.place(x=540,y=70)

framemygames = customtkinter.CTkFrame(master=app, width=200, height=250,corner_radius=20, fg_color="#250454",bg_color="black")
framemygames.place(x=830,y=70)

framewishlist = customtkinter.CTkFrame(master=app, width=200, height=250,corner_radius=20, fg_color="#250454",bg_color="black")
framewishlist.place(x=830, y=370)

framenotes= customtkinter.CTkFrame(master=app, width=200, height=250,corner_radius=20, fg_color="#250454",bg_color="black")
framenotes.place(x=540, y=370)

framesupport = customtkinter.CTkFrame(master=app, width=200, height=250,corner_radius=20, fg_color="#250454",bg_color="black")
framesupport.place(x=250,y=370)


app.mainloop()
