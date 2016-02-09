__author__ = 'Paul'

# Here we count how many element equal 1 are nearby specified item.

grid = ((1, 0, 0, 1, 0),
        (0, 1, 0, 0, 0),
        (0, 0, 1, 0, 1),
        (1, 0, 0, 0, 0),
        (0, 0, 1, 0, 0),)

def count_neighbours(grid, row, col):
    count = 0
    NEIGHBORS = ((-1, -1), (-1, 0), (-1, 1),
                 (0, -1), (0, 1),
                 (1, -1), (1, 0), (1, 1))

    for diff in NEIGHBORS:
        n_row = row + diff[0]
        n_col = col + diff[1]
        if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[n_row]):
            if grid[n_row][n_col] == 1:
                count += 1
    return count



print(count_neighbours(grid, 1, 2))
