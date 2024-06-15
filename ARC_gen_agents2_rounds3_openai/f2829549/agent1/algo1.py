def solve(input):
    # Initialize the output grid with zeros
    output = [[0 for _ in range(3)] for _ in range(4)]
    
    # Iterate through each row to check conditions based on the positions of 1 and 5
    for i in range(4):
        # Check for '1' in the fourth column and adjust conditions around it
        if input[i][3] == 1:
            # Check for '5' to the right of '1'
            if 5 in input[i][4:]:
                output[i][2] = 3
            # Check for '5' in the same row but not necessarily to the right of '1'
            if 5 in input[i]:
                output[i][1] = 3
            # If '7' is present in the row, it might influence the first column
            if 7 in input[i][:3]:
                output[i][0] = 3
            # Additional checks can be added based on further pattern analysis
            
    return output

# Test case
input_test = [[0, 0, 0, 1, 0, 5, 0], [7, 7, 7, 1, 5, 5, 0], [0, 0, 0, 1, 5, 0, 0], [7, 0, 0, 1, 5, 5, 5]]
output_test = solve(input_test)
for row in output_test:
    print(row)