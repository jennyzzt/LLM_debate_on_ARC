def solve(input_grid):
    # Initialize the output grid with the same dimensions as the input grid
    output_grid = [[cell for cell in row] for row in input_grid]
    rows, cols = len(input_grid), len(input_grid[0])

    # Helper function to check if a cell is part of a vertical or horizontal line of three or more '1's
    def is_part_of_line(r, c):
        # Check horizontal line
        horizontal_count = 1
        for i in range(c - 1, -1, -1):
            if input_grid[r][i] == 1:
                horizontal_count += 1
            else:
                break
        for i in range(c + 1, cols):
            if input_grid[r][i] == 1:
                horizontal_count += 1
            else:
                break
        if horizontal_count >= 3:
            return True

        # Check vertical line
        vertical_count = 1
        for i in range(r - 1, -1, -1):
            if input_grid[i][c] == 1:
                vertical_count += 1
            else:
                break
        for i in range(r + 1, rows):
            if input_grid[i][c] == 1:
                vertical_count += 1
            else:
                break
        if vertical_count >= 3:
            return True

        return False

    # Apply the transformation rules to each cell
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