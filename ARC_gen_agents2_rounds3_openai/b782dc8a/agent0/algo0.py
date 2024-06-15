def solve(input_grid):
    # Initialize the output grid with the same dimensions as the input grid
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Example transformation rule (to be adjusted based on the actual task's rules)
    # For demonstration purposes, let's assume we need to replace 4 with 1, 3 with 2, and vice versa,
    # while keeping 8 and 0 unchanged. This rule is arbitrary and should be replaced with the actual rule.
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            if input_grid[i][j] == 4:
                output_grid[i][j] = 1
            elif input_grid[i][j] == 3:
                output_grid[i][j] = 2
            elif input_grid[i][j] == 1:
                output_grid[i][j] = 4
            elif input_grid[i][j] == 2:
                output_grid[i][j] = 3
            else:
                # Keep the number unchanged if it's not 1, 2, 3, or 4
                output_grid[i][j] = input_grid[i][j]
    
    return output_grid

# Test case
input_grid = [
    [8, 8, 0, 8, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 8, 8, 8, 8, 4, 8, 8, 8, 8, 8, 8, 8],
    [0, 8, 0, 0, 0, 0, 4, 3, 8, 0, 0, 0, 0, 0, 8],
    # ... Add the rest of the input grid rows
]

output_grid = solve(input_grid)
for row in output_grid:
    print(row)