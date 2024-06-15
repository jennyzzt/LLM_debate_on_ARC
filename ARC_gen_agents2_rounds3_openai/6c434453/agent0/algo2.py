def solve(input_grid):
    # Initialize the output grid with the same dimensions as the input grid
    output_grid = [[cell for cell in row] for row in input_grid]
    rows, cols = len(input_grid), len(input_grid[0])

    # Helper function to check if a cell is part of a vertical or horizontal line of exactly three '1's
    def is_part_of_line(r, c):
        # Check horizontal line of exactly three '1's
        if c + 2 < cols and input_grid[r][c] == 1 and input_grid[r][c + 1] == 1 and input_grid[r][c + 2] == 1:
            if (c - 1 >= 0 and input_grid[r][c - 1] == 1) or (c + 3 < cols and input_grid[r][c + 3] == 1):
                return False
            return True

        # Check vertical line of exactly three '1's
        if r + 2 < rows and input_grid[r][c] == 1 and input_grid[r + 1][c] == 1 and input_grid[r + 2][c] == 1:
            if (r - 1 >= 0 and input_grid[r - 1][c] == 1) or (r + 3 < rows and input_grid[r + 3][c] == 1):
                return False
            return True

        return False

    # Apply the transformation rules to each cell
    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] == 1 and is_part_of_line(r, c):
                output_grid[r][c] = 2
                # Mark the rest of the line as '2'
                if c + 2 < cols and input_grid[r][c + 1] == 1 and input_grid[r][c + 2] == 1:
                    output_grid[r][c + 1] = 2
                    output_grid[r][c + 2] = 2
                if r + 2 < rows and input_grid[r + 1][c] == 1 and input_grid[r + 2][c] == 1:
                    output_grid[r + 1][c] = 2
                    output_grid[r + 2][c] = 2

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