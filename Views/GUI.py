import tkinter as Chess
import tkinter.messagebox as mb
from PIL import Image, ImageTk

class tkGui:

    def __init__(self):
        self.top = Chess.Tk()
        self.eventNew = ''
        self.eventResume = ''
        self.eventSave = ''
        self.eventHelp = ''
        self.eventAbout = ''
        self.eventExit = ''
        self.testphoto = Image.open('crown.png')
        self.tkphoto = ImageTk.PhotoImage(self.testphoto)

    # This builds the menu
    def buildMenu(self, parent):
        menus = (
            ("File", (("New Game", self.eventNew),
                      ("Resume Game", self.eventResume),
                      ("Save Game", self.eventSave),
                      ("Exit", self.eventExit))),
            ("Help", (("Help", self.eventHelp),
                      ("About", self.eventAbout))),
        )

        menubar = Chess.Menu(parent)

        for menu in menus:
            m = Chess.Menu(parent)
            for item in menu[1]:
                m.add_command(label=item[0], command=item[1])
            menubar.add_cascade(label=menu[0], menu=m)

        return menubar

    # This shows that a cell has been clicked and registers the input
    def eventClick(self, row, col):
        mb.showinfo("cells", "Cell Clicked: rows:{}, col:{}".format(row, col))

    # This is just to represent what we plan to do later, meaningless at this point.
    def Functiontabs(self,):
        mb.showinfo("Test", "to be developed later")

    # We build the chess board
    def buildChessBoard(self, parent):
        outer = Chess.Frame(parent, border=5, relief='sunken')
        inner = Chess.Frame(outer)
        inner.pack()
        clr = True

        rowNum = 0
        for row in range(8):  # This for loop builds the board while also alternating black and white squares
            if row % 2 == 0:
                clr = True
            if row % 2 != 0:
                clr = False
            for col in range(8):
                if clr is True:
                    if rowNum > 1 and rowNum < 6:
                        cell = Chess.Button(inner, text="", width="20", height="7", background="sandybrown",
                                            command=lambda r=row, c=col: self.eventClick(r, c))
                        cell.grid(row=row, column=col)
                    else:
                        cell = Chess.Button(inner, text="", width="143", height="100", background="sandybrown",
                                            image=self.tkphoto, command=lambda r=row, c=col: self.eventClick(r, c))

                        cell.grid(row=row, column=col)
                    clr = False
                elif clr is False:
                    if rowNum > 1 and rowNum < 6:
                        cell = Chess.Button(inner, text=" ", width="20", height="7", background="saddlebrown",
                                            command=lambda r=row, c=col: self.eventClick(r, c))

                        cell.grid(row=row, column=col)
                    else:
                        cell = Chess.Button(inner, text=" ", width="143", height="100", background="saddlebrown",
                                            image=self.tkphoto, command=lambda r=row, c=col: self.eventClick(r, c))

                        cell.grid(row=row, column=col)

                    clr = True
            rowNum += 1
        return outer

    def showStartBoard(self):
        self.eventNew = self.Functiontabs
        self.eventResume = self.Functiontabs
        self.eventSave = self.Functiontabs
        self.eventExit = self.top.quit
        self.eventHelp = self.Functiontabs
        self.eventAbout = self.Functiontabs

        menubar = self.buildMenu(self.top)
        self.top["menu"] = menubar
        chBoard = self.buildChessBoard(self.top)
        chBoard.pack()

        Chess.mainloop()


