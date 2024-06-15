def solve(input):
    output = [[0, 0, 0] for _ in range(4)]  # Initialize the output grid with zeros
    
    for i in range(4):  # Iterate through each row
        # Check for '7's in the left section (first three columns of the input)
        if 7 in input[i][:3]:
            output[i][0] = 3
        # Check for '5's in the right section (last three columns of the input)
        if 5 in input[i][4:]:
            output[i][2] = 3
        # If there are '7's in the left and '5's in the right section, place '3' in the middle column of the output
        if (7 in input[i][:3]) and (5 in input[i][4:]):
            output[i][1] = 3
    
    return output

# Test case
test_input = [[0, 0, 0, 1, 0, 5, 0], [7, 7, 7, 1, 5, 5, 0], [0, 0, 0, 1, 5, 0, 0], [7, 0, 0, 1, 5, 5, 5]]
print(solve(test_input))