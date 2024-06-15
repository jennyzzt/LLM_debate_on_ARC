def solve(input_grid):
    # Initialize the output grid with the same dimensions as the input grid
    output = [[cell for cell in row] for row in input_grid]  # Copy the input grid
    
    # Get the dimensions of the grid
    rows, cols = len(input_grid), len(input_grid[0])
    
    # Helper function to check if a cell should be changed to '2'
    def should_change(r, c):
        # Check horizontal line of three '1's
        if c + 2 < cols and input_grid[r][c] == 1 and input_grid[r][c+1] == 1 and input_grid[r][c+2] == 1:
            return True
        # Check vertical line of three '1's
        if r + 2 < rows and input_grid[r][c] == 1 and input_grid[r+1][c] == 1 and input_grid[r+2][c] == 1:
            return True
        return False
    
    # Apply the transformation rules
    for r in range(rows):
        for c in range(cols):
            if should_change(r, c):
                output[r][c] = 2
                output[r][c+1] = 2 if c + 1 < cols and input_grid[r][c+1] == 1 else output[r][c+1]
                output[r][c+2] = 2 if c + 2 < cols and input_grid[r][c+2] == 1 else output[r][c+2]
                output[r+1][c] = 2 if r + 1 < rows and input_grid[r+1][c] == 1 else output[r+1][c]
                output[r+2][c] = 2 if r + 2 < rows and input_grid[r+2][c] == 1 else output[r+2][c]
    
    return output

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