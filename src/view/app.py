from tkinter import Tk

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("ChessPython")
        self.geometry("800x600")
        self.resizable(False, False)