import sys
def choose_next(x, y, size):
    if x == size:
        return 1
    if y == size:
        return 1
    return choose_next(x + 1, y, size) + choose_next(x, y + 1, size)


start = 1
a = 1
size = 21
"""
size = start
while start < size:
    print choose_next(0, 0, start)
    start += 1
"""
grid = [[1]*size for x in xrange(size)]
for x in range(1, size):
    for y in range(1, size):
        grid[x][y] = grid[x-1][y] + grid[x][y-1]

print grid[size - 1][size - 1]
