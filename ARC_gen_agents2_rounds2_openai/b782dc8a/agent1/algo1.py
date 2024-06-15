def solve(input_grid):
    # Initialize the output grid with the same dimensions and values as the input grid
    output_grid = [row[:] for row in input_grid]
    
    # Define the sequence patterns observed in the demonstration
    pattern_3 = [2, 3]  # Pattern to apply after '3'
    pattern_4 = [1, 4]  # Pattern to apply after '4'
    
    # Iterate through the grid to apply transformations based on the patterns
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            # Check for the presence of '3' and apply the corresponding pattern
            if input_grid[i][j] == 3:
                for k, val in enumerate(pattern_3):
                    if j + k + 1 < len(input_grid[0]):  # Ensure we don't go out of bounds
                        output_grid[i][j + k + 1] = val
            
            # Check for the presence of '4' and apply the corresponding pattern
            elif input_grid[i][j] == 4:
                for k, val in enumerate(pattern_4):
                    if j + k + 1 < len(input_grid[0]):  # Ensure we don't go out of bounds
                        output_grid[i][j + k + 1] = val
    
    # Return the transformed output grid
    return output_grid

# Test case
input_grid = [
    [8, 8, 0, 8, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 8, 8, 8, 8, 4, 8, 8, 8, 8, 8, 8, 8],
    [0, 8, 0, 0, 0, 0, 4, 3, 8, 0, 0, 0, 0, 0, 8],
    [0, 8, 8, 8, 8, 8, 8, 4, 8, 8, 8, 0, 8, 8, 8],
    [0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 8, 0, 8, 0, 0],
    [8, 8, 8, 8, 8, 0, 8, 8, 8, 0, 8, 0, 8, 0, 8],
    [0, 0, 0, 0, 8, 0, 0, 0, 8, 0, 8, 0, 8, 0, 8],
    [8, 8, 8, 0, 8, 8, 8, 0, 8, 0, 8, 0, 8, 8, 8],
    [0, 0, 8, 0, 0, 0, 8, 0, 8, 0, 8, 0, 0, 0, 0],
    [8, 0, 8, 8, 8, 0, 8, 8, 8, 0, 8, 8, 8, 0, 8],
    [8, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 8, 0, 8],
    [8, 8, 8, 0, 8, 0, 8, 8, 8, 8, 8, 8, 8, 0, 8],
    [0, 0, 8, 0, 8, 0, 8, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 8, 8, 8, 0, 8, 0, 8, 8, 8, 8, 8, 8, 8],
    [8, 0, 0, 0, 0, 0, 8, 0, 8, 0, 0, 0, 0, 0, 0]
]

output_grid = solve(input_grid)
for row in output_grid:
    print(row)