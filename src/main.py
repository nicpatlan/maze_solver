from graphics import Window, Point, Line 
from cell import Cell

def main():
    max_width = 800
    max_height = 600

    win = Window(max_width, max_height)

    cells = []

    for i in range(10, 210, 20):
        cell = Cell(win, Point(i, i), Point(i + 10, i + 10))

        n = len(cells)
        if n == 0:
            cell.has_top_wall = False
        elif n == 1:
            cell.has_bottom_wall = False
        elif n == 2:
            cell.has_left_wall = False
        elif n == 3:
            cell.has_right_wall = False
        elif n == 4:
            cell.has_top_wall = cell.has_bottom_wall = False
        elif n == 5:
            cell.has_right_wall = cell.has_left_wall = False
        elif n == 6:
            cell.has_right_wall = cell.has_top_wall = False
        elif n == 7:
            cell.has_right_wall = cell.has_bottom_wall = False
        elif n == 8:
            cell.has_left_wall = cell.has_top_wall = False
        else:
            cell.has_left_wall = cell.has_bottom_wall = False

        cells.append(cell)

    for cell in cells:
        cell.draw() 

    for i in range(5, 0, -1):
        cells[i].draw_move(cells[i - 1])

    for i in range(5, 9):
        cells[i].draw_move(cells[i + 1], undo=True)

    win.wait_for_close()

main()
