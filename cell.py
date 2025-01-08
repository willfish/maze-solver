class Cell:
    def __init__(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        win,
        line_color = "white",
    ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.line_color = line_color
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self.top_left = (x1, y1)
        self.bottom_left = (x1, y2)
        self.top_right = (x2, y1)
        self.bottom_right = (x2, y2)
        self.cell_center = (
            (x1 + x2) // 2,
            (y1 + y2) // 2,
        )
        self._win = win
        self.left = None
        self.right = None
        self.top = None
        self.bottom = None
        self.move = None

    def visit(self):
        self.visited = True

    def draw(self):
        """draw() method conditionally draws the cell walls on the window canvas
        :returns: None
        """
        self._draw_left()
        self._draw_right()
        self._draw_top()
        self._draw_bottom()

    def draw_move(self, to_cell, undo=False):
        """draw_move() method draws a line between the current cell and the other cell
            :param to_cell: Cell object
        """
        if self.move:
            self._win.canvas.delete(self.move)

        if undo:
            line_color = "gray"
        else:
            line_color = "red"

        x1, y1 = self.cell_center
        x2, y2 = to_cell.cell_center

        self.move = self._win.draw_line(x1, y1, x2, y2, line_color)

    def undo_move(self):
        """undo_move() method clears the move line from the window canvas
        :returns: None
        """
        if self.move:
            self._win.canvas.delete(self.move)
            self.move = None

    def _draw_left(self):
        if self.has_left_wall:
            if self.left:
                return

            x1, y1 = self.top_left
            x2, y2 = self.bottom_left
            self.left = self._win.draw_line(x1, y1, x2, y2, self.line_color)
        else:
            self.clear("left")
            self.left = None

    def _draw_right(self):
        if self.has_right_wall:
            if self.right:
                return

            x1, y1 = self.top_right
            x2, y2 = self.bottom_right
            self.right = self._win.draw_line(x1, y1, x2, y2, self.line_color)
        else:
            self.clear("right")
            self.right = None

    def _draw_top(self):
        if self.has_top_wall:
            if self.top:
                return

            x1, y1 = self.top_left
            x2, y2 = self.top_right
            self.top = self._win.draw_line(x1, y1, x2, y2, self.line_color)
        else:
            self.clear("up")
            self.top = None

    def _draw_bottom(self):
        if self.has_bottom_wall:
            if self.bottom:
                return

            x1, y1 = self.bottom_left
            x2, y2 = self.bottom_right
            self.bottom = self._win.draw_line(x1, y1, x2, y2, self.line_color)
        else:
            self.clear("down")
            self.bottom = None

    def clear(self, direction):
        """clear() method conditionally clears the cell walls on the window canvas
        :returns: None
        """
        if direction == "up":
            self._win.canvas.delete(self.top)
        elif direction == "down":
            self._win.canvas.delete(self.bottom)
        elif direction == "left":
            self._win.canvas.delete(self.left)
        elif direction == "right":
            self._win.canvas.delete(self.right)
