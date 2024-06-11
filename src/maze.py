import time
from graphics import Point
from cell import Cell

class Maze():
    def __init__(self,
                 upper_left_point,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win=None):
        self._upper_left_point = upper_left_point
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
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

    def _draw_cell(self, cell):
        if self._win is None:
            return
        cell.draw()
        self._win.redraw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
