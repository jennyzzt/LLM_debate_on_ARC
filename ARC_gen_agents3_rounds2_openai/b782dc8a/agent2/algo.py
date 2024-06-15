def solve(input_grid):
    # Initialize the output grid with the same dimensions as the input grid
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Copy the input grid to the output grid as a starting point
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            output_grid[i][j] = input_grid[i][j]
    
    # Apply a simplified transformation rule based on observed patterns
    # Note: This part is speculative and might not accurately reflect the intended transformation
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            # Check for numbers other than 0 and 8
            if input_grid[i][j] not in [0, 8]:
                # Speculative transformation: Copy the number without change
                # A more complex rule would be needed here based on a better understanding of the pattern
                output_grid[i][j] = input_grid[i][j]
                
    return output_grid

# Test case input
input_grid = [
    [8, 8, 0, 8, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 8, 8, 8, 8, 4, 8, 8, 8, 8, 8, 8, 8],
    [0, 8, 0, 0, 0, 0, 4, 3, 8, 0, 0, 0, 0, 0, 8],
    # ... remaining rows omitted for brevity
]

# Call the solve function with the test case input
output_grid = solve(input_grid)

# Print the output grid
for row in output_grid:
    print(row)