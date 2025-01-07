from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self._root = Tk(className="MazeSolver")
        self._root.title("Game")
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._canvas = Canvas()
        self._canvas.pack(fill=BOTH, expand=True)
        self.is_running = False

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self.is_running = True

        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False
