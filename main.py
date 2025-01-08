from window import Window
from maze import Maze

border_width = 0
border_height = 0
width = 1500
height = 1000
win = Window(width, height)
cols = 30
rows = 30
seed = 0

maze = Maze(
    border_width,
    border_height,
    rows,
    cols,
    (width - border_width * 2) // rows,
    (height - border_height * 2) // cols,
    win,
    seed
)

win.wait_for_close()
