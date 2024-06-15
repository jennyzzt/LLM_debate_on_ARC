def solve(input):
    output = [[0, 0, 0] for _ in range(4)]  # Initialize the output grid with zeros
    
    for i, row in enumerate(input):
        # Check for two '7's before the '1'
        if row.count(7) >= 2 and row.index(1) > row.index(7, row.index(7) + 1):
            output[i][0] = 3
        
        # Check for a '5' immediately after the '1'
        if 1 in row and row.index(1) + 1 < len(row) and row[row.index(1) + 1] == 5:
            output[i][1] = 3
        
        # Check for two '5's after the '1'
        if row.count(5) >= 2 and 1 in row:
            index_1 = row.index(1)
            five_counts_after_1 = sum(1 for x in row[index_1+1:] if x == 5)
            if five_counts_after_1 >= 2:
                output[i][2] = 3
    
    return output

# Test case
test_input = [[0, 0, 0, 1, 0, 5, 0], [7, 7, 7, 1, 5, 5, 0], [0, 0, 0, 1, 5, 0, 0], [7, 0, 0, 1, 5, 5, 5]]
print(solve(test_input))