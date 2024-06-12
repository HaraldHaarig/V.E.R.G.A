# import imp
# import tkinter
# #import splashscreen_ctk as splash
# import threading, time
# from sympy import im, true
# from Tkinter_GUI.Profil import Profil
# import tkinter as tk
# from API.SteamAPI import getSteamGamesbyID
# from PIL import ImageTk,Image
# from itertools import count, cycle

# class Loadingscreen:
#     def show_loading_screen(self):      #das loading screen fenster wird geladen 
#         self.root = tk.Tk()
#         self.root.title("Loading...")

#         # Center the window
#         window_width = 600
#         window_height = 480
#         screen_width = self.root.winfo_screenwidth()
#         screen_height = self.root.winfo_screenheight()
#         position_top = int(screen_height / 2 - window_height / 2)
#         position_right = int(screen_width / 2 - window_width / 2)
#         self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

#         image = Image.open("Design/Background.png")
#         photo = ImageTk.PhotoImage(image)

#         self.label = tk.Label(self.root,image=photo)
#         self.label.image = photo
#         self.label.pack(expand=True)

        
#         return self.root

#     def mainapiload(self):          #einzelne funktionen für das ausführen vom laden der Api lore
#         #getSteamGamesbyID("76561199015522225")
        
#         print("mainapilore task completed")



#     def spielcardload(self):        #laden von api lore
#         for i in range(10):
#             print(f"spiecard task running... {i+1}")
#             time.sleep(1)  # Simulate a time-consuming task
#         print("spielcard task completed")


#     def startpageload(self):
#         from Tkinter_GUI.Startseite import Startpage
#         Startpage()






        
#     def loadmainapi(self):
#         # Create and show the loading screen
#         loading_screen = self.show_loading_screen()

#         # Run the background task in a separate thread
#         thread = threading.Thread(target=self.mainapiload)
#         thread.start()

#         # Check if the background task is completed and close the loading screen
#         def check_thread(self):
#             if thread.is_alive(self):
#                 loading_screen.after(10, check_thread)
#             else:
#                 loading_screen.destroy()

#         # Start checking the thread
#         check_thread()

#         # Start the Tkinter main loop
#         loading_screen.mainloop()






#     def loadspielcards(self):
#         # Create and show the loading screen
#         loading_screen = self.show_loading_screen()

#         # Run the background task in a separate thread
#         thread = threading.Thread(target=self.spielcardload)
#         thread.start()

#         # Check if the background task is completed and close the loading screen
#         def check_thread():
#             if thread.is_alive():
#                 loading_screen.after(10, check_thread)
#             else:
#                 loading_screen.destroy()

#         # Start checking the thread
#         check_thread()

#         # Start the Tkinter main loop
#         loading_screen.mainloop()








#     def loadstartpage(self):
#         # Create and show the loading screen
#         loading_screen = self.show_loading_screen()

#         # Run the background task in a separate thread
#         thread = threading.Thread(target=self.startpageload)
#         thread.start()

#         # Check if the background task is completed and close the loading screen
#         def check_thread():
#             if thread.is_alive():
#                 loading_screen.after(10, check_thread)
#             else:
#                 loading_screen.destroy()

#         # Start checking the thread
#         check_thread()

#         # Start the Tkinter main loop
#         loading_screen.mainloop()




import customtkinter as ctk
import threading
import multiprocessing
import time
from PIL import Image, ImageTk
from Tkinter_GUI.Startseite import Startpage


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CustomTkinter Application")

        # Start with the loading screen
        self.loading_screen = LoadingScreen(self)
        self.loading_screen.pack(fill="both", expand=True)

        # Start the background task
        self.loading_screen.start_background_task()

    def switch_to_main_screen(self):
        self.loading_screen.pack_forget()
        main_screen = Startpage(self)
        main_screen.pack(fill="both", expand=True)



class LoadingScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.label = ctk.CTkLabel(self, text="Loading, please wait...", font=("Helvetica", 16))
        self.label.pack(pady=10)

        # Load an image and display it in the label
        self.loading_image = Image.open("loading_image.png")  # Replace with your image path
        self.photo = ImageTk.PhotoImage(self.loading_image)
        self.image_label = ctk.CTkLabel(self, image=self.photo)
        self.image_label.pack(pady=10)

    def start_background_task(self):
        self.thread = threading.Thread(target=self.background_task)
        self.thread.start()
        self.check_thread()

    def background_task(self):
        process = multiprocessing.Process(target=self.long_running_task)
        process.start()
        process.join()  # Wait for the process to finish

    def long_running_task(self):
        for i in range(5):
            print(f"Background task running... {i+1}")
            time.sleep(1)
        print("Background task completed")

    def check_thread(self):
        if self.thread.is_alive():
            self.after(100, self.check_thread)
        else:
            self.master.switch_to_main_screen()



if __name__ == "__main__":
    app = App()
    app.mainloop()
