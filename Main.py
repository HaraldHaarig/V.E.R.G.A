from zmq import NULL
# from Tkinter_GUI.Bibliothek import Bibliothek
from Tkinter_GUI.Spielcards import Spielcards
from Tkinter_GUI.Bibliothek import Bibliothek
from DB_Service.Connection import Connection
from Tkinter_GUI.Login import Login
from Tkinter_GUI.Startseite import Startpage
from API.SteamAPI import getSteamProfile

#Nachher Bei Startseite, Bibliothek, Spielcards, Spielbeschreibung Login objekt mitgeben
# generate classes
# bibliothek = Bibliothek(False, None, None, None)

connection=Connection()
login = Login(connection)
startseite=Startpage(login)

