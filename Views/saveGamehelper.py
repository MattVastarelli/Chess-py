from tkinter import *
import tkinter.messagebox as mb
from PIL import Image, ImageTk
from Models import board
from Controller import game

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
        print (text1)
        text1 += ".txt"
        fn = open(text1, 'w')
        checkforpiece = game.Game()
        currentstate = board.Board()      
        x = 0
        y = 0
        while y <= 7:
            while x <= 7:
                tuple1 = (x,y)
                test1 = currentstate.get_spot(x,y)
                print(test1)
                x+=1
                occupied = checkforpiece.is_spot_occupied(tuple1)
                if occupied == True:
                    print(occupied, tuple1)
                    piece = checkforpiece.get_piece_type(tuple1)
                    color = checkforpiece.get_piece_color(tuple1)
                    tofile = str(tuple1)
                    tofile +='@'
                    color = str(color)
                    tofile += color
                    tofile += '@'
                    piece = str(piece)
                    tofile += piece
                    fn.write(tofile)
                    fn.write('\n')
                    
                elif occupied == False:
                    continue
            x = 0
            y+=1
        fn.close()
        self.saveGame.destroy()

        
    def showSaveGame(self):
        self.event_save = self.readoutFile
        self.event_cancel = self.saveGame.destroy
        sg = self.buildSaveGame(self.saveGame)
        return None
    def runSave(self):
        self.showSaveGame()
        self.saveGame.mainloop()
                            