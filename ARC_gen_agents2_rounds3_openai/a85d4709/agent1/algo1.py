def solve(input_grid):
    # Initialize the output grid with the same dimensions as the input grid
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Iterate through each row of the input grid
    for i, row in enumerate(input_grid):
        # Count the number of non-zero elements in the current row
        non_zero_count = sum(1 for x in row if x != 0)
        
        # Determine the value to fill based on the number of non-zero elements
        if non_zero_count == 1:
            fill_value = 3
        elif non_zero_count == 2:
            fill_value = 4
        elif non_zero_count == 3:
            fill_value = 2
        else:
            fill_value = 0  # This case is just for completeness, though not expected based on the task description
        
        # Fill the corresponding row in the output grid with the determined value
        output_grid[i] = [fill_value for _ in row]
    
    return output_grid

# Test case
input_grid = [[0, 0, 5], [5, 0, 0], [0, 5, 0]]
output = solve(input_grid)
print(output)