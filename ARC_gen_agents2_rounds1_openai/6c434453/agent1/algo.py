def solve(input_grid):
    rows, cols = len(input_grid), len(input_grid[0])
    output_grid = [[cell for cell in row] for row in input_grid]  # Copy input grid

    # Function to check if a cell is part of a horizontal line of three or more '1's
    def check_horizontal(r, c):
        count = 1
        # Check to the right
        for i in range(c + 1, cols):
            if input_grid[r][i] == 1:
                count += 1
            else:
                break
        # Check to the left
        for i in range(c - 1, -1, -1):
            if input_grid[r][i] == 1:
                count += 1
            else:
                break
        return count >= 3

    # Function to check if a cell is part of a vertical line of three or more '1's
    def check_vertical(r, c):
        count = 1
        # Check downwards
        for i in range(r + 1, rows):
            if input_grid[i][c] == 1:
                count += 1
            else:
                break
        # Check upwards
        for i in range(r - 1, -1, -1):
            if input_grid[i][c] == 1:
                count += 1
            else:
                break
        return count >= 3

    # Update the output grid based on the rules
    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] == 1 and (check_horizontal(r, c) or check_vertical(r, c)):
                output_grid[r][c] = 2

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

output = solve(input_grid)
for row in output:
    print(row)