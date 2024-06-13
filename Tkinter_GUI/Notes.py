from Tkinter_GUI.Login import Login
from Tkinter_GUI.Sidebar import Sidebar
from tkinter import *
from customtkinter import *
from PIL import Image
import pywinstyles
from Tkinter_GUI.Login import Login

class Notes:
    def __init__(self, login:Login):
            
        set_appearance_mode("dark")
        self.app = CTk()
        self.app.title("Notes")
        self.steamid=login.getSteamId()
        self.connection=login.getConnection()

        self.app.iconbitmap(default="Design/Icon.png")
        self.app.iconphoto(False, PhotoImage(master=self.app,file="Design/Icon.png"))

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
        sidebar = Sidebar(self.app,login)

        self.inputText = CTkTextbox(master=self.app,
                                    width=940,
                                    height=680,
                                    fg_color="#250454",
                                    bg_color="#000001",
                                    font=("Arial", 20))
        pywinstyles.set_opacity(self.inputText, color="#000001")
        self.inputText.place(x=320, y=20)
        if(login.getNotes() is not None):
            print(login.getNotes())
            self.inputText.insert("0.0",login.getNotes())


        self.button = CTkButton(master=self.app,
                                text="Save",
                                width=50,
                                height=40,
                                fg_color="#3B0F82",
                                bg_color="#000001",
                                font=("Arial", 30),
                                command=self.setText)
        pywinstyles.set_opacity(self.button, color="#000001")
        self.button.place(x=1170, y=650)

        self.app.mainloop()
    
     # Funktion, um den text in die DB zu schreiben
    def setText(self):
        if(len(self.inputText.get('1.0', END))<499):
            with self.connection.cursor() as cur:
                sql="""UPDATE account SET notes=%s WHERE steamid=%s"""
                cur.execute(sql,(self.inputText.get('1.0',END),self.steamid,))
                self.connection.commit()
                #self.button.configure(color="green", text="Successfull) Mit Marko besprechen
        else:
            print("Error")
            #self.button.configure(color="red", text="Failed")