def solve(input):
    # Initialize the output grid with zeros
    output = [[0 for _ in range(3)] for _ in range(4)]
    
    # Define the conditions for filling each cell in the output grid
    # These conditions are based on the analysis of the demonstration examples
    conditions = [
        (lambda row: 7 in row[:3] or 5 in row[4:]),  # Condition for the first column in output
        (lambda row: 7 in row[1:4]),                 # Condition for the second column in output
        (lambda row: 5 in row[3:] or 7 in row[2:5])  # Condition for the third column in output
    ]
    
    # Iterate through each row in the input grid
    for i, row in enumerate(input):
        # Check each condition
        for j, condition in enumerate(conditions):
            # If the condition is met, set the corresponding cell in the output grid to 3
            if condition(row):
                output[i][j] = 3
    
    return output

# Test case
input_test = [[0, 0, 0, 1, 0, 5, 0], [7, 7, 7, 1, 5, 5, 0], [0, 0, 0, 1, 5, 0, 0], [7, 0, 0, 1, 5, 5, 5]]
print(solve(input_test))