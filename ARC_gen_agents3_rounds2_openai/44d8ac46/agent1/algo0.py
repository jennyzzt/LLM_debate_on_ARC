def solve(input_grid):
    # Copy the input grid to the output grid.
    output_grid = [row[:] for row in input_grid]
    
    # Iterate through each cell in the grid.
    for i in range(len(input_grid)):
        for j in range(len(input_grid[i])):
            # Check if the current cell is a '0' and is surrounded by '5's.
            # We need to check the cells to the left, right, above, and below the current cell.
            if input_grid[i][j] == 0:
                surrounded_by_5 = True
                # Check above
                if i > 0 and input_grid[i-1][j] != 5:
                    surrounded_by_5 = False
                # Check below
                if i < len(input_grid)-1 and input_grid[i+1][j] != 5:
                    surrounded_by_5 = False
                # Check left
                if j > 0 and input_grid[i][j-1] != 5:
                    surrounded_by_5 = False
                # Check right
                if j < len(input_grid[i])-1 and input_grid[i][j+1] != 5:
                    surrounded_by_5 = False
                
                # If the cell is surrounded by '5's, replace it with '2'.
                if surrounded_by_5:
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