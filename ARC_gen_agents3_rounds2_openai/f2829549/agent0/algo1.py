def solve(input):
    # Initialize the output grid with zeros
    output = [[0, 0, 0] for _ in range(4)]
    
    for i in range(4):  # Loop through each row
        # Check for '7' in the first three columns of the input
        if 7 in input[i][:3]:
            output[i][0] = 3
        # Check for '1' in the fourth column of the input (always true based on demonstrations)
        if input[i][3] == 1:
            output[i][1] = 3
        # Check for '5' in the last three columns of the input
        if 5 in input[i][-3:]:
            output[i][2] = 3
            
    return output

# Test case
input_test = [[0, 0, 0, 1, 0, 5, 0], [7, 7, 7, 1, 5, 5, 0], [0, 0, 0, 1, 5, 0, 0], [7, 0, 0, 1, 5, 5, 5]]
print(solve(input_test))