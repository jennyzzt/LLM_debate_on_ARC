def solve(input_grid):
    output_grid = [[0 for _ in range(3)] for _ in range(4)]  # Initialize a 4x3 grid with zeros
    
    for i in range(4):  # Iterate through each row
        # Check for 7 in the first three columns
        if 7 in input_grid[i][:3]:
            output_grid[i][0] = 3
        # Check for 5 in the fifth or sixth column for the second column of the output
        if 5 in input_grid[i][4:6]:
            output_grid[i][1] = 3
        # Check for 5 in the fifth or seventh column for the third column of the output
        if 5 in [input_grid[i][4], input_grid[i][6]]:
            output_grid[i][2] = 3
    
    return output_grid

# Test case
input_test = [[0, 0, 0, 1, 0, 5, 0], [7, 7, 7, 1, 5, 5, 0], [0, 0, 0, 1, 5, 0, 0], [7, 0, 0, 1, 5, 5, 5]]
print(solve(input_test))