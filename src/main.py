from graphics import Window, Point, Line

def main():
    max_width = 800
    max_height = 600

    win = Window(max_width, max_height)

    line = Line(Point(0, 0), Point(max_width, max_height))
    win.draw_line(line, "red")

    win.wait_for_close()

main()
