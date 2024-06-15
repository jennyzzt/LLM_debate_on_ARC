def solve(input_grid):
    # Initialize the output grid with zeros, matching the size of the input grid
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Helper function to check if a cell contains a 5 and is within the grid bounds
    def is_five(x, y):
        return 0 <= x < len(input_grid) and 0 <= y < len(input_grid[0]) and input_grid[x][y] == 5
    
    # Iterate through each cell in the input grid
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            # If the current cell is a 5, determine its transformation
            if input_grid[i][j] == 5:
                # Check for horizontal and vertical adjacency
                horizontal_adj = is_five(i, j+1) or is_five(i, j-1)
                vertical_adj = is_five(i+1, j) or is_five(i-1, j)
                
                # Apply transformation rules based on adjacency
                if horizontal_adj and not vertical_adj:
                    output_grid[i][j] = 2
                elif vertical_adj and not horizontal_adj:
                    output_grid[i][j] = 3
                elif not vertical_adj and not horizontal_adj:
                    output_grid[i][j] = 1
                else:
                    # For cases where there's both horizontal and vertical adjacency,
                    # we default to the simpler transformation
                    output_grid[i][j] = 1
    
    return output_grid

# Test case
input_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 5], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 5], 
    [0, 0, 5, 5, 0, 5, 5, 0, 0, 5], 
    [0, 5, 5, 0, 0, 0, 5, 0, 0, 5], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [5, 0, 0, 5, 5, 0, 0, 5, 0, 0], 
    [5, 0, 0, 0, 0, 0, 0, 5, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

output_grid = solve(input_grid)
for row in output_grid:
    print(row)