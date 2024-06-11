from graphics import Line, Point

class Cell():
    def __init__(self, win, p1, p2):
        self.__win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__p_upper_l = p1
        self.__p_lower_r = p2

    def draw(self):
        if self.has_left_wall or self.has_bottom_wall:
            p_lower_l = Point(self.__p_upper_l.x,
                          self.__p_lower_r.y)
            if self.has_left_wall:
                line = Line(self.__p_upper_l, p_lower_l)
                self.__win.draw_line(line, "black")
            if self.has_bottom_wall:
                line = Line(p_lower_l, self.__p_lower_r)
                self.__win.draw_line(line, "black") 
        if self.has_right_wall or self.has_top_wall:
            p_upper_r = Point(self.__p_lower_r.x, 
                          self.__p_upper_l.y)
            if self.has_right_wall:            
                line = Line(p_upper_r, self.__p_lower_r)
                self.__win.draw_line(line, "black")
            if self.has_top_wall:
                line = Line(self.__p_upper_l, p_upper_r)
                self.__win.draw_line(line, "black")

    def center(self):
        x = self.__p_upper_l.x + (self.__p_lower_r.x - self.__p_upper_l.x)
        y = self.__p_upper_l.y + (self.__p_lower_r.y - self.__p_upper_l.y)
        return Point(x, y)

    def draw_move(self, to_cell, undo=False):
        fill_color = "gray" if undo else "red"
        self.__win.draw_line(Line(self.center(), to_cell.center()), fill_color)
