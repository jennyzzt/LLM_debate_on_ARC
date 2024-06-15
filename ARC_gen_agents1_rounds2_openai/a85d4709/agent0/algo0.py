def solve(input_grid):
    # Initialize the output grid with zeros, having the same dimensions as the input grid
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Iterate through each cell in the input grid
    for row in range(len(input_grid)):
        for col in range(len(input_grid[0])):
            # If the current cell is non-zero, increment the count for the corresponding row and column in the output grid
            if input_grid[row][col] != 0:
                # Increment counts for the entire row and column in the output grid
                for i in range(len(input_grid)):
                    output_grid[i][col] += 1
                for j in range(len(input_grid[0])):
                    output_grid[row][j] += 1
    
    # Adjust counts to account for double counting of the cell where row and column intersect
    for row in range(len(input_grid)):
        for col in range(len(input_grid[0])):
            if input_grid[row][col] != 0:
                output_grid[row][col] -= 1
    
    return output_grid

# Test case
input_grid = [[0, 0, 5], [5, 0, 0], [0, 5, 0]]
output = solve(input_grid)
print(output)