from point import Point 

class Line:
    def __init__(self, x: Point, y: Point) -> None:
        self.x1 = x.x
        self.y1 = x.y
        self.x2 = y.x
        self.y2 = y.y

    def draw(self, canvas, fill_color) -> int:
        return canvas.create_line(
            self.x1,
            self.y1,
            self.x2,
            self.y2,
            fill=fill_color,
            width=2
        )
