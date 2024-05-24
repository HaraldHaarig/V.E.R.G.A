import imp
import tkinter
import splashscreen_ctk as splash
import threading, time
from sympy import im, true
from Tkinter_GUI.Profil import Profil
import tkinter as tk
from API.SteamAPI import getSteamGamesbyID
from Tkinter_GUI.Startseite import Startpage
from PIL import ImageTk,Image


def show_loading_screen():      #das loading screen fenster wird geladen 
    root = tk.Tk()
    root.title("Loading...")

    # Center the window
    window_width = 600
    window_height = 480
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    image = Image.open("Design/Background.png")
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(root,image=photo)
    label.image = photo
    label.pack(expand=True)

    counter = 0

    while counter < 1000000000000000000:
  
        photo = tk.PhotoImage(file="Design/loading.gif", format="gif -index " + str(counter))
        label.config(image = photo)
        time.sleep(0.05)
        root.update()
        counter += 1
    
  
    return root




def mainapiload():          #einzelne funktionen für das ausführen vom laden der Api lore
    #getSteamGamesbyID("76561199015522225")
    
    print("mainapilore task completed")



def spielcardload():        #laden von api lore
    for i in range(10):
        print(f"spiecard task running... {i+1}")
        time.sleep(1)  # Simulate a time-consuming task
    print("spielcard task completed")



def startpageload():
    
    pass


def loadmainapi():
    # Create and show the loading screen
    loading_screen = show_loading_screen()

    # Run the background task in a separate thread
    thread = threading.Thread(target=mainapiload)
    thread.start()

    # Check if the background task is completed and close the loading screen
    def check_thread():
        if thread.is_alive():
            loading_screen.after(10, check_thread)
        else:
            loading_screen.destroy()

    # Start checking the thread
    check_thread()

    # Start the Tkinter main loop
    loading_screen.mainloop()




def loadspielcards():
    # Create and show the loading screen
    loading_screen = show_loading_screen()

    # Run the background task in a separate thread
    thread = threading.Thread(target=spielcardload)
    thread.start()

    # Check if the background task is completed and close the loading screen
    def check_thread():
        if thread.is_alive():
            loading_screen.after(10, check_thread)
        else:
            loading_screen.destroy()

    # Start checking the thread
    check_thread()

    # Start the Tkinter main loop
    loading_screen.mainloop()




def loadstartpage():
     # Create and show the loading screen
    loading_screen = show_loading_screen()

    # Run the background task in a separate thread
    thread = threading.Thread(target=startpageload)
    thread.start()

    # Check if the background task is completed and close the loading screen
    def check_thread():
        if thread.is_alive():
            loading_screen.after(10, check_thread)
        else:
            loading_screen.destroy()

    # Start checking the thread
    check_thread()

    # Start the Tkinter main loop
    loading_screen.mainloop()

