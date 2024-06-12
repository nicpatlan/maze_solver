import time, random
from graphics import Point
from cell import Cell

class Maze():
    def __init__(self,
                 upper_left_point,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win=None,
                 seed=None):
        self._upper_left_point = upper_left_point
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._rand = random.seed(0) if seed is None else random.seed(seed)
        self._create_cells()

    def _create_cells(self):
        for x in range(1, self._num_cols + 1):
            self._cells.append([])
            lower_right_x = self._upper_left_point.x + (self._cell_size_x * x)
            upper_left_x = self._upper_left_point.x + (self._cell_size_x * (x - 1))
            for y in range(1, self._num_rows + 1):
                upper_left_y = self._upper_left_point.y + (self._cell_size_y * (y - 1))
                upper_left_point = Point(upper_left_x, upper_left_y)
                lower_right_y = self._upper_left_point.y + self._cell_size_y * y
                lower_right_point = Point(lower_right_x, lower_right_y)
                cell = Cell(upper_left_point, lower_right_point, self._win)
                self._cells[x - 1].append(cell)
                self._draw_cell(cell)
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _draw_cell(self, cell):
        if self._win is None:
            return
        cell.draw()
        self._win.redraw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        ent_cell = self._cells[0][0]
        if random.randrange(1) == 0:
            ent_cell.has_top_wall = False
        else:
            ent_cell.has_left_wall = False
        self._draw_cell(ent_cell)
        exit_cell = self._cells[self._num_cols - 1][self._num_rows - 1]
        if random.randrange(1) == 0:
            exit_cell.has_bottom_wall = False
        else:
            exit_cell.has_right_wall = False
        self._draw_cell(exit_cell)

    def _break_walls_r(self, col, row):
        self._cells[col][row].visited = True
        while True:
            to_visit = []
            if col > 0 and not self._cells[col - 1][row].visited:
                to_visit.append((col - 1, row))
            if col < self._num_cols - 1 and not self._cells[col + 1][row].visited:
                to_visit.append((col + 1, row))
            if row > 0 and not self._cells[col][row - 1].visited:
                to_visit.append((col, row - 1))
            if row < self._num_rows - 1 and not self._cells[col][row + 1].visited:
                to_visit.append((col, row + 1))

            if len(to_visit) == 0:
                self._draw_cell(self._cells[col][row])
                return

            direction = random.randrange(len(to_visit))
            next_cell = to_visit[direction]
            if next_cell[0] == col:
                if next_cell[1] == row + 1:
                    # moving down
                    self._cells[col][row].has_bottom_wall = False
                    self._cells[next_cell[0]][next_cell[1]].has_top_wall = False
                else:
                    # moving up
                    self._cells[col][row].has_top_wall = False
                    self._cells[next_cell[0]][next_cell[1]].has_bottom_wall = False
            else:
                if next_cell[0] == col - 1:
                    # moving left
                    self._cells[col][row].has_left_wall = False
                    self._cells[next_cell[0]][next_cell[1]].has_right_wall = False
                else:
                    # moving right
                    self._cells[col][row].has_right_wall = False
                    self._cells[next_cell[0]][next_cell[1]].has_left_wall = False
            self._break_walls_r(next_cell[0], next_cell[1]) 
