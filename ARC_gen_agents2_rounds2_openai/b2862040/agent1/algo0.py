def solve(input_grid):
    # Copy the input grid to the output grid.
    output_grid = [row[:] for row in input_grid]
    rows = len(input_grid)
    cols = len(input_grid[0])

    # Function to check if a cell should be transformed to 8.
    def should_transform_to_8(r, c):
        transform = False
        # Check horizontally
        if c > 0 and c < cols - 1 and input_grid[r][c - 1] == 1 and input_grid[r][c + 1] == 1:
            transform = True
        # Check vertically
        if r > 0 and r < rows - 1 and input_grid[r - 1][c] == 1 and input_grid[r + 1][c] == 1:
            transform = True
        return transform

    # Iterate through the grid and apply the transformation rules.
    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] == 1:
                if should_transform_to_8(r, c):
                    output_grid[r][c] = 8

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