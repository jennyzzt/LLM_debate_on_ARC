def solve(input_grid):
    # Initialize the output grid as a deep copy of the input grid
    output_grid = [row[:] for row in input_grid]
    
    # Get the dimensions of the grid
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    
    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # Check if the current cell contains an 8 and is not on the right edge
            if input_grid[i][j] == 8 and j < cols - 1:
                # Place a 1 to the right of the 8
                output_grid[i][j + 1] = 1
    
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

output_grid = solve(input_grid)
for row in output_grid:
    print(row)