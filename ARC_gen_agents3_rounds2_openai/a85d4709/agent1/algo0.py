def solve(input_grid):
    # Initialize the output grid with the same dimensions as the input grid
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Iterate through each row of the input grid
    for i, row in enumerate(input_grid):
        # Count the number of non-zero elements in the current row
        non_zero_count = sum(1 for element in row if element != 0)
        
        # Determine the output value based on the count of non-zero elements
        if non_zero_count == 1 or non_zero_count == 3:
            output_value = 3
        elif non_zero_count == 2:
            output_value = 4
        else:
            output_value = 2  # Default case, though not observed in the demonstrations
        
        # Fill the corresponding row in the output grid with the determined output value
        output_grid[i] = [output_value for _ in range(len(row))]
    
    return output_grid

# Test case
input_grid = [[0, 0, 5], [5, 0, 0], [0, 5, 0]]
print(solve(input_grid))