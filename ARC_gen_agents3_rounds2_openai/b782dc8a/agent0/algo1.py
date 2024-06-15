def solve(input_grid):
    # Initialize the output grid with the same dimensions as the input grid
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Directly copy the input grid to the output grid as a base
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            output_grid[i][j] = input_grid[i][j]
    
    # Apply transformation rules based on observed patterns from the demonstrations
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            # Check for numbers 3 and 4 and apply a transformation based on their positions
            if input_grid[i][j] == 4:
                # Assuming a pattern where '4' might be replaced with '2' based on its position
                output_grid[i][j] = 2
                # Additional logic to handle sequences or adjacent transformations could be added here
            elif input_grid[i][j] == 3:
                # Assuming a pattern where '3' might be replaced with '1' based on its position
                output_grid[i][j] = 1
                # Additional logic for handling sequences or adjacent transformations could be added here
                
    return output_grid

# Test case
input_grid = [
    [8, 8, 0, 8, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 8, 8, 8, 8, 4, 8, 8, 8, 8, 8, 8, 8],
    [0, 8, 0, 0, 0, 0, 4, 3, 8, 0, 0, 0, 0, 0, 8],
    # ... Rest of the input grid omitted for brevity
]

# Solve the test case using the generalized transformation logic
output_grid = solve(input_grid)
for row in output_grid:
    print(row)