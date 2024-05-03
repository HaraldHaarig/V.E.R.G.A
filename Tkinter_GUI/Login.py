from customtkinter import *
from PIL import Image
from sympy import false

class Login:
    def __init__(self):
        self.app = CTk()
        self.app.geometry("600x480")
        self.app.resizable(0,0)

        side_img_data = Image.open("Tkinter_GUI/Images/Background_frfr.png")
        email_icon_data = Image.open("Tkinter_GUI/Images/Username-icon.png")
        password_icon_data = Image.open("Tkinter_GUI/Images/password-icon.png")

        side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
        email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20,20))
        password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17,17))

        CTkLabel(master=self.app, text="", image=side_img).pack(expand=True, side="left")

        self.frame = CTkFrame(master=self.app, width=300, height=480, fg_color="#222234")
        self.frame.pack_propagate(0)
        self.frame.pack(expand=True, side="right")

        CTkLabel(master=self.frame, text="Servus bei Verga!", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
        CTkLabel(master=self.frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

        CTkLabel(master=self.frame, text="  Username:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
        
        self.username=CTkEntry(master=self.frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
        self.username.pack(anchor="w", padx=(25, 0))

        CTkLabel(master=self.frame, text="  Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
        
        self.password=CTkEntry(master=self.frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*")
        self.password.pack(anchor="w", padx=(25, 0))

        CTkButton(master=self.frame, text="Login", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225,command=self.pressedLogin).pack(anchor="w", pady=(40, 0), padx=(25, 0))
        self.app.mainloop()

    def pressedLogin(self):
        username=self.username.get()
        password=self.password.get()
        self.checkAccount(username,password)

    def checkAccount(self,username,password):
        print("Enter db")
        found=0
        try:
            db=open('db.txt','r')
            
            for user in db:
                curr=user.split(";")
                if(curr[0]==username and curr[1].split("\n")[0]==password): #Voll Pfusch
                    print("Login granted on Account: "+username +" with password: "+password)
                    found=1
                    break
                elif(curr[0]==username and curr[1].split("\n")[0]!=password):
                    found=2
                    break

            if(found==0):
                db.close()
                db=open('db.txt','a')
                db.write(username+";"+password+"\n")
                print("Account Created with username: "+username+" and password: "+password)
            elif(found==2):
                print("Username already exists")

        except FileNotFoundError:
            db=open('db.txt','w')
            