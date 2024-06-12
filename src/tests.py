import unittest
from graphics import Point
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

        num_cols = 2
        num_rows = 10
        m1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

        num_cols = 3
        num_rows = 2
        m1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_entrance_and_exit(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
        ent_cell = m1._cells[0][0]
        exit_cell = m1._cells[9][9]
        ent_wall = (not (ent_cell.has_left_wall and
                         ent_cell.has_top_wall))
        exit_wall = (not (exit_cell.has_right_wall and
                          exit_cell.has_bottom_wall))
        self.assertEqual(True, (ent_wall and exit_wall))
 
if __name__ == "__main__":
    unittest.main()
