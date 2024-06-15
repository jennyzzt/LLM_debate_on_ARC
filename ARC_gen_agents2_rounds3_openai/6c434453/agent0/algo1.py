def solve(input_grid):
    rows, cols = len(input_grid), len(input_grid[0])
    output_grid = [[cell for cell in row] for row in input_grid]  # Copy the input grid to the output grid

    # Function to mark '1's that are part of a horizontal or vertical line of three or more '1's
    def mark_convertible_ones():
        for r in range(rows):
            for c in range(cols):
                # Check for horizontal line of three or more '1's
                if c <= cols - 3 and all(input_grid[r][c+i] == 1 for i in range(3)):
                    output_grid[r][c] = 2
                    i = 1
                    while c+i < cols and input_grid[r][c+i] == 1:
                        output_grid[r][c+i] = 2
                        i += 1

                # Check for vertical line of three or more '1's
                if r <= rows - 3 and all(input_grid[r+i][c] == 1 for i in range(3)):
                    output_grid[r][c] = 2
                    i = 1
                    while r+i < rows and input_grid[r+i][c] == 1:
                        output_grid[r+i][c] = 2
                        i += 1

    # Apply the transformation rules
    mark_convertible_ones()

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