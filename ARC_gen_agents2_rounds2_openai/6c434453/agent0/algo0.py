def solve(input_grid):
    # Initialize the output grid with the same dimensions as the input grid, filled with zeros.
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Iterate through each cell in the input grid.
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            # Copy the value from the input grid to the output grid by default.
            output_grid[i][j] = input_grid[i][j]
            
            # Check for horizontal triplets.
            if j > 0 and j < len(input_grid[0]) - 1:
                if input_grid[i][j-1] == 1 and input_grid[i][j] == 1 and input_grid[i][j+1] == 1:
                    output_grid[i][j-1] = 2
                    output_grid[i][j] = 2
                    output_grid[i][j+1] = 2
            
            # Check for vertical triplets.
            if i > 0 and i < len(input_grid) - 1:
                if input_grid[i-1][j] == 1 and input_grid[i][j] == 1 and input_grid[i+1][j] == 1:
                    output_grid[i-1][j] = 2
                    output_grid[i][j] = 2
                    output_grid[i+1][j] = 2
    
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