def solve(input):
    output = [[0 for _ in range(3)] for _ in range(4)]  # Initialize output grid with zeros
    
    for i, row in enumerate(input):
        # Check for '7' in the first three columns
        if any(x == 7 for x in row[:3]):
            output[i][0] = 3
        # Check for '5' in the last three columns
        if any(x == 5 for x in row[-3:]):
            output[i][2] = 3
        # Determine the condition for the second column in the output grid
        if output[i][0] == 3 or output[i][2] == 3:
            output[i][1] = 3
    
    return output

# Test case
input_test = [[0, 0, 0, 1, 0, 5, 0], [7, 7, 7, 1, 5, 5, 0], [0, 0, 0, 1, 5, 0, 0], [7, 0, 0, 1, 5, 5, 5]]
output_test = solve(input_test)
for row in output_test:
    print(row)