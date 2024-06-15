def solve(input_grid):
    # Copy the input grid to the output grid
    output_grid = [row[:] for row in input_grid]
    
    # Get the number of rows and columns in the grid
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    
    # Iterate through each cell in the grid
    for row in range(1, rows-1):  # Avoid the edges
        for col in range(1, cols-1):  # Avoid the edges
            
            # Check if the current cell is '0' and surrounded by '5's
            if input_grid[row][col] == 0:
                if (input_grid[row-1][col] == 5 and
                    input_grid[row+1][col] == 5 and
                    input_grid[row][col-1] == 5 and
                    input_grid[row][col+1] == 5):
                    # Replace '0' with '2' in the output grid
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

output_grid = solve(input_grid)

# Print the output grid
for row in output_grid:
    print(row)