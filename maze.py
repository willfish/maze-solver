from cell import Cell
import random
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
        seed = None
    ) -> None:
        self.x1 = x1 # the width of the border
        self.y1 = y1 # the height of the border
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x # the width of the cell
        self.cell_size_y = cell_size_y # the height of the cell
        self.win = win
        self.cells = []

        if seed:
            random.seed(seed)

        self._create_cells()
        self._reset_cells_visited()

    def solve(self):
        return self._solve(0, 0)

    def _solve(self, i, j):
        cell = self.cells[i][j]
        cell.visit()

        if cell == self.cells[self.num_rows - 1][self.num_cols - 1]:
            return True

        for dead_end, new_cell, new_i, new_j, _ in self._solve_exhaust_directions(i, j):
            if not dead_end:
                cell.draw_move(new_cell, undo=False)
                self._animate()

                if self._solve(new_i, new_j):
                    return True
                else:
                    cell.draw_move(new_cell, undo=True)
                    self._animate()
                    continue

        return False

    def _create_cells(self):
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                x1, y1, x2, y2 =  self._calculate_cell_position(i, j)
                cell = Cell(x1, y1, x2, y2, self.win)
                self._draw_cell(cell)
                row.append(cell)
            self.cells.append(row)

        self._break_entrance_and_exit()
        self._break_walls(0, 0)

    def _calculate_cell_position(self, i, j):
        x1 = self.x1 + j * self.cell_size_x
        y1 = self.y1 + i * self.cell_size_y
        x2 =  x1 + self.cell_size_x
        y2 =  y1 + self.cell_size_y

        return (x1, y1, x2, y2)

    def _draw_cell(self, cell: Cell):
        cell.draw()
        self._animate()

    def _animate(self):
        time.sleep(0.05)
        self.win.redraw()

    def _break_entrance_and_exit(self):
        start_cell = self.cells[0][0]
        end_cell = self.cells[self.num_rows - 1][self.num_cols - 1]
        start_cell.has_left_wall = False
        end_cell.has_bottom_wall = False
        self._draw_cell(start_cell)
        self._draw_cell(end_cell)

    def _break_walls(self, i, j):
        cell: Cell = self.cells[i][j]
        cell.visit()

        if i == self.num_rows - 1 and j == self.num_cols - 1:
            return True

        for dead_end, new_cell, new_i, new_j, direction in self._exhaust_directions(i, j):
            if dead_end:
                return False

            self._break_wall(cell, new_cell, direction)
            self._draw_cell(cell)
            self._draw_cell(new_cell)

            if self._break_walls(new_i, new_j):
                return True
            else:
                continue

    def _reset_cells_visited(self):
        for row in self.cells:
            for cell in row:
                cell.visited = False

    def _break_wall(
        self,
        cell: Cell,
        new_cell: Cell,
        direction: str,
    ):
        match direction:
            case "top":
                cell.has_top_wall = False
                new_cell.has_bottom_wall = False
            case "bottom":
                cell.has_bottom_wall = False
                new_cell.has_top_wall = False
            case "left":
                cell.has_left_wall = False
                new_cell.has_right_wall = False
            case "right":
                cell.has_right_wall = False
                new_cell.has_left_wall = False
        self._draw_cell(cell)
        self._draw_cell(new_cell)


    def _exhaust_directions(self, i, j):
        directions = [
            (0, 1, "right"),
            (0, -1, "left"),
            (-1, 0, "top"),
            (1, 0, "bottom"),
        ]

        # Randomly exhaust the possible directions
        while len(directions) > 1:
            # Pick a direction
            random_index = random.randrange(0, len(directions))
            candidate_i, candidate_j, candidate_direction = directions[random_index]
            del directions[random_index]
            candidate_i, candidate_j = i + candidate_i, j + candidate_j

            # Handle exceeding the boundaries of the matrix
            if candidate_i < 0 or candidate_j < 0 or candidate_i > self.num_rows - 1 or candidate_j > self.num_cols - 1:
                continue

            candidate_cell = self.cells[candidate_i][candidate_j]

            # Handle already visited directions
            if candidate_cell.visited:
                continue

            # Found a valid direction
            new_i, new_j = candidate_i, candidate_j
            new_cell = candidate_cell
            direction = candidate_direction

            yield False, new_cell, new_i, new_j, direction

        yield True, None, None, None, None

    def _solve_exhaust_directions(self, i, j):
        directions = [
            (0, 1, "right"),
            (0, -1, "left"),
            (-1, 0, "top"),
            (1, 0, "bottom"),
        ]
        cell = self.cells[i][j]

        for offset_i, offset_j, direction in directions:
            new_i, new_j = (i + offset_i, j + offset_j)

            if new_i < 0 or new_j < 0 or new_i > self.num_rows - 1 or new_j > self.num_cols - 1:
                continue

            new_cell = self.cells[new_i][new_j]
            wall_in_way = getattr(cell, f"has_{direction}_wall")

            if new_cell.visited:
                print(f"Cell in direction {direction} already visited")
                continue

            if not wall_in_way:
                print(f"Trying direction: {direction}")
                yield False, new_cell, new_i, new_j, direction
            else:
                print(f"Wall found in direction: {direction}")


        yield True, None, None, None, None
