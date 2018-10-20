import tkinter as tk
import tkinter.messagebox as mb
from Views import guiHelper
from PIL import Image, ImageTk

class SplashScreen:
    def __init__(self):
         self.welcome = tk.Tk()
         self.welcome.geometry("500x700")
         self.welcome.title("Chess")
         self.bgphoto = Image.open('chessbgc5.jpg')
         self.tkphoto1 = ImageTk.PhotoImage(self.bgphoto)
         self.welcome.resizable(0,0)
         self.event_new = ''
         self.event_resume = ''
         self.event_help = ''
         self.event_about = ''
         self.event_exit = ''
         
    def function_tabs(self,):
        mb.showinfo("Test")
    def AboutButtonAction(self,):
        mb.showinfo("About", "Authors: Matthew and Evan")
    def buildSplashScreen(self, parent):
        backpic = tk.Label(self.welcome, image=self.tkphoto1)
        backpic.place(x=0,y=0, relwidth = 1, relheight =1)
        outer = tk.Frame(parent, border = 5, background = "sandybrown", relief = 'sunken')
        inner = tk.Frame(outer, background = "saddlebrown")
        inner.pack()
        for i in range(5):
            if i == 0:
               b1 =  tk.Button(inner, text = "New Game", width="35", height="7",command = self.startGame)
               b1.pack()
            if i == 1:
               b2 =  tk.Button(inner, text = "Resume Game", width="35", height="7",command = self.event_resume)
               b2.pack()
            if i == 2:
               b3 =  tk.Button(inner, text = "Help", width="35", height="7",command = self.event_help)
               b3.pack()
            if i == 3:
               b4 =  tk.Button(inner, text = "About", width="35", height="7", command = self.event_about)
               b4.pack()
            if i == 4:
               b5 =  tk.Button(inner, text = "Quit", width="35", height="7",command = self.event_exit)
               b5.pack()
        
        return outer
    def startGame(self):
        self.welcome.destroy()
        testgui = TkGui()
        testgui.run()
    def showSplashScreen(self):
        self.event_resume = self.function_tabs
        self.event_exit = self.function_tabs
        self.event_help = self.function_tabs
        self.event_about = self.AboutButtonAction        
        splash = self.buildSplashScreen(self.welcome)        
        splash.pack()
        return None
    def run(self):
        self.showSplashScreen()
       
        tk.mainloop()



class TkGui:
    # main GUI class to build the gui and launch call the controller methods
    def __init__(self):
        self.top = tk.Tk()
        self.event_new = ''
        self.event_resume = ''
        self.event_save = ''
        self.event_help = ''
        self.event_about = ''
        self.event_exit = ''
        self.gui_objects = guiHelper.GuiObjects()

    # This builds the menu
    def build_menu(self, parent):
        menus = (("File", (("New Game", self.event_new),
                      ("Resume Game", self.event_resume),
                      ("Save Game", self.event_save),
                      ("Exit", self.event_exit))),
            ("Help", (("Help", self.event_help),
                      ("About", self.event_about))),)

        menubar = tk.Menu(parent)

        for menu in menus:
            m = tk.Menu(parent)
            for item in menu[1]:
                m.add_command(label=item[0], command=item[1])
            menubar.add_cascade(label=menu[0], menu=m)

        return menubar

    # This is just to represent what we plan to do later, meaningless at this
    # point.
    def function_tabs(self,):
        mb.showinfo("Test", "to be developed later")

    # build the chess board
    def build_chess_board(self, parent):
        outer = tk.Frame(parent, border=5, relief='sunken')
        inner = tk.Frame(outer)
        inner.pack()
        clr = True

        row_num = 0
        # This for loop builds the board while also alternating sandybrown and
        # saddlebrown squares
        for row in range(8): 
            if row % 2 == 0:
                clr = True
            if row % 2 != 0:
                clr = False
            for col in range(8):
                if clr is True:
                    if row_num > 1 and row_num < 6:
                        cell = tk.Button(inner, text="", width="20", height="7", background="sandybrown",
                                            command=lambda r=row, c=col: self.gui_objects.event_click(r, c))

                        cell.grid(row=row, column=col)
                        self.gui_objects.gui_board[row][col] = cell
                    else:
                        cell = tk.Button(inner, text="", width="143", height="110", background="sandybrown",
                            image=self.gui_objects.tkphoto,
                                         command=lambda r=row, c=col: self.gui_objects.event_click(r, c))

                        cell.grid(row=row, column=col)
                        self.gui_objects.gui_board[row][col] = cell
                    clr = False
                elif clr is False:
                    if row_num > 1 and row_num < 6:
                        cell = tk.Button(inner, text=" ", width="20", height="7", background="saddlebrown",
                                            command=lambda r=row, c=col: self.gui_objects.event_click(r, c))

                        cell.grid(row=row, column=col)
                        self.gui_objects.gui_board[row][col] = cell
                    else:
                        cell = tk.Button(inner, text=" ", width="143", height="110", background="saddlebrown",
                            image=self.gui_objects.tkphoto,
                                         command=lambda r=row, c=col: self.gui_objects.event_click(r, c))

                        cell.grid(row=row, column=col)
                        self.gui_objects.gui_board[row][col] = cell

                    clr = True
            row_num += 1
        return outer

    def show_board(self):
        self.event_new = self.function_tabs
        self.event_resume = self.function_tabs
        self.event_save = self.function_tabs
        self.event_exit = self.function_tabs
        self.event_help = self.function_tabs
        self.event_about = self.function_tabs

        menubar = self.build_menu(self.top)
        self.top["menu"] = menubar
        ch_board = self.build_chess_board(self.top)
        ch_board.pack()

        return None

    def run(self):
        self.show_board()
        tk.mainloop()
