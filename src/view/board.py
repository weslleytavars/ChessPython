from tkinter import Frame, Tk

class Board(Frame):
    def __init__(self, master: Tk):
        super().__init__(master)
        self.pack()

        self.squares_frame = Frame(self)
        self.squares_frame.pack()

        self.create_board_squares()

    def create_board_squares(self):
        """Creates the chess board squares."""
        for row in range(8):
            for col in range(8):
                color = 'white' if (row + col) % 2 == 0 else 'black'
                square = Frame(self.squares_frame, width=75, height=75, bg=color)
                square.grid(row=row, column=col)
