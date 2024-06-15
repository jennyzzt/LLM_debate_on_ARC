def solve(input_grid):
    # Initialize the output grid with zeros, having the same dimensions as the input grid
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Iterate through each cell in the input grid
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            # Count non-zero numbers in the current row and column
            count = 0
            # Count in row
            for k in range(len(input_grid[0])):
                if input_grid[i][k] != 0:
                    count += 1
            # Count in column
            for l in range(len(input_grid)):
                if input_grid[l][j] != 0 and l != i:  # Avoid double counting the cell itself
                    count += 1
            # Assign the count to the corresponding cell in the output grid
            output_grid[i][j] = count
    
    return output_grid

# Test case
input_grid = [[0, 0, 5], [5, 0, 0], [0, 5, 0]]
print(solve(input_grid))