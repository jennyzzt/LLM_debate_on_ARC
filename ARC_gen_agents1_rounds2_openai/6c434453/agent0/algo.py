def solve(input_grid):
    rows, cols = len(input_grid), len(input_grid[0])
    output = [[cell for cell in row] for row in input_grid]  # Deep copy of the input grid

    # Function to check and mark cells that are part of a vertical or horizontal line of three '1's
    def mark_cells(r, c):
        # Check horizontal line of three '1's
        if c + 2 < cols and all(input_grid[r][c+i] == 1 for i in range(3)):
            for i in range(3):
                output[r][c+i] = 2
        # Check vertical line of three '1's
        if r + 2 < rows and all(input_grid[r+i][c] == 1 for i in range(3)):
            for i in range(3):
                output[r+i][c] = 2

    # Apply the transformation rules to each cell
    for r in range(rows):
        for c in range(cols):
            mark_cells(r, c)

    return output

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

output = solve(input_grid)
for row in output:
    print(row)