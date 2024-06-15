def solve(input_grid):
    # Initialize the output grid with the same dimensions as the input grid, copying the original values.
    output_grid = [[cell for cell in row] for row in input_grid]
    rows, cols = len(input_grid), len(input_grid[0])

    # Function to check if a cell is part of a horizontal or vertical line of three '1's.
    def is_part_of_line(r, c):
        # Check horizontal line
        if c + 2 < cols and input_grid[r][c] == 1 and input_grid[r][c + 1] == 1 and input_grid[r][c + 2] == 1:
            return True
        # Check vertical line
        if r + 2 < rows and input_grid[r][c] == 1 and input_grid[r + 1][c] == 1 and input_grid[r + 2][c] == 1:
            return True
        return False

    # Process each cell in the input grid
    for r in range(rows):
        for c in range(cols):
            # If the cell is part of a line, set its value to '2' in the output grid.
            if is_part_of_line(r, c):
                output_grid[r][c] = 2

    return output_grid

# Test case
input_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1], [0, 1, 1, 1, 0, 0, 0, 0, 1, 0], 
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0], [0, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0, 1, 1], 
    [0, 1, 1, 1, 0, 0, 0, 0, 1, 1]
]

output_grid = solve(input_grid)
for row in output_grid:
    print(row)