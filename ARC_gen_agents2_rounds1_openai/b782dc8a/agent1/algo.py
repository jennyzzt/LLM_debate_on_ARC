def solve(input_grid):
    # Initialize the output grid with the same dimensions as the input grid
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Iterate through the grid to apply transformation rules
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            # Directly copy the 8s from the input to the output
            if input_grid[i][j] == 8:
                output_grid[i][j] = 8
            # For cells containing 4, spread or alternate with 3 based on some observed pattern
            elif input_grid[i][j] == 4:
                # This is a placeholder for the actual logic, which needs to be inferred
                output_grid[i][j] = 4  # Example action, replace with actual logic
                # You might want to check adjacent cells and apply a specific pattern
            # For cells containing 3, apply a similar logic
            elif input_grid[i][j] == 3:
                output_grid[i][j] = 3  # Example action, replace with actual logic
            # Handle other numbers based on observed patterns
            else:
                # Placeholder for handling other numbers
                pass
    
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

# Call the solve function with the test case
output_grid = solve(input_grid)
# Print the output grid
for row in output_grid:
    print(row)