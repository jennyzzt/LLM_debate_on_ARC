def solve(input_grid):
    rows, cols = len(input_grid), len(input_grid[0])
    output_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    # Helper function to check if a cell is part of a horizontal or vertical sequence of three '1's
    def is_part_of_sequence(r, c):
        # Check horizontal sequence
        horizontal = sum(1 for dx in range(max(0, c-2), min(cols, c+3)) if input_grid[r][dx] == 1) >= 3
        # Check vertical sequence
        vertical = sum(1 for dy in range(max(0, r-2), min(rows, r+3)) if input_grid[dy][c] == 1) >= 3
        return horizontal or vertical

    # Transform the input grid based on the sequence rule
    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] == 1 and is_part_of_sequence(r, c):
                output_grid[r][c] = 2
            else:
                output_grid[r][c] = input_grid[r][c]

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