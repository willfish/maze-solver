import unittest

from maze import Maze

class TestMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        num_rows = 10
        num_cols = 12
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(maze.cells),
            num_cols,
        )
        self.assertEqual(
            len(maze.cells[0]),
            num_rows,
        )

if __name__ == "__main__":
    unittest.main()
