def solve(input_grid):
    rows = len(input_grid)
    cols = len(input_grid[0])
    
    # Function to check if a cell is surrounded by '9's or at the edge
    def is_changeable(x, y):
        if input_grid[x][y] != 1:
            return False
        # Edge cells are not changeable
        if x == 0 or x == rows - 1 or y == 0 or y == cols - 1:
            return False
        # Check surrounding cells
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if input_grid[nx][ny] != 9:
                return True
        return False

    # Copy the input grid to the output grid
    output_grid = [row[:] for row in input_grid]

    # Iterate through the grid and apply the transformation rule
    for i in range(1, rows - 1):  # Exclude the border
        for j in range(1, cols - 1):  # Exclude the border
            if is_changeable(i, j):
                output_grid[i][j] = 8

    return output_grid

# Test case
input_grid = [
    [1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9],
    [9, 9, 9, 1, 1, 1, 1, 1, 9, 9, 9, 1, 9, 9, 9],
    [9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 1, 9, 9, 9],
    [9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 1, 9, 9, 9],
    [9, 9, 9, 9, 1, 1, 1, 1, 9, 9, 9, 1, 9, 9, 1],
    [9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 1, 1, 1, 1],
    [1, 1, 1, 1, 9, 9, 9, 1, 9, 9, 9, 1, 9, 9, 1],
    [1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1],
    [1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1],
    [1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 9],
    [9, 9, 9, 1, 9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9],
    [9, 9, 9, 1, 9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9],
    [9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 9]
]

output_grid = solve(input_grid)
for row in output_grid:
    print(row)