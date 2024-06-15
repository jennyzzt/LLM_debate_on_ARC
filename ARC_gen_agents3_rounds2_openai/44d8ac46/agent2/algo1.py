def solve(input_grid):
    # Copy the input grid to the output grid to avoid modifying the original grid.
    output_grid = [row[:] for row in input_grid]
    
    # Get the number of rows and columns in the grid.
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    
    # Iterate through each cell in the grid, avoiding the border cells.
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            # Check if the current cell is 0 and surrounded by 5s.
            if (input_grid[row][col] == 0 and
                input_grid[row-1][col] == 5 and
                input_grid[row+1][col] == 5 and
                input_grid[row][col-1] == 5 and
                input_grid[row][col+1] == 5):
                # Change the current cell to 2 in the output grid.
                output_grid[row][col] = 2
                
    return output_grid

# Test case
input_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [5, 5, 5, 5, 5, 0, 0, 5, 5, 5, 5, 0], 
    [5, 0, 0, 0, 5, 0, 0, 5, 5, 0, 5, 0], 
    [5, 0, 0, 0, 5, 0, 0, 5, 0, 0, 5, 0], 
    [5, 0, 0, 0, 5, 0, 0, 5, 0, 0, 5, 0], 
    [5, 5, 5, 5, 5, 0, 0, 5, 5, 5, 5, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0], 
    [0, 0, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0], 
    [0, 0, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0], 
    [0, 0, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0]
]

# Solve the test case and print the output grid
output_grid = solve(input_grid)
for row in output_grid:
    print(row)