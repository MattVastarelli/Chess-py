import tkinter as tk
import webbrowser

#Helper class, that displays help info
class help:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Help")

    #opens a webbrowser with direcitons to play chess
    def openHowTo (self, event):
        webbrowser.open_new(r"https://www.chess.com/learn-how-to-play-chess")

    #opens webbrowser to our git hub
    def openGitHub (self, event):
        webbrowser.open_new(r"https://github.com/MattVastarelli/Chess-py")

    #opens default email client
    def email (self, event):
        webbrowser.open('mailto:chessworks@yahoo.com', new=1)

    #builds the display with links to click on.
    def buildhelper(self, parent):
        frame1 = tk.Frame (self.window)
        frame1.pack(expand=True)

        text = tk.Label(frame1,  text="https://www.chess.com/learn-how-to-play-chess", cursor = "hand2")
        text.pack()
        text.bind("<Button-1>", self.openHowTo)

        text1 = tk.Label(frame1, text="View the Github Repo: https://github.com/MattVastarelli/Chess-py", cursor = "hand2")
        text1.pack()
        text1.bind("<Button-1>", self.openGitHub)

        text2 = tk.Label(frame1,  text="Contact the devs: chessworks@yahoo.com", cursor = "hand2")
        text2.pack()
        text2.bind("<Button-1>", self.email)

        button_OK = tk.Button(frame1, text = "OK", command = self.window.destroy)
        button_OK.pack()

        return frame1

    #Builds the frame and packs it in the main windows
    def show_help(self):
        helper = self.buildhelper(self.window)
        helper.pack()

        return None

    #Runs the program
    def run(self):
        self.show_help()
        tk.mainloop()
