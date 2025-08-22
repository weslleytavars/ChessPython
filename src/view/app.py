from tkinter import Tk

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("ChessPython")
        self.geometry("800x600")
        self.resizable(False, False)

        self.center_window()

    def center_window(self):
        """Center the window on the screen."""
        self.update_idletasks()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        app_width = self.winfo_width()
        app_height = self.winfo_height()

        x = (screen_width // 2) - (app_width // 2)
        y = (screen_height // 2) - (app_height // 2)
        self.geometry(f"{app_width}x{app_height}+{x}+{y}")
