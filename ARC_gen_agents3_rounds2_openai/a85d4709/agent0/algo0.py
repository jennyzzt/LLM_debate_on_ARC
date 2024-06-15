def solve(input_grid):
    # Initialize the output grid with zeros, having the same dimensions as the input grid
    output = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Iterate through each cell in the input grid
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            # Count non-zero values in the current row and column
            row_count = sum(1 for value in input_grid[i] if value != 0)
            col_count = sum(1 for row in input_grid if row[j] != 0)
            
            # Assign the sum of row_count and col_count to the corresponding cell in the output grid
            output[i][j] = row_count + col_count
            
    return output

# Test case
input_grid = [[0, 0, 5], [5, 0, 0], [0, 5, 0]]
print(solve(input_grid))