def solve(input_grid):
    # Create a copy of the input grid to modify it without altering the original input
    output_grid = [row[:] for row in input_grid]
    
    # Get the dimensions of the grid
    rows, cols = len(input_grid), len(input_grid[0])
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # Check if the current cell contains an 8
            if input_grid[r][c] == 8:
                # Check if we can place a 1 to the right
                if c + 1 < cols and input_grid[r][c + 1] == 0:
                    output_grid[r][c + 1] = 1
                # Otherwise, check if we can place a 1 below
                elif r + 1 < rows and input_grid[r + 1][c] == 0:
                    output_grid[r + 1][c] = 1
    
    return output_grid

# Test case
input_test = [
    [0, 0, 0, 0, 0, 8, 8],
    [8, 8, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 8, 8, 0, 0],
    [0, 8, 0, 0, 0, 0, 0],
    [8, 8, 0, 0, 0, 0, 0]
]

output_test = solve(input_test)
for row in output_test:
    print(row)