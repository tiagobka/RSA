from tkinter import *
from tkinter import filedialog
from RSA import RSA


class RSAInterface:
    def __init__(self, keySize:int = 1024):
        self.filePath = "/data/data.dat"
        self.mainWindow = Tk()
        self.mainWindow.geometry("630x500")
        #self.mainWindow.configure(background = "black")
        self.mainWindow.title("RSA Encrypter-Decrypter")
        self.mainWindow.grid_columnconfigure(0, minsize=10)
        self.mainWindow.grid_rowconfigure(10, minsize=20)
        self.keySize = keySize
        #Instantiate RSA class, Key will be 1024 by default
        self.rsa = RSA(self.keySize)
        self.option = IntVar(0)

    def setKeySize (self,keySize:int):
        self.keySize = keySize
        self.rsa.setKeySize(keySize)

    def generateKeys(self):
        try:
            x = int(self.mainWindow.grid_slaves(0, 2)[0].get())
            self.setKeySize(x)
            #
            #if (self.msg3.winfo_ismapped()):
             #   self.msg3.grid_forget()

            if 2 <= x <= 2048:


                self.rsa.RSA_Algorithm()  # creates private and public keys

                self.msg3['text'] = "Keys were created successfully!"
                self.msg3['foreground'] = "green"
                self.msg3.grid(row=0, column=4)
                self.mainWindow.grid_slaves(3, 3)[0].config(state = NORMAL)
                self.mainWindow.grid_slaves(4, 3)[0].config(state=NORMAL)
            else:
                self.msg3['text'] = "Key must be an integer between 2 and 2048"
                self.msg3.grid(row=0, column=4)
        except:
            self.msg3['text']= "Key must be an integer"
            self.msg3.grid(row=0,column = 4)


    def startGUI(self):
        self.mainWindow.grid_columnconfigure(0,minsize = 10)

        Label(self.mainWindow, text= "Key Size:").grid(row=0, column =1, sticky=E)
        keySize = Entry(self.mainWindow)
        keySize.insert(END,1024)
        keySize.grid(row=0, column = 2)
        Button(self.mainWindow, text = "Generate Key", command= self.generateKeys).grid(row = 0,column = 3)


        Label(self.mainWindow, text="Input data:").grid(row = 1, column = 1, sticky=W)
        Label(self.mainWindow, text="Output data:").grid(row=1, column=4, sticky=W)
        self.L = Text(self.mainWindow, height = 10, width=30)
        self.R = Text(self.mainWindow, height = 10, width=30)
        self.L.grid(row = 3, column = 1, rowspan = 7, columnspan = 2, sticky = W)
        self.R.grid(row = 3, column =4, rowspan = 7, columnspan = 2)

        Button(self.mainWindow, text="Encrypt ->", command= self.encryptFunction, state =DISABLED).grid(row=3, column=3)
        Button(self.mainWindow, text="<- Decrypt", command=self.decryptFunction, state = DISABLED).grid(row=4, column=3)

        Button(self.mainWindow, text = "Save private key to File", command = self.savePrKeyToFile, width = 18). grid(row = 11, column = 1,sticky=W)
        Button(self.mainWindow, text="get private key from File", command = self.getPrKeyFromFile, width = 18).grid(row=12, column=1,sticky=W)
        Button(self.mainWindow, text="Save public key to File", command=self.savePubKeyToFile, width = 18).grid(row=11, column=2,
                                                                                                    sticky=W)
        Button(self.mainWindow, text="get public key from File", command=self.getPubKeyFromFile, width = 18).grid(row=12, column=2,
                                                                                                      sticky=W)

        Radiobutton(self.mainWindow, text="Integers Only", variable=self.option, value=0).grid(row = 11, column = 4, sticky=W)
        Radiobutton(self.mainWindow, text="Message", variable=self.option, value=1).grid(row = 12, column = 4, sticky=W)

        self.msg1 = Label(self.mainWindow, text="Input must be an integer", foreground = "red")
        self.msg2 = Label(self.mainWindow, text="Output must be an integer", foreground = "red")
        self.msg3 = Label(self.mainWindow, text="Key must be an integer between 2 and 2048", foreground="red")


        self.mainWindow.mainloop()


    def getPrKeyFromFile(self):
        self.mainWindow.fileName = filedialog.askopenfilename(initialdir="./keys",
                                                              filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")),
                                                             title="Select private key file")
        if self.mainWindow.fileName != "":
            self.rsa.getPrivateKeyFromFile(str(self.mainWindow.fileName))
            if self.mainWindow.grid_slaves(4, 3)[0]['state'] == DISABLED:
                self.mainWindow.grid_slaves(4, 3)[0]['state'] = NORMAL
            if (self.msg3.winfo_ismapped()):
                self.msg3.grid_forget()



    def savePrKeyToFile(self):
        filename = filedialog.asksaveasfilename(title='Export private key', defaultextension='txt', initialdir="./keys")
        if filename != "":
            self.rsa.createPrivateKeyFile(filename)

    def getPubKeyFromFile(self):
        self.mainWindow.fileName = filedialog.askopenfilename(initialdir="./keys",
                                                              filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")),
                                                              title="Select public key file")
        if self.mainWindow.fileName != "":
            self.rsa.getPublicKeyFromFile(str(self.mainWindow.fileName))
            if self.mainWindow.grid_slaves(3, 3)[0]['state'] == DISABLED:
                self.mainWindow.grid_slaves(3, 3)[0]['state'] = NORMAL
            if (self.msg3.winfo_ismapped()):
                self.msg3.grid_forget()


    def savePubKeyToFile(self):
        filename = filedialog.asksaveasfilename(title='Export public key',defaultextension = 'txt',initialdir = "./keys")
        if filename != "":
            self.rsa.createPublicKeyFile(filename)

    def encryptFunction(self):
        if self.option.get() == 0:
            try:
                value = int(self.L.get(1.0,END))
                if (self.msg1.winfo_ismapped()):
                    self.msg1.grid_forget()
                if (self.msg2.winfo_ismapped()):
                    self.msg2.grid_forget()
                crypto = self.rsa.encryptInt(value)
                self.R.delete(1.0,END)
                self.R.insert(END, crypto)
            except:
                self.msg1['text'] = "Input must be an integer"
                self.msg1.grid(row=10, column=1, sticky=W)
        elif self.option.get() ==1:
            try:
                if (self.msg1.winfo_ismapped()):
                    self.msg1.grid_forget()
                if (self.msg2.winfo_ismapped()):
                    self.msg2.grid_forget()
                crypto = self.rsa.encryptText(self.L.get(1.0,END))
                self.R.delete(1.0, END)
                self.R.insert(END, crypto)
            except:
                self.msg1['text'] = "An error has occured"
                self.msg1.grid(row=10, column=1, sticky=W)


    def decryptFunction(self):
        if self.option.get() == 0:
            try:
                crypto = int(self.R.get(1.0,END))
                if (self.msg2.winfo_ismapped()):
                    self.msg2.grid_forget()
                if (self.msg1.winfo_ismapped()):
                    self.msg1.grid_forget()
                value = self.rsa.decryptInt(crypto)

                self.L.delete(1.0,END)
                self.L.insert(END, value)
            except:
                self.msg2.grid(row=10, column=4, sticky=W)
        elif self.option.get() == 1:
            try:
                crypto = int(self.R.get(1.0,END))
                if (self.msg2.winfo_ismapped()):
                    self.msg2.grid_forget()
                if (self.msg1.winfo_ismapped()):
                    self.msg1.grid_forget()

                value = self.rsa.decryptText(crypto)
                self.L.delete(1.0,END)
                self.L.insert(END, value)
            except:
                self.msg2.grid(row=10, column=4, sticky=W)


GUI = RSAInterface()
GUI.startGUI()


