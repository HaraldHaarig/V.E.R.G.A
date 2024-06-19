from DB_Service.Connection import Connection
from Tkinter_GUI.Login import Login
from Tkinter_GUI.Startseite import Startpage
#from LoadingScreen import Loadingscreen

# loadingscreen = Loadingscreen()
# loadingscreen.loadspielcards()



connection=Connection()
login = Login(connection)
startseite=Startpage(login)

