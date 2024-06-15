def solve(input_grid):
    # Initialize the output grid with the same dimensions as the input grid, filled with zeros.
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Initialize a counter to keep track of the occurrences of '5'.
    counter = 1
    
    # Iterate through each cell in the input grid.
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            # If the current cell value is '5', replace it with the current counter value in the output grid.
            if input_grid[i][j] == 5:
                output_grid[i][j] = counter
                # Increment the counter for the next occurrence of '5'.
                counter += 1
            # If the current cell value is not '5', it remains '0' as initialized in the output grid.
    
    # Return the transformed output grid.
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

# Solve the test case
output_grid = solve(input_grid)

# Print the output grid
for row in output_grid:
    print(row)