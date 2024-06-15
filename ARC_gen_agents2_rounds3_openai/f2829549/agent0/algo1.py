def solve(input):
    output = [[0, 0, 0] for _ in range(4)]  # Initialize the output grid with zeros

    for i, row in enumerate(input):
        has_1 = 1 in row
        if has_1:
            index_1 = row.index(1)
            # Check for '7' before '1'
            if 7 in row[:index_1]:
                output[i][0] = 3
            # Check for '5' after '1'
            if 5 in row[index_1:]:
                output[i][2] = 3
            # Additional rule for the second column based on further analysis
            if row[index_1 + 1:].count(0) == len(row[index_1 + 1:]) - 1 and 5 in row[index_1 + 1:]:
                output[i][1] = 3
                if 7 in row[:index_1]:
                    output[i][1] = 0  # Adjust based on the presence of '7' before '1'

    return output

# Test case
input_test = [[0, 0, 0, 1, 0, 5, 0], [7, 7, 7, 1, 5, 5, 0], [0, 0, 0, 1, 5, 0, 0], [7, 0, 0, 1, 5, 5, 5]]
print(solve(input_test))