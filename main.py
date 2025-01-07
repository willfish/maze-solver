from window import Window

win = Window(800, 600)

win.draw_cell(200, 300, 300, 200, "red")

win.wait_for_close()
