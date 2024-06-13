import threading, time
import tkinter as tk
from PIL import ImageTk,Image
from customtkinter import *
import pywinstyles


class Loadingscreen:
    def show_loading_screen(self):
        self.root = tk.Tk()
        self.root.title("Loading...")

        # Center the window
        window_width = 600
        window_height = 480
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        imagebg = Image.open("Design/Background.png")
        photo = ImageTk.PhotoImage(imagebg)

        self.root.overrideredirect(True)


        self.label = tk.Label(self.root, image=photo)
        self.label.image = photo
        self.label.pack(expand=True)




        gif_label = CTkLabel(self.root, image="",bg_color="#000001", text="")
        pywinstyles.set_opacity(gif_label,color="#000001")
        gif_label.place(x=250, y=160)  # place the gif_label
        
        text_label = CTkLabel(self.root, image="", bg_color="#000001", text="API fladert...",font=("Arial",20))
        pywinstyles.set_opacity(text_label,color="#000001")
        text_label.place(x=250, y=280)
       
        
    
        file = "Design/loading.gif"
        gif = Image.open(file)
        


        desired_width = 100         # Change to your desired width
        desired_height = 100        # Change to your desired height



        photoimage_objects = []
        for i in range(gif.n_frames):
            gif.seek(i)

            # Convert the frame to RGBA (handles transparency if needed)
            pil_image = gif.convert('RGBA')

            # Create a new image with transparency (white background)
            transparent_image = Image.new('RGBA', pil_image.size, (255, 255, 255, 0))

            # Paste the frame onto the transparent background
            transparent_image.paste(pil_image, (0, 0), pil_image)

            # Resize the image
            resized_image = transparent_image.resize((desired_width, desired_height), Image.LANCZOS)

            # Convert the resized PIL image to a PhotoImage object
            obj = ImageTk.PhotoImage(resized_image)

            # Append the PhotoImage object to the list
            photoimage_objects.append(obj)

        def animation(current_frame=0):
            global loop
            image = photoimage_objects[current_frame]

            gif_label.configure(image=image)
            
            
            current_frame = (current_frame + 1) % len(photoimage_objects)

            loop = self.root.after(50, lambda: animation(current_frame))

        animation(current_frame=0)

        return self.root






    def mainapiload(self):
        print("mainapilore task completed")             #Hier bitte eric die lade api klauen einbinden danki <3 UWU




    def spielcardload(self):
        for i in range(10):
            print(f"spiecard task running... {i+1}")        #Hier bitte eric die lade api klauen einbinden danki <3 UWU
            time.sleep(1)
        print("spielcard task completed")



    def profileload(self):
        pass                                        #Hier bitte eric die lade api klauen einbinden danki <3 UWU










    def loadmainapi(self,function):
        loading_screen = self.show_loading_screen()

        thread = threading.Thread(target=function)
        thread.start()

        def check_thread():
            if thread.is_alive():
                loading_screen.after(10, check_thread)
            else:
                loading_screen.destroy()

        check_thread()
        loading_screen.mainloop()







    def loadspielcards(self):
        loading_screen = self.show_loading_screen()


        thread = threading.Thread(target=self.spielcardload)
        thread.start()

        def check_thread():
            if thread.is_alive():
                loading_screen.after(10, check_thread)
            else:
                loading_screen.destroy()

        check_thread()
        loading_screen.mainloop()






    def loadprofile(self):
        loading_screen = self.show_loading_screen()
        

        thread = threading.Thread(target=self.profileload)
        thread.start()

        def check_thread():
            if thread.is_alive():
                loading_screen.after(10, check_thread)
            else:
                loading_screen.destroy()

        check_thread()
        loading_screen.mainloop()




