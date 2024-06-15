def solve(input_grid):
    # Initialize the output grid with the same dimensions as the input grid
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Iterate through each row in the input grid
    for i, row in enumerate(input_grid):
        # Count the number of non-zero elements in the current row
        non_zero_count = sum(1 for x in row if x != 0)
        
        # The output value for each cell in this row is non_zero_count + 1
        output_value = non_zero_count + 1
        
        # Update the output grid with the calculated output value for this row
        output_grid[i] = [output_value for _ in row]
    
    return output_grid

# Test case
input_grid = [[0, 0, 5], [5, 0, 0], [0, 5, 0]]
print(solve(input_grid))