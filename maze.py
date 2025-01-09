from cell import Cell
import random
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed = None) -> None:
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
        self._break_entrance_and_exit()
        self._break_walls_iterative()
        self._reset_cells_visited()

    def solve(self):
        return self._solve_iterative()

    def _solve_iterative(self):
        end_i = self.num_rows - 1
        end_j = self.num_cols - 1
        stack = [((0,0), None)]

        while stack:
            (i, j), parent = stack[-1]
            cell = self.cells[i][j]

            if i == end_i and j == end_j:
                return True

            unvisited_neighbors = list(
                filter(
                    lambda x: not x[0],
                    self._exhaust_directions(i, j, check_walls=True)
                )
            )
            if unvisited_neighbors:
                _, _, new_i, new_j, _ = unvisited_neighbors[0]
                new_cell = self.cells[new_i][new_j]

                new_cell.visit()

                cell.draw_move(new_cell, undo=False)
                self._animate()
                stack.append(((new_i, new_j), (i, j)))
            else:
                stack.pop()
                if parent is not None:
                    parent_cell = self.cells[parent[0]][parent[1]]
                    cell.draw_move(parent_cell, undo=True)
                    self._animate()

        return False


    def _solve_recursive(self, i = 0, j = 0):
        cell = self.cells[i][j]
        cell.visit()

        if cell == self.cells[self.num_rows - 1][self.num_cols - 1]:
            return True

        for dead_end, new_cell, new_i, new_j, _ in self._exhaust_directions(i, j, check_walls=True):
            if not dead_end:
                cell.draw_move(new_cell, undo=False)
                self._animate()

                if self.solve(new_i, new_j):
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
                self._draw_cell(cell, animate=False)
                row.append(cell)
            self.cells.append(row)

    def _calculate_cell_position(self, i, j):
        x1 = self.x1 + j * self.cell_size_x
        y1 = self.y1 + i * self.cell_size_y
        x2 =  x1 + self.cell_size_x
        y2 =  y1 + self.cell_size_y

        return (x1, y1, x2, y2)

    def _draw_cell(self, cell: Cell, animate=True):
        cell.draw()

        if animate:
            self._animate()

    def _animate(self):
        # time.sleep(0.001)
        self.win.redraw()

    def _break_entrance_and_exit(self):
        start_cell = self.cells[0][0]
        end_cell = self.cells[self.num_rows - 1][self.num_cols - 1]
        start_cell.has_left_wall = False
        end_cell.has_bottom_wall = False
        self._draw_cell(start_cell)
        self._draw_cell(end_cell)

    def _break_walls_recursive(self, i, j):
        cell: Cell = self.cells[i][j]
        cell.visit()

        for dead_end, new_cell, new_i, new_j, direction in self._exhaust_directions(i, j):
            if dead_end:
                return False

            self._break_wall(cell, new_cell, direction)
            self._draw_cell(cell)
            self._draw_cell(new_cell)

            if self._break_walls_recursive(new_i, new_j):
                return True
            else:
                continue

    def _break_walls_iterative(self):
        stack = [(0, 0)]

        while stack:
            i, j = stack.pop()
            current = self.cells[i][j]

            if not current.visited:
                current.visit()

            for dead_end, new_cell, new_i, new_j, direction in self._exhaust_directions(i, j):
                if dead_end:
                    continue

                self._break_wall(current, new_cell, direction)
                self._draw_cell(current)
                self._draw_cell(new_cell)

                new_cell.visit()
                stack.append((new_i, new_j))


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


    def _exhaust_directions(self, i, j, check_walls=False):
        directions = [
            (0, 1, "right"),
            (0, -1, "left"),
            (-1, 0, "top"),
            (1, 0, "bottom"),
        ]
        cell = self.cells[i][j]

        random.shuffle(directions)

        for offset_i, offset_j, direction in directions:
            new_i = i + offset_i
            new_j = j + offset_j

            if new_i < 0 or new_j < 0 or new_i > self.num_rows - 1 or new_j > self.num_cols - 1:
                continue

            current = self.cells[new_i][new_j]

            if current.visited:
                continue

            if check_walls:
                wall_in_way = getattr(cell, f"has_{direction}_wall")
            else:
                wall_in_way = False

            if not wall_in_way:
                yield False, current, new_i, new_j, direction

        yield True, None, None, None, None
