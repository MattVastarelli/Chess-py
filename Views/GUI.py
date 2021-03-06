import tkinter as tk
import tkinter.messagebox as mb
from PIL import Image, ImageTk
from Views import guiBoard
from Views import loadGame
from Controller import guiChessButton
from Views import helpHelper


class SplashScreen:
    # Constructor for splash screen, user will see splash screen before anything else.
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

    def help(self,):
        # Brings up the help box with links to click
        run_help = helpHelper.Help()
        run_help.run()

    def about_button_action(self):
        mb.showinfo("About", "Authors: Matthew and Evan")

    def start_game(self):
        # If new game is clicked, Splash Screen is destroyed and game is loaded.
        self.welcome.destroy()
        gui = guiBoard.GuiBoard()
        gui.run()
    

    def resume_game(self):
        # This resumes the game
        # read from the save file and start the new game,
        # takes a string self.game that is populated by load_game
        # and converts into a dictionary
        # then the dictionary is passed to guiBoard which starts the game

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
        # This function gets string from file when Load game is selected
        # instantiate the class with a reference to the main controller class
        lsgui = loadGame.LoadFromFile(self.gui_objects.game)
        lsgui.run_load()
        self.game = str(lsgui)
        lsgui.destroy_windows()
        self.resume_game()

    def build_splash_screen(self, parent):
        # This method builds the frame and label where the buttons are displayed,
        # and the actions are assigned to the buttons

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
        # Create the top level GUI and creates the final assignments for event handling.
        self.event_help = self.help
        self.event_about = self.about_button_action

        splash = self.build_splash_screen(self.welcome)
        splash.pack()
        return None

    def run(self):
        # We now run the mainloop that displays the GUI on the screen.
        self.show_splash_screen()       
        tk.mainloop()

