from window import Window

win = Window(800, 600)

cell_1 = win.draw_cell(100, 200, 200, 100, "red")
cell_2 = win.draw_cell(300, 200, 400, 100, "red")
cell_3 = win.draw_cell(500, 200, 600, 100, "red")

cell_1.draw_move(cell_2)
cell_2.draw_move(cell_3)

win.wait_for_close()
