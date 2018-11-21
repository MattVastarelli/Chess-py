from Views import guiBoard
from tkinter import *

#This method helps start a new game, when called within the game.
class NewGame:
    #contructor
    def __init__(self, current_game):
        self.ng = Tk()
        self.ng.title("New Game?")
        self.ng.geometry("200x115")
        self.ng.resizable(0,0)
        self.event_new = ''
        self.event_cancel = ''
        self.guiBoard = current_game

    #Builds new game windows asking if the user is sure.
    def build_new_game(self, parent):
        frame1 = Frame(self.ng)
        frame1.pack(expand=True)

        for i in range(3):
            if i == 0:
                usure = Text(frame1, height="2", width="30")
                usure.pack()
                usure.insert(END, "Are you sure you want to start a new game?")
            if i == 1:
                new_button = Button(frame1, text="New Game", width="10", height="1", command=self.event_new)
                new_button.pack(side=LEFT)
            if i == 2:
                cancel_button = Button(frame1, text="Cancel", width="10", height="1", command=self.event_cancel)
                cancel_button.pack(side=RIGHT)

    #Starts the new game if the user selects the button for it.
    def start_new_game(self):
        self.ng.destroy()
        self.guiBoard.destroy()
        sng = guiBoard.GuiBoard()
        sng.run()

    #This creates the window for the new game window.
    def show_new_game(self):
        self.event_new = self.start_new_game
        self.event_cancel = self.ng.destroy
        ngd = self.build_new_game(self.ng)

        return None

    #This displays the window on the screen for the user.
    def run(self):
        self.show_new_game()
        self.ng.mainloop()
