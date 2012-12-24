from utils.main import main

"""
Starting in the top left corner of a 22 grid, there are 6 routes (without
backtracking) to the bottom right corner.


How many routes are there through a 2020 grid?
"""

def find_option_through_grid(size):
    grid = [[1]*size for x in xrange(size)]
    for x in range(1, size):
        for y in range(1, size):
            grid[x][y] = grid[x-1][y] + grid[x][y-1]

    return grid[size - 1][size - 1]


if __name__ == '__main__':
    main(find_option_through_grid, 21)
