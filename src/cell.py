from graphics import Line, Point

class Cell():
    def __init__(self, p1, p2, win=None):
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._p_upper_l = p1
        self._p_lower_r = p2
        self.visited = False

    def draw(self):
        if self._win == None:
            return
        p_lower_l = Point(self._p_upper_l.x,
                          self._p_lower_r.y)
        p_upper_r = Point(self._p_lower_r.x,
                          self._p_upper_l.y)

        wall_color = "black" if self.has_left_wall else "white"
        self._win.draw_line(Line(self._p_upper_l, p_lower_l), wall_color)

        wall_color = "black" if self.has_right_wall else "white"
        self._win.draw_line(Line(p_upper_r, self._p_lower_r), wall_color)

        wall_color = "black" if self.has_top_wall else "white"
        self._win.draw_line(Line(self._p_upper_l, p_upper_r), wall_color)

        wall_color = "black" if self.has_bottom_wall else "white"
        self._win.draw_line(Line(p_lower_l, self._p_lower_r), wall_color)

    def center(self):
        x = self._p_upper_l.x + (self._p_lower_r.x - self._p_upper_l.x)
        y = self._p_upper_l.y + (self._p_lower_r.y - self._p_upper_l.y)
        return Point(x, y)

    def draw_move(self, to_cell, undo=False):
        fill_color = "gray" if undo else "red"
        self._win.draw_line(Line(self.center(), to_cell.center()), fill_color)
