def solve(input_grid):
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    output_grid = [[cell for cell in row] for row in input_grid]  # Copy input grid

    # Function to check if a cell is part of a vertical or horizontal line of three '1's
    def is_part_of_line_of_three(r, c):
        # Check horizontal line of three '1's
        horizontal_checks = [
            (c + 2 < cols and input_grid[r][c] == 1 and input_grid[r][c + 1] == 1 and input_grid[r][c + 2] == 1),
            (c - 1 >= 0 and c + 1 < cols and input_grid[r][c] == 1 and input_grid[r][c - 1] == 1 and input_grid[r][c + 1] == 1),
            (c - 2 >= 0 and input_grid[r][c] == 1 and input_grid[r][c - 1] == 1 and input_grid[r][c - 2] == 1)
        ]
        # Check vertical line of three '1's
        vertical_checks = [
            (r + 2 < rows and input_grid[r][c] == 1 and input_grid[r + 1][c] == 1 and input_grid[r + 2][c] == 1),
            (r - 1 >= 0 and r + 1 < rows and input_grid[r][c] == 1 and input_grid[r - 1][c] == 1 and input_grid[r + 1][c] == 1),
            (r - 2 >= 0 and input_grid[r][c] == 1 and input_grid[r - 1][c] == 1 and input_grid[r - 2][c] == 1)
        ]
        return any(horizontal_checks) or any(vertical_checks)

    # Apply transformation rule
    for r in range(rows):
        for c in range(cols):
            if is_part_of_line_of_three(r, c):
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