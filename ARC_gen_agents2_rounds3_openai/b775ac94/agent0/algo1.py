def solve(input_grid):
    # Initialize the output grid with the same dimensions as the input grid
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Copy the input grid to the output grid
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            output_grid[i][j] = input_grid[i][j]
    
    # Apply transformations based on observed patterns
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            value = input_grid[i][j]
            
            # Check and apply transformation for value 8
            if value == 8:
                if i+1 < len(input_grid):
                    output_grid[i+1][j] = max(output_grid[i+1][j], 8)
                if j+1 < len(input_grid[0]):
                    output_grid[i][j+1] = max(output_grid[i][j+1], 8)
                if i+1 < len(input_grid) and j+1 < len(input_grid[0]):
                    output_grid[i+1][j+1] = max(output_grid[i+1][j+1], 8)
            
            # Check and apply transformation for value 4
            if value == 4 and j+1 < len(input_grid[0]):
                output_grid[i][j+1] = max(output_grid[i][j+1], 4)
            
            # Check and apply transformation for value 3
            if value == 3 and i+1 < len(input_grid):
                output_grid[i+1][j] = max(output_grid[i+1][j], 3)
            
            # Check and apply transformation for value 2
            if value == 2:
                if i+1 < len(input_grid):
                    output_grid[i+1][j] = max(output_grid[i+1][j], 2)
                if j+1 < len(input_grid[0]):
                    output_grid[i][j+1] = max(output_grid[i][j+1], 2)
                if i+1 < len(input_grid) and j+1 < len(input_grid[0]):
                    output_grid[i+1][j+1] = max(output_grid[i+1][j+1], 2)
            
            # Check and apply transformation for value 1
            if value == 1:
                if i-1 >= 0:
                    output_grid[i-1][j] = max(output_grid[i-1][j], 1)
                if i+1 < len(input_grid):
                    output_grid[i+1][j] = max(output_grid[i+1][j], 1)
                if j-1 >= 0:
                    output_grid[i][j-1] = max(output_grid[i][j-1], 1)
                if j+1 < len(input_grid[0]):
                    output_grid[i][j+1] = max(output_grid[i][j+1], 1)
    
    # Return the transformed output grid
    return output_grid

# Define the input grid for the test case
input_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # ... Add the rest of the input grid rows here
]

# Solve the test case
output_grid = solve(input_grid)

# Print the output grid
for row in output_grid:
    print(row)