import unittest
from unittest.mock import Mock

from maze import Maze

def any_cells_visited(maze):
    for row in maze.cells:
        for cell in row:
            if cell.visited:
                return True
    return False

class TestMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        window = Mock()
        window.draw_line.return_value = 1
        window.clear.return_value = None
        window.redraw.return_value = None
        num_rows = 10
        num_cols = 12
        maze = Maze(0, 0, num_rows, num_cols, 10, 10, window)
        self.assertEqual(
            len(maze.cells),
            num_rows,
        )
        self.assertEqual(
            len(maze.cells[0]),
            num_cols,
        )

        self.assertFalse(any_cells_visited(maze))

if __name__ == "__main__":
    unittest.main()
