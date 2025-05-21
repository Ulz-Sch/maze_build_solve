import unittest
from graphics import *

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(maze.num_cols,num_cols)
        self.assertEqual(maze.num_rows,num_rows)

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(maze.num_cols,num_cols)
        self.assertEqual(maze.num_rows,num_rows)
        
    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1.cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )




if __name__ == "__main__":
    unittest.main()