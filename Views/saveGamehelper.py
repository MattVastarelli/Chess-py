from tkinter import *
import tkinter.messagebox as mb
from PIL import Image, ImageTk

class saveToFile:
    def __init__(self):
        self.saveGame = Tk()
        self.saveGame.geometry("200x115")
        self.saveGame.title("Save Game")
        self.saveGame.resizable(0,0)
        self.event_save = ''
        self.event_cancel = ''
    def function_tabs(self,):
        mb.showinfo("Test")
    def __repr__(self):
        return str(self.filename)
    def buildSaveGame (self,parent):
        frame1 = Frame(self.saveGame)
        frame1.pack(expand=True)
        
        for i in range (3):
            if i == 0:
                self.textBox = Entry(frame1)
                self.textBox.pack()
            if i == 1:
                saveButton = Button(frame1, text = "Save Game", width = "9", height = "1", command = self.event_save)
                saveButton.pack(side = LEFT)
            if i == 2:
                cancelButton = Button(frame1, text = "Cancel", width = "9", height = "1", command = self.event_cancel)
                cancelButton.pack(side = RIGHT)
    def readoutFile (self):
        text1 = self.textBox.get()
        print (test1)
        fn = open(text1, w)
        
    def showSaveGame(self):
        self.event_save = self.readoutFile
        self.event_cancel = self.saveGame.destroy
        sg = self.buildSaveGame(self.saveGame)
        return None
    def runSave(self):
        self.showSaveGame()
        self.saveGame.mainloop()
                            