def solve(input):
    # Initialize the output grid with zeros
    output = [[0 for _ in range(3)] for _ in range(4)]
    
    # Define a function to check the presence of 7 and 5 around 1
    def check_around(row):
        idx_1 = row.index(1) if 1 in row else -1
        has_7_left = any(x == 7 for x in row[:idx_1])
        has_5_right = any(x == 5 for x in row[idx_1+1:])
        return has_7_left, has_5_right
    
    # Apply the rule to each row
    for i, row in enumerate(input):
        has_7_left, has_5_right = check_around(row)
        # Adjust the output based on the presence of 7 and 5
        if has_7_left and has_5_right:
            output[i] = [0, 3, 0]
        elif has_7_left:
            output[i][1] = 3
        elif has_5_right:
            output[i][2] = 3
    
    return output

# Test case
input_test = [[0, 0, 0, 1, 0, 5, 0], [7, 7, 7, 1, 5, 5, 0], [0, 0, 0, 1, 5, 0, 0], [7, 0, 0, 1, 5, 5, 5]]
print(solve(input_test))