def solve(input_grid):
    # Initialize the output grid with zeros, matching the size of the input grid
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Calculate the count of non-zero elements in each row and column
    row_counts = [sum(1 for x in row if x != 0) for row in input_grid]
    col_counts = [sum(1 for row in input_grid if row[col] != 0) for col in range(len(input_grid[0]))]
    
    # Fill the output grid based on the sum of counts in corresponding row and column
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            # The output value for each cell is determined by the sum of its row and column counts
            output_grid[i][j] = row_counts[i] + col_counts[j]
    
    return output_grid

# Test case
input_grid = [[0, 0, 5], [5, 0, 0], [0, 5, 0]]
print(solve(input_grid))