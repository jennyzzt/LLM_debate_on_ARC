def solve(input_grid):
    # Initialize the output grid as a deep copy of the input grid
    output_grid = [row[:] for row in input_grid]
    
    # Get the dimensions of the grid
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    
    # Function to mark the cell to the left and above if they are '0'
    def mark_cell(r, c):
        if c > 0 and output_grid[r][c-1] == 0:  # Check and mark the cell to the left
            output_grid[r][c-1] = 1
        if r > 0 and output_grid[r-1][c] == 0:  # Check and mark the cell above
            output_grid[r-1][c] = 1
    
    # Iterate through each cell in the grid to find '8's and apply the transformation rule
    for i in range(rows):
        for j in range(cols):
            if input_grid[i][j] == 8:
                mark_cell(i, j)
    
    return output_grid

# Test case
input_grid = [
    [0, 0, 0, 0, 0, 8, 8],
    [8, 8, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 8, 8, 0, 0],
    [0, 8, 0, 0, 0, 0, 0],
    [8, 8, 0, 0, 0, 0, 0]
]

output = solve(input_grid)
for row in output:
    print(row)