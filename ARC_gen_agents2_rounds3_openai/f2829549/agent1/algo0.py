def solve(input):
    output = [[0 for _ in range(3)] for _ in range(4)]  # Initialize output grid with zeros
    
    for i, row in enumerate(input):
        # Check for '7' in the first three columns
        if 7 in row[:3]:
            output[i][0] = 3
        # Check for '5' in the last three columns
        if 5 in row[-3:]:
            output[i][2] = 3
        # Deduce the rule for the second column based on the pattern observed
        # If both '7' and '5' are present in their respective areas, place a '3' in the second column
        if output[i][0] == 3 and output[i][2] == 3:
            output[i][1] = 3
        # If there's a '7' in the first three columns but no '5' in the last three, place a '3' in the second column
        elif output[i][0] == 3 and 5 not in row[-3:]:
            output[i][1] = 3
        # If there's a '5' in the last three columns but no '7' in the first three, place a '3' in the second column
        elif output[i][2] == 3 and 7 not in row[:3]:
            output[i][1] = 3
    
    return output

# Test case
input_test = [[0, 0, 0, 1, 0, 5, 0], [7, 7, 7, 1, 5, 5, 0], [0, 0, 0, 1, 5, 0, 0], [7, 0, 0, 1, 5, 5, 5]]
print(solve(input_test))