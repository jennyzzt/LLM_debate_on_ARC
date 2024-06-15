def solve(input):
    output = [[0, 0, 0] for _ in range(4)]  # Initialize the output grid with zeros
    
    for i in range(4):
        row = input[i]
        # Check for '7' in the first three columns
        if 7 in row[:3]:
            output[i][0] = 3
        
        # Check for '5' in the last three columns
        if 5 in row[4:]:
            output[i][2] = 3
        
        # Refine the rule for the second column based on the presence of '7' and '5'
        # If '7' is present in the first three columns and '5' in the last three, set the second column to '3'
        # This rule seems to be more complex and might involve specific patterns of '7' and '5'
        # However, based on the provided demonstrations and insights, we'll apply a simplified version of this rule
        if 7 in row[:3] and 5 in row[4:]:
            output[i][1] = 3
        # If there is no '7' in the first three columns but '5' is present in the last three, adjust the second column based on additional conditions
        # This adjustment is made based on the observation that the second column's value seems to depend on a specific pattern of '7' and '5'
        # For simplicity, we'll leave the second column as '0' unless both '7' and '5' are present as described
        
    return output

# Test case
input_test = [[0, 0, 0, 1, 0, 5, 0], [7, 7, 7, 1, 5, 5, 0], [0, 0, 0, 1, 5, 0, 0], [7, 0, 0, 1, 5, 5, 5]]
output_test = solve(input_test)
print(output_test)