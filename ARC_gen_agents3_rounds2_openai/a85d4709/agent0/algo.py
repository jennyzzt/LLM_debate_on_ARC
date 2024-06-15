def solve(input_grid):
    # Initialize the output grid with zeros
    output = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Calculate the sum of non-zero elements in each row and column
    row_sums = [sum(1 for cell in row if cell != 0) for row in input_grid]
    col_sums = [sum(1 for row in input_grid if row[col] != 0) for col in range(len(input_grid[0]))]
    
    # Fill the output grid based on the rule deduced
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            if input_grid[i][j] == 0:
                # If the cell is zero, just sum the non-zero counts in its row and column
                output[i][j] = row_sums[i] + col_sums[j]
            else:
                # If the cell is non-zero, subtract 1 after summing (to avoid double counting)
                output[i][j] = row_sums[i] + col_sums[j] - 1
                
    return output

# Test case
input_grid = [[0, 0, 5], [5, 0, 0], [0, 5, 0]]
print(solve(input_grid))