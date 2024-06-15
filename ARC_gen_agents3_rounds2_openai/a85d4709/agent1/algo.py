def solve(input_grid):
    # Initialize the output grid with zeros, same size as input_grid
    size = len(input_grid)
    output_grid = [[0 for _ in range(size)] for _ in range(size)]
    
    # Function to count non-zero elements in a row
    def count_non_zero_row(row):
        return sum(1 for cell in input_grid[row] if cell != 0)
    
    # Function to count non-zero elements in a column
    def count_non_zero_col(col):
        return sum(1 for row in input_grid if row[col] != 0)
    
    # Fill the output grid
    for row in range(size):
        for col in range(size):
            # Count non-zero elements in the corresponding row and column
            row_count = count_non_zero_row(row)
            col_count = count_non_zero_col(col)
            # Subtract 1 if the current cell in input_grid is non-zero (to avoid double counting)
            if input_grid[row][col] != 0:
                output_grid[row][col] = row_count + col_count - 1
            else:
                output_grid[row][col] = row_count + col_count
    
    return output_grid

# Test case
input_grid = [[0, 0, 5], [5, 0, 0], [0, 5, 0]]
print(solve(input_grid))