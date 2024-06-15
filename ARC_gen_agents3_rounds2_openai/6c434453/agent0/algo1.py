def solve(input_grid):
    rows, cols = len(input_grid), len(input_grid[0])
    output_grid = [[cell for cell in row] for row in input_grid]  # Copy the input grid

    # Helper function to check and transform a group of three '1's into '2's
    def check_and_transform(r, c):
        # Horizontal check
        if c + 2 < cols and all(input_grid[r][c+i] == 1 for i in range(3)):
            for i in range(3):
                output_grid[r][c+i] = 2
        # Vertical check
        if r + 2 < rows and all(input_grid[r+i][c] == 1 for i in range(3)):
            for i in range(3):
                output_grid[r+i][c] = 2

    # Apply the transformation rules to each cell in the grid
    for r in range(rows):
        for c in range(cols):
            check_and_transform(r, c)

    return output_grid

# Test case
input_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0, 0, 0, 0, 1, 1]
]

output_grid = solve(input_grid)
for row in output_grid:
    print(row)