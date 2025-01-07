from line import Line
from point import Point

class Cell:
    def __init__(self, x1, x2, y1, y2, win) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win
        self.top_left = (x1, y1)
        self.bottom_left = (x1, y2)
        self.top_right = (x2, y1)
        self.bottom_right = (x2, y2)

    def draw(self, line_color="white"):
        """draw() method conditionally draws the cell walls on the window canvas
        :returns: None
        """
        self.draw_left(line_color)
        self.draw_right(line_color)
        self.draw_top(line_color)
        self.draw_bottom(line_color)

    def draw_left(self, line_color):
        if self.has_left_wall:
            x1, y1 = self.top_left
            x2, y2 = self.bottom_left
            self._win.draw_line(x1, y1, x2, y2, line_color)

    def draw_right(self, line_color):
        if self.has_right_wall:
            x1, y1 = self.top_right
            x2, y2 = self.bottom_right
            self._win.draw_line(x1, y1, x2, y2, line_color)

    def draw_top(self, line_color):
        if self.has_top_wall:
            x1, y1 = self.top_left
            x2, y2 = self.top_right
            self._win.draw_line(x1, y1, x2, y2, line_color)

    def draw_bottom(self, line_color):
        if self.has_bottom_wall:
            x1, y1 = self.bottom_left
            x2, y2 = self.bottom_right
            self._win.draw_line(x1, y1, x2, y2, line_color)
