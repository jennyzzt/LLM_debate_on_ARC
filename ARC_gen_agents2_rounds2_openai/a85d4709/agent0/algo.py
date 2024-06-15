def solve(input_grid):
    # Initialize the output grid with zeros
    output = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Function to count non-zero elements in a list
    def count_non_zero(lst):
        return sum(1 for x in lst if x != 0)
    
    # Iterate through each cell in the input grid
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            # Count non-zero elements in the current row and column
            row_count = count_non_zero(input_grid[i])
            col_count = count_non_zero([input_grid[x][j] for x in range(len(input_grid))])
            
            # Calculate the value for the output grid cell
            # Subtract 1 if the current cell is non-zero since it's counted in both row and column
            output[i][j] = row_count + col_count - (1 if input_grid[i][j] != 0 else 0)
    
    return output

# Test case
input_grid = [[0, 0, 5], [5, 0, 0], [0, 5, 0]]
print(solve(input_grid))