def solve(input_grid):
    # Initialize the output grid with the same dimensions as the input grid
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Iterate through each row of the input grid
    for i, row in enumerate(input_grid):
        # Count the number of non-zero elements in the current row
        non_zero_count = sum(1 for cell in row if cell != 0)
        # Calculate the value to fill in the output grid based on the corrected rule
        fill_value = non_zero_count + 1  # Corrected increment to +1 for each non-zero element
        # Fill the corresponding row in the output grid with the calculated value
        output_grid[i] = [fill_value for _ in row]
    
    return output_grid

# Test case
input_grid = [[0, 0, 5], [5, 0, 0], [0, 5, 0]]
output = solve(input_grid)
print(output)