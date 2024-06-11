from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("closing window...")

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, p1, p2):
        self.__p1 = p1
        self.__p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.__p1.x, 
                           self.__p1.y, 
                           self.__p2.x, 
                           self.__p2.y, 
                           fill=fill_color, 
                           width=2)

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
