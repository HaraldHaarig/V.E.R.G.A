import tkinter.messagebox
from turtle import bgcolor
from customtkinter import *
from PIL import Image
from numpy import empty
from sympy import false, true
import bcrypt


class Login:
    def __init__(self):
        self.app = CTk()
        self.app.geometry("600x480")
        self.app.resizable(0,0)

        side_img_data = Image.open("Tkinter_GUI/Images/Background_frfr.png")
        email_icon_data = Image.open("Tkinter_GUI/Images/Username-icon.png")
        password_icon_data = Image.open("Tkinter_GUI/Images/password-icon.png")
        steam_icon_data=Image.open("Tkinter_GUI/Images/steamIcon.png")

        side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
        email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20,20))
        password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17,17))
        steam_icon=CTkImage(dark_image=steam_icon_data,light_image=steam_icon_data, size=(20,20))

        CTkLabel(master=self.app, text="", image=side_img).pack(expand=True, side="left")

        self.frame = CTkFrame(master=self.app, width=300, height=480, fg_color="#222234")
        self.frame.pack_propagate(0)
        self.frame.pack(expand=True, side="right")

        CTkLabel(master=self.frame, text="Servus bei Verga!", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
        CTkLabel(master=self.frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

        CTkLabel(master=self.frame, text="  Username:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
        
        self.username=CTkEntry(master=self.frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
        self.username.configure(placeholder_text="myusername123", placeholder_text_color="gray")
        self.username.pack(anchor="w", padx=(25, 0))

        CTkLabel(master=self.frame, text="  Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
        
        self.password=CTkEntry(master=self.frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*")
        self.password.configure(placeholder_text="********", placeholder_text_color="gray")
        self.password.pack(anchor="w", padx=(25, 0))
        
        CTkLabel(master=self.frame, text="  (Only for SignIn) SteamID:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=steam_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))

        self.steamId=CTkEntry(master=self.frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
        self.steamId.configure(placeholder_text="76561197960359230", placeholder_text_color="gray")
        self.steamId.pack(anchor="w", padx=(25,0))

        CTkButton(master=self.frame, text="Login", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225,command=self.pressedLogin).pack(anchor="w", pady=(40, 0), padx=(25, 0))
        CTkButton(master=self.frame, text="Create V.E.R.G.A Account", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, command=self.pressedSignIn).pack(anchor="w", pady=(20, 0), padx=(25, 0))
        self.app.mainloop()

    def pressedSignIn(self):
        username=self.username.get()
        password=self.password.get()
        steam=self.steamId.get()
        salt=bcrypt.gensalt()
        
        if(len(username)==0):
           self.username.configure(fg_color="red")
        elif(len(password)==0):
            self.password.configure(fg_color="red")
        elif(len(steam)==0):
            self.steamId.configure(fg_color="red")
        else:
            self.checkSignIn(username,password,salt,steam)

    def checkSignIn(self,username,password,salt,steamid):
        temp=password.encode('utf-8')
        finalpassword=bcrypt.hashpw(temp,salt)
        print("Enter SingIn")
        exists=false
        try:
            db=open('db.txt','r')

            for user in db:
                if(username==user.split(";")[0]):
                    exists=true
                    break

            if(exists):
                print("Username already exists")
            else:
                db.close()
                db=open('db.txt','a')
                self.username.configure(fg_color="green")
                self.password.configure(fg_color="green")
                self.steamId.configure(fg_color="green")
                db.write(username+";"+str(finalpassword.decode("utf-8"))+";"+steamid+"\n")

        except FileNotFoundError:
            db=open('db.txt','w')





    def pressedLogin(self):
        username=self.username.get()
        password=self.password.get()
        
        if(len(username)==0):
            self.username.configure(fg_color="red")
        elif(len(password)==0):
            self.password.configure(fg_color="red")
        else:
            self.checkLogin(username,password)



    def checkLogin(self,username,password):
        print("Enter db")
        isempty=true
        try:
            db=open('db.txt','r')
            
            for user in db:
                isempty=false
                curr=user.split(";")
                encoded=password.encode("utf-8")
                hashed=bytes(curr[1],"utf-8")
                
                if(curr[0]==username and bcrypt.checkpw(encoded,hashed)): #Voll Pfusch
                    self.username.configure(fg_color="green")
                    self.password.configure(fg_color="green")
                    print("Login granted on Account: "+username)
                    break
                elif(curr[0]==username and not bcrypt.checkpw(encoded,hashed)):
                    print("Username exists but password is wrong")
                    break            
                else:
                    print("Your User does not exists. Pls go to Sign in")
            if(isempty):
                print("Empty db go to Sign In")
        except FileNotFoundError:
            db=open('db.txt','w')
            