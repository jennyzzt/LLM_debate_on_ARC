def solve(input):
    output = [[0, 0, 0] for _ in range(4)]  # Initialize the output grid with zeros
    
    for i, row in enumerate(input):
        # Find the index of the first occurrence of '1' if it exists
        if 1 in row:
            index_1 = row.index(1)
            
            # First Column Rule: Check for at least two '7's before '1'
            sevens_before_1 = row[:index_1].count(7)
            if sevens_before_1 >= 2:
                output[i][0] = 3
            
            # Second Column Rule: Check for a '5' immediately after '1'
            if index_1 + 1 < len(row) and row[index_1 + 1] == 5:
                output[i][1] = 3
            
            # Third Column Rule: Check for at least two '5's after '1'
            fives_after_1 = row[index_1:].count(5)
            if fives_after_1 >= 2:
                output[i][2] = 3
    
    return output

# Test case
input_test = [[0, 0, 0, 1, 0, 5, 0], [7, 7, 7, 1, 5, 5, 0], [0, 0, 0, 1, 5, 0, 0], [7, 0, 0, 1, 5, 5, 5]]
print(solve(input_test))