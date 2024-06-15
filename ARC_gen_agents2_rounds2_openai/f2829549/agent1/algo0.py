def solve(input_grid):
    # Initialize the output grid with zeros
    output = [[0 for _ in range(3)] for _ in range(4)]
    
    # Loop through each row of the input grid
    for i in range(4):
        # Check for '7' in the first three columns
        if 7 in input_grid[i][:3]:
            output[i][0] = 3
        # The second column in the output is always filled based on the presence of '1' in the fourth column
        if input_grid[i][3] == 1:
            output[i][1] = 3
        # Check for '5' in the last three columns
        if any(x == 5 for x in input_grid[i][-3:]):
            output[i][2] = 3
    
    return output

# Test case
input_grid = [[0, 0, 0, 1, 0, 5, 0], [7, 7, 7, 1, 5, 5, 0], [0, 0, 0, 1, 5, 0, 0], [7, 0, 0, 1, 5, 5, 5]]
print(solve(input_grid))