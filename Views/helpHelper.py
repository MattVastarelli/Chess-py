import tkinter as tk
import webbrowser


class Help:
    # Helper class, that displays help info
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Help")

    def open_how_to(self, event):
        # opens a web browser with directions to play chess
        webbrowser.open_new(r"https://www.chess.com/learn-how-to-play-chess")

    def open_git_hub(self, event):
        # opens web browser to our github
        webbrowser.open_new(r"https://github.com/MattVastarelli/Chess-py")
        return None

    def email(self, event):
        # opens default email client
        webbrowser.open('mailto:chessworks@yahoo.com', new=1)
        return None

    def build_helper(self, parent):
        # builds the display with links to click on.
        frame1 = tk.Frame(self.window)
        frame1.pack(expand=True)

        text = tk.Label(frame1,  text="https://www.chess.com/learn-how-to-play-chess", cursor = "hand2")
        text.pack()
        text.bind("<Button-1>", self.open_how_to)

        text1 = tk.Label(frame1, text="View the Github Repo: https://github.com/MattVastarelli/Chess-py", cursor = "hand2")
        text1.pack()
        text1.bind("<Button-1>", self.open_git_hub)

        text2 = tk.Label(frame1,  text="Contact the devs: chessworks@yahoo.com", cursor = "hand2")
        text2.pack()
        text2.bind("<Button-1>", self.email)

        button_ok = tk.Button(frame1, text="OK", command=self.window.destroy)
        button_ok.pack()

        return frame1

    def show_help(self):
        # Builds the frame and packs it in the main windows
        helper = self.build_helper(self.window)
        helper.pack()

        return None

    def run(self):
        # Runs the program
        self.show_help()
        tk.mainloop()
