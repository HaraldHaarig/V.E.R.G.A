import customtkinter
from PIL import Image
import PIL



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
    






app.mainloop()
