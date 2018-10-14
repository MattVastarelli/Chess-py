import tkinter as tk
import tkinter.messagebox as mb
from PIL import Image, ImageTk
from Models import board
from Controller import game

class tkGui:

    def __init__(self):
        self.top = tk.Tk()
        self.event_new = ''
        self.event_resume = ''
        self.event_save = ''
        self.event_help = ''
        self.event_about = ''
        self.event_exit = ''
        self.testphoto = Image.open('crown.png')
        self.tkphoto = ImageTk.PhotoImage(self.testphoto)
        self.click_count = 0
        self.click_1 = tuple()
        self.click_2 = tuple()

    # This builds the menu
    def build_menu(self, parent):
        menus = (
            ("File", (("New Game", self.event_new),
                      ("Resume Game", self.event_resume),
                      ("Save Game", self.event_save),
                      ("Exit", self.event_exit))),
            ("Help", (("Help", self.event_help),
                      ("About", self.event_about))),
        )

        menubar = tk.Menu(parent)

        for menu in menus:
            m = tk.Menu(parent)
            for item in menu[1]:
                m.add_command(label=item[0], command=item[1])
            menubar.add_cascade(label=menu[0], menu=m)

        return menubar

    # This shows that a cell has been clicked and registers the input
    def event_click(self, row, col):
        self.click_count += 1
        # remember the first click
        if self.click_count is 1:
            self.click_1 = (row, col)
        else:
            # check to see if two clicks have been made
            self.click_2 = (row, col)
            self.click_count = 0

        # mb.showinfo("cells", "Cell Clicked: rows:{}, col:{}".format(row, col))

    # This is just to represent what we plan to do later, meaningless at this point.
    def function_tabs(self,):
        mb.showinfo("Test", "to be developed later")

    # We build the chess board
    def build_chess_board(self, parent):
        outer = tk.Frame(parent, border=5, relief='sunken')
        inner = tk.Frame(outer)
        inner.pack()
        clr = True

        row_num = 0
        for row in range(8):  # This for loop builds the board while also alternating black and white squares
            if row % 2 == 0:
                clr = True
            if row % 2 != 0:
                clr = False
            for col in range(8):
                if clr is True:
                    if row_num > 1 and row_num < 6:
                        cell = tk.Button(inner, text="", width="20", height="7", background="sandybrown",
                                            command=lambda r=row, c=col: self.event_click(r, c))
                        cell.grid(row=row, column=col)
                    else:
                        cell = tk.Button(inner, text="", width="143", height="100", background="sandybrown",
                                            image=self.tkphoto, command=lambda r=row, c=col: self.event_click(r, c))

                        cell.grid(row=row, column=col)
                    clr = False
                elif clr is False:
                    if row_num > 1 and row_num < 6:
                        cell = tk.Button(inner, text=" ", width="20", height="7", background="saddlebrown",
                                            command=lambda r=row, c=col: self.event_click(r, c))

                        cell.grid(row=row, column=col)
                    else:
                        cell = tk.Button(inner, text=" ", width="143", height="100", background="saddlebrown",
                                            image=self.tkphoto, command=lambda r=row, c=col: self.event_click(r, c))

                        cell.grid(row=row, column=col)

                    clr = True
            row_num += 1
        return outer

    def show_board(self):
        self.event_new = self.function_tabs
        self.event_resume = self.function_tabs
        self.event_save = self.function_tabs
        self.event_exit = self.top.quit
        self.event_help = self.function_tabs
        self.event_about = self.function_tabs

        menubar = self.build_menu(self.top)
        self.top["menu"] = menubar
        ch_board = self.build_chess_board(self.top)
        ch_board.pack()

        tk.mainloop()

        return None
