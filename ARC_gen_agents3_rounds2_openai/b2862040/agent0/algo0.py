def solve(input_grid):
    # Copy the input grid to the output grid.
    output_grid = [row[:] for row in input_grid]
    
    # Get the number of rows and columns in the grid.
    rows = len(input_grid)
    cols = len(input_grid[0])
    
    # Iterate through each cell in the grid except the border cells.
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            # Check if the current cell is '1'.
            if input_grid[i][j] == 1:
                # Check the cells around the current cell.
                if (input_grid[i-1][j] != 9 or input_grid[i+1][j] != 9 or
                    input_grid[i][j-1] != 9 or input_grid[i][j+1] != 9):
                    # Change the current cell to '8' in the output grid.
                    output_grid[i][j] = 8
    
    return output_grid

# Test case
input_test = [
    [1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9],
    [9, 9, 9, 1, 1, 1, 1, 1, 9, 9, 9, 1, 9, 9, 9],
    [9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 1, 9, 9, 9],
    [9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 1, 9, 9, 9],
    [9, 9, 9, 9, 1, 1, 1, 1, 9, 9, 9, 1, 9, 9, 1],
    [9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 1, 1, 1, 1],
    [1, 1, 1, 1, 9, 9, 9, 1, 9, 9, 9, 1, 9, 9, 1],
    [1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1],
    [1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1],
    [1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 9],
    [9, 9, 9, 1, 9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9],
    [9, 9, 9, 1, 9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9],
    [9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 9]
]

# Solve the test case
output_test = solve(input_test)

# Print the output grid
for row in output_test:
    print(row)