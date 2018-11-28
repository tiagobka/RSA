from tkinter import *
from tkinter import filedialog
import RSA

class RSAInterface:
    def __init__(self):
        self.filePath = "/data/data.dat"
        self.mainWindow = Tk()
        self.mainWindow.geometry("800x800")
        self.mainWindow.title("RSA Encrypter-Decripter")


    def startGUI(self):
        #self.mainWindow.fileName = filedialog.askopenfilename(initialdir = "./keys",filetypes = (("Text Files", "*.txt"), ("All Files", "*.*")), title = "Select key file")
        #print (self.mainWindow.fileName)
        Label(self.mainWindow, text="Input data (Must be an integer):").grid(row = 0, column = 1)
        Button(self.mainWindow, text = "Encrypt ->").grid(row=2, column = 2)
        Button(self.mainWindow, text="<- Decrypt").grid(row=3, column=2)
        Label(self.mainWindow, text="Output data (Must be an integer):").grid(row=0, column=7)
        L = Text(self.mainWindow, height = 10, width=30)
        R = Text(self.mainWindow, height = 10, width=30)
        L.grid(row = 2, column = 1)
        R.grid(row = 2, column =7)


        self.mainWindow.mainloop()
    def encryptFunction(self):
        pass

GUI = RSAInterface()
GUI.startGUI()


