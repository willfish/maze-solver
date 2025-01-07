class Cell:
    def __init__(self, x1, y1, x2, y2, win) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win
        self.top_left = (x1, y1)
        self.bottom_left = (x1, y2)
        self.top_right = (x2, y1)
        self.bottom_right = (x2, y2)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        # x_mid = (self.top_right[0] - self.top_left[0]) // 2
        # y_mid = (self.bottom_left[1] - self.top_left[1]) // 2
        x_mid = (x1 + x2) // 2 # 
        y_mid = (y1 + y2) // 2
        self.cell_center = (x_mid, y_mid)

    def draw(self, line_color="white"):
        """draw() method conditionally draws the cell walls on the window canvas
        :returns: None
        """
        self._draw_left(line_color)
        self._draw_right(line_color)
        self._draw_top(line_color)
        self._draw_bottom(line_color)

    def draw_move(self, to_cell, undo=False):
        """draw_move() method draws a line between the current cell and the other cell
            :param to_cell: Cell object
        """
        if undo:
            line_color = "gray"
        else:
            line_color = "red"

        x1, y1 = self.cell_center
        x2, y2 = to_cell.cell_center

        self._win.draw_line(x1, y1, x2, y2, line_color)

    def _draw_left(self, line_color):
        if self.has_left_wall:
            x1, y1 = self.top_left
            x2, y2 = self.bottom_left
            self._win.draw_line(x1, y1, x2, y2, line_color)

    def _draw_right(self, line_color):
        if self.has_right_wall:
            x1, y1 = self.top_right
            x2, y2 = self.bottom_right
            self._win.draw_line(x1, y1, x2, y2, line_color)

    def _draw_top(self, line_color):
        if self.has_top_wall:
            x1, y1 = self.top_left
            x2, y2 = self.top_right
            self._win.draw_line(x1, y1, x2, y2, line_color)

    def _draw_bottom(self, line_color):
        if self.has_bottom_wall:
            x1, y1 = self.bottom_left
            x2, y2 = self.bottom_right
            self._win.draw_line(x1, y1, x2, y2, line_color)
