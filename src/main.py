from graphics import Window, Point, Line 
from cell import Cell
from maze import Maze

def main():
    max_width = 800
    max_height = 600

    win = Window(max_width, max_height)

    maze = Maze(Point(10, 10), 10, 10, 50, 50, win)

    win.wait_for_close()

main()
