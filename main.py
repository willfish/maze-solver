from window import Window
from maze import Maze

border_width = 0
border_height = 0
width = 800
height = 800
win = Window(width, height)
cols = 200
rows = 200
seed = 100

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
print(f"Created a {rows}x{cols} maze")
print("Solving maze...")
result = maze.solve()
print("Maze solved:", result)

win.wait_for_close()
