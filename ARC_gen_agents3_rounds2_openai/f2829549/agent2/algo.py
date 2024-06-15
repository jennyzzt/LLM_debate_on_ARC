def solve(input):
    # Initialize the output grid with zeros
    output = [[0, 0, 0] for _ in range(4)]
    
    # Apply the rules to fill the output grid
    for i in range(4):  # Iterate through each row
        # Rule for placing 3 in the top cell of a column
        if input[i][2] == 7:  # 7 to the left of 1
            output[i][0] = 3
        # Rule for placing 3 in the bottom cell of a column
        if input[i][4] == 5:  # 5 to the right of 1
            output[i][2] = 3
    
    # Additional rules for the middle cell
    for i in range(1, 4):  # Check for 7 above 1
        if input[i-1][3] == 7:
            output[i][1] = 3
    for i in range(3):  # Check for 5 below 1
        if input[i+1][3] == 5:
            output[i][1] = 3
    
    return output

# Test case
input_test = [[0, 0, 0, 1, 0, 5, 0], [7, 7, 7, 1, 5, 5, 0], [0, 0, 0, 1, 5, 0, 0], [7, 0, 0, 1, 5, 5, 5]]
print(solve(input_test))