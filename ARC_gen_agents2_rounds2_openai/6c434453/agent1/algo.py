def solve(input_grid):
    rows, cols = len(input_grid), len(input_grid[0])
    output_grid = [[cell for cell in row] for row in input_grid]  # Copy the input grid

    # Helper function to check if a cell is part of a horizontal or vertical line of three or more '1's
    def is_part_of_line(r, c):
        # Check horizontal line
        horizontal_count = 1
        for delta in [-1, 1]:  # Check left and right
            i = 1
            while 0 <= c + delta * i < cols and input_grid[r][c + delta * i] == 1:
                horizontal_count += 1
                i += 1
        if horizontal_count >= 3:
            return True

        # Check vertical line
        vertical_count = 1
        for delta in [-1, 1]:  # Check up and down
            i = 1
            while 0 <= r + delta * i < rows and input_grid[r + delta * i][c] == 1:
                vertical_count += 1
                i += 1
        if vertical_count >= 3:
            return True

        return False

    # Apply the transformation rule
    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] == 1 and is_part_of_line(r, c):
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