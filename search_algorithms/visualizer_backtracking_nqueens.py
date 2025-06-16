import tkinter as tk
import time

CELL_SIZE = 50
DELAY = 0.1

class NQueensVisualizer:
    def __init__(self, size):
        self.size = size
        self.results = 0

        self.window = tk.Tk()
        self.window.title(f"{size}-Queens Visualizer")
        canvas_size = CELL_SIZE * size
        self.canvas = tk.Canvas(self.window, width=canvas_size, height=canvas_size)
        self.canvas.pack()

        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.rects = [[None for _ in range(size)] for _ in range(size)]
        self.draw_board()
        self.window.after(500, lambda: self.solve(0))
        self.window.mainloop()

    def draw_board(self):
        for row in range(self.size):
            for col in range(self.size):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                color = "white" if (row + col) % 2 == 0 else "gray"
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                self.rects[row][col] = rect

    def draw_queen(self, row, col, place=True):
        x = col * CELL_SIZE + CELL_SIZE // 2
        y = row * CELL_SIZE + CELL_SIZE // 2
        symbol = "♛" if place else ""
        self.canvas.create_text(x, y, text=symbol, font=("Arial", 24), tags=f"q{row}{col}")
        if not place:
            self.canvas.delete(f"q{row}{col}")
        self.window.update()
        time.sleep(DELAY)

    def solve(self, row):
        if row == self.size:
            self.results += 1
            self.save_solution()
            print(f"Solution #{self.results}")
            time.sleep(0.8)
            return

        for col in range(self.size):
            self.board[row][col] = 1
            self.draw_queen(row, col, place=True)

            if self.is_safe(row, col):
                self.solve(row + 1)

            self.board[row][col] = 0
            self.draw_queen(row, col, place=False)

    def is_safe(self, row, col):
        for i in range(row):
            if self.board[i][col] == 1:
                return False

        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        i, j = row - 1, col + 1
        while i >= 0 and j < self.size:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def save_solution(self):
        with open("solutions.txt", "a", encoding="utf-8") as f:
            f.write(f"Solution #{self.results}:\n")
            for row in self.board:
                f.write(" ".join("♛" if cell else "·" for cell in row) + "\n")
            f.write("\n")



