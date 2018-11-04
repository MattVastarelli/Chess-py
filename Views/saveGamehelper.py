import tkinter as tk
import tkinter.messagebox as mb

class saveToFile:
    def __init__(self):
        self.saveGame = tk.Tk()
        self.saveGame.geometry("700x500")
        self.saveGame.title("Save Game")
        self.saveGame.resizable(0,0)
        self.event_save = ''
        self.event_cancel = ''
    def function_tabs(self,):
        mb.showinfo("Test")
    def buildSaveGame (self, parent):
        #outer = tk.Frame(parent, border = 5, background = "sandybrown", relief = 'sunken')
        #inner = tk.Frame(outer, backgroud = "saddlebrown")
        for i in range (3):
            if i == 0:
                textBox = tk.Entry(self.saveGame, text = "Type in name for saved game")
                textBox.pack()
            if i == 1:
                saveButton = tk.Button(self.saveGame, text = "Save Game", width = "35", height = "5", command = self.event_save)
                saveButton.pack()
            if i == 2:
                cancelButton = tk.Button(self.saveGame, text = "Cancel", width = "35", height = "5", command = self.event_cancel)
                cancelButton.pack()
    def showSaveGame(self):
        self.event_save = self.function_tabs
        self.event_cancel = self.function_tabs
        sg = self.buildSaveGame(self.saveGame)
        return None
    def runSave(self):
        self.showSaveGame()
        tk.mainloop
                            