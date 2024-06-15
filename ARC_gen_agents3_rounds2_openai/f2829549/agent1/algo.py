def solve(input_grid):
    output_grid = [[0 for _ in range(3)] for _ in range(4)]  # Initialize a 4x3 grid of zeros
    
    for i, row in enumerate(input_grid):
        index_of_1 = row.index(1)  # Find the index of '1' in the current row
        
        # Check for '7' before '1'
        if 7 in row[:index_of_1]:
            output_grid[i][0] = 3
        # Check for '7' after '1'
        if 7 in row[index_of_1:]:
            output_grid[i][1] = 3
        # Check for '5' after '1'
        if 5 in row[index_of_1:]:
            output_grid[i][2] = 3
    
    return output_grid

# Test case
input_test = [[0, 0, 0, 1, 0, 5, 0], [7, 7, 7, 1, 5, 5, 0], [0, 0, 0, 1, 5, 0, 0], [7, 0, 0, 1, 5, 5, 5]]
output_test = solve(input_test)
print(output_test)