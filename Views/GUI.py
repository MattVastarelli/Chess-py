import tkinter as tk
import tkinter.messagebox as mb
from PIL import Image, ImageTk
from Views import guiBoard
from Views import loadGame
from Views import guiChessButton


class SplashScreen:
    def __init__(self):
        self.welcome = tk.Tk()
        self.welcome.geometry("500x700")
        self.welcome.title("Chess")
        self.bgphoto = Image.open('chessbgc5.jpg')
        self.tkphoto1 = ImageTk.PhotoImage(self.bgphoto)
        self.welcome.resizable(0, 0)
        self.event_new = ''
        self.event_help = ''
        self.event_about = ''
        self.event_exit = ''
        self.game = ''
        self.gui_objects = guiChessButton.GuiObjects()
         
    def function_tabs(self,):
        mb.showinfo("Test")

    def about_button_action(self):
        mb.showinfo("About", "Authors: Matthew and Evan")

    def start_game(self):
        self.welcome.destroy()
        gui = guiBoard.GuiBoard()
        gui.run()

    def resume_game(self):
        # read from the save file and start the new game
        dictofPieces = dict()
        tempNum = ''
        tempPiece = ''
        for c in self.game:
            if c.isdigit():
                tempNum += c
            elif c.isalpha():
                tempPiece += c
                if tempPiece == "turnWhite" or tempPiece == "turnBlack":
                    dictofPieces['turn'] = tempPiece
            elif c == ',' and tempPiece != '':
                tempTuple = (int(tempNum[0]), int(tempNum[1]))
                dictofPieces[tempTuple] = tempPiece
                tempNum = ''
                tempPiece = ''
        self.welcome.destroy()
        gui = guiBoard.LoadGuiBoard()
        gui.run(dictofPieces)

        return None

    def load_game(self,):
        # instantiate the class with a reference to the main controller class
        lsgui = loadGame.LoadFromFile(self.gui_objects.game)
        lsgui.run_load()
        self.game = str(lsgui)
        lsgui.destroy_windows()
        self.resume_game()

    def build_splash_screen(self, parent):
        backpic = tk.Label(self.welcome, image=self.tkphoto1)
        backpic.place(x=0, y=0, relwidth=1, relheight=1)
        outer = tk.Frame(parent, border=5, background="sandybrown", relief='sunken')
        inner = tk.Frame(outer, background="saddlebrown")
        inner.pack()
        for i in range(5):
            if i == 0:
               b1 = tk.Button(inner, text="New Game", width="35", height="7", command=self.start_game)
               b1.pack()
            if i == 1:
               b2 = tk.Button(inner, text="Resume Game", width="35", height="7", command=self.load_game)
               b2.pack()
            if i == 2:
               b3 = tk.Button(inner, text="Help", width="35", height="7", command=self.event_help)
               b3.pack()
            if i == 3:
               b4 = tk.Button(inner, text="About", width="35", height="7", command=self.event_about)
               b4.pack()
            if i == 4:
               b5 = tk.Button(inner, text="Quit", width="35", height="7", command=self.welcome.destroy)
               b5.pack()
        
        return outer

    def show_splash_screen(self):
        self.event_help = self.function_tabs
        self.event_about = self.about_button_action

        splash = self.build_splash_screen(self.welcome)
        splash.pack()
        return None

    def run(self):
        self.show_splash_screen()
       
        tk.mainloop()


