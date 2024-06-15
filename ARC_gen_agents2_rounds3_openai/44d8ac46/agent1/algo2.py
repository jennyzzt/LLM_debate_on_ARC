def solve(input_grid):
    # Copy the input grid to avoid modifying the original grid
    output_grid = [row[:] for row in input_grid]
    
    # Get the number of rows and columns in the grid
    rows = len(input_grid)
    cols = len(input_grid[0])
    
    # Function to check if a cell is surrounded by '5's
    def is_surrounded_by_fives(r, c):
        # Check if the current cell is at the boundary or not surrounded by '5's
        if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
            return False
        # Check all four sides for '5's
        if input_grid[r-1][c] == 5 and input_grid[r+1][c] == 5 and input_grid[r][c-1] == 5 and input_grid[r][c+1] == 5:
            return True
        return False
    
    # Iterate through each cell in the grid, skipping the boundary cells
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            # If the cell is '0' and is surrounded by '5's, change its value to '2'
            if input_grid[i][j] == 0 and is_surrounded_by_fives(i, j):
                output_grid[i][j] = 2
                
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
for row in output_grid:
    print(row)