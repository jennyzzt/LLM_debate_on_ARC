def solve(input_grid):
    # Initialize the output grid with the same dimensions as the input grid, filled with zeros.
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Copy the input grid to the output grid
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            output_grid[i][j] = input_grid[i][j]
    
    # Check for horizontal lines of three or more '1's and change them to '2's in the output grid.
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0]) - 2):  # Subtract 2 to avoid index out of range
            if input_grid[i][j] == 1 and input_grid[i][j+1] == 1 and input_grid[i][j+2] == 1:
                output_grid[i][j] = 2
                output_grid[i][j+1] = 2
                output_grid[i][j+2] = 2
    
    # Check for vertical lines of three or more '1's and change them to '2's in the output grid.
    for i in range(len(input_grid) - 2):  # Subtract 2 to avoid index out of range
        for j in range(len(input_grid[0])):
            if input_grid[i][j] == 1 and input_grid[i+1][j] == 1 and input_grid[i+2][j] == 1:
                output_grid[i][j] = 2
                output_grid[i+1][j] = 2
                output_grid[i+2][j] = 2
    
    return output_grid

# Test case
input_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1], 
    [0, 1, 1, 1, 0, 0, 0, 0, 1, 0], 
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0], 
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 1], 
    [0, 1, 1, 1, 0, 0, 0, 0, 1, 1]
]

output = solve(input_grid)
for row in output:
    print(row)