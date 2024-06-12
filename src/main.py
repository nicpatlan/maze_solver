import random
from graphics import Window, Point, Line 
from cell import Cell
from maze import Maze

def main():
    max_width = 800
    max_height = 600

    win = Window(max_width, max_height)
    seed = random.randrange(1000)
    maze = Maze(Point(30, 30), 11, 15, 50, 50, win, seed)

    win.wait_for_close()

main()
