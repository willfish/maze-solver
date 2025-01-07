from tkinter import Tk, BOTH, Canvas
from point import Point
from line import Line
from cell import Cell

class Window():
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self._root = Tk(className="MazeSolver")
        self._root.title("Game")
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas()
        self.canvas.pack(fill=BOTH, expand=True)
        self.canvas.config(width=self.width, height=self.height)
        self.is_running = False

    def draw_line(self, x1, y1, x2, y2, fill_color):
        line = Line(Point(x1, y1), Point(x2, y2))
        line.draw(self.canvas, fill_color)

    def draw_cell(self, x1, y1, x2, y2, line_color) -> Cell:
        cell = Cell(x1, y1, x2, y2, self)
        cell.has_left_wall = False
        cell.has_right_wall = False
        cell.draw(line_color)

        return cell

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self.is_running = True

        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False
