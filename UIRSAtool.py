from tkinter import *

class RSAInterface:
    def __init__(self):
        self.filePath = "/data/data.dat"
        self.mainWindow = Tk()
        self.mainWindow.geometry("800x800")
        self.mainWindow.title("RSA Encrypter-Decripter")


    def startGUI(self):

        self.mainWindow.mainloop()

GUI = RSAInterface()
GUI.startGUI()


