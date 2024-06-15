def solve(input_grid):
    # Determine the size of the grid
    n = len(input_grid)
    
    # Initialize the output grid with zeros
    output_grid = [[0 for _ in range(n)] for _ in range(n)]
    
    # Calculate the count of non-zero values in each row and column
    row_counts = [sum(1 for cell in row if cell != 0) for row in input_grid]
    col_counts = [sum(1 for row in input_grid if row[col] != 0) for col in range(n)]
    
    # Fill the output grid based on the pattern
    for i in range(n):
        for j in range(n):
            # The value is the sum of counts in the corresponding row and column, minus one if the cell is non-zero
            output_grid[i][j] = row_counts[i] + col_counts[j] - (1 if input_grid[i][j] != 0 else 0)
    
    return output_grid

# Test case
input_grid = [[0, 0, 5], [5, 0, 0], [0, 5, 0]]
print(solve(input_grid))