from tkinter import *
import tkinter.messagebox as mb


class LoadFromFile:
    def __init__(self):
        self.loadGame = Tk()
        self.loadGame.geometry("200x115")
        self.loadGame.title("Load Game")
        self.loadGame.resizable(0, 0)
        self.load_save = ''
        self.event_cancel = ''
        self.text_box = ''

    def build_load_game(self, parent):
        frame1 = Frame(self.loadGame)
        frame1.pack(expand=True)

        for i in range(3):
            if i == 0:
                self.text_box = Entry(frame1)
                self.text_box.pack()
            if i == 1:
                load_button = Button(frame1, text="Load Game", width="9", height="1", command=self.load_save)
                load_button.pack(side=LEFT)
            if i == 2:
                cancel_button = Button(frame1, text="Cancel", width="9", height="1", command=self.event_cancel)
                cancel_button.pack(side=RIGHT)

    def loadFromFile(self):
        text1 = self.text_box.get()
        text1 += ".txt"
        try:
            x = -1
            y = -1
            counter = 0
            color = ''
            piece = ''
            numberholder = ''
            test=[line.strip() for line in open(text1, 'r')]
            for line in test:
                print(line)
                for c in line:
                    if c.isdigit() and y == -1:
                        y = int(c)
                    elif c.isdigit() and x == -1:
                        x = int(c)
                    elif x != -1 and y != -1:
                        numberholder += str(y)
                        numberholder += str(x)
                        x = -1
                        y = -1
                    elif c == '@' and counter == 0:
                        counter += 1
                    elif c != '@' and counter == 1 and c.isalpha():
                        color += c
                    elif c == '@' and counter == 1:
                        counter += 1
                    elif c != '@' and counter == 2 and c.isalpha():
                        piece += c

                print("Test: ", numberholder)
                print("Test: ", color)
                print("Test: ", piece)
                piece = ''
                color = ''
                counter = 0
                numberholder = ''
                if y != -1 or x != -1:
                    y = -1
                    x = -1
            self.loadGame.destroy()
        except FileNotFoundError:
            mb.showinfo("ERROR", "File Does Not Exist!")
            self.loadGame.destroy()

    def show_load_game(self):
        self.load_save = self.loadFromFile
        self.event_cancel = self.loadGame.destroy
        lg = self.build_load_game(self.loadGame)

        return None

    def run_load(self):
        self.show_load_game()
        self.loadGame.mainloop()
