def solve(input):
    # Calculate the number of 5s in each row and column
    row_counts = [row.count(5) for row in input]
    col_counts = [col.count(5) for col in zip(*input)]
    
    # Initialize the output grid with zeros
    output = [[0 for _ in range(len(input[0]))] for _ in range(len(input))]
    
    # Define the mapping from counts to output values
    count_to_value = {0: 2, 1: 3, 2: 4, 3: 3}
    
    # Fill the output grid based on the counts
    for i in range(len(input)):
        for j in range(len(input[0])):
            # The output value is determined by the sum of the counts from the corresponding row and column
            output[i][j] = count_to_value[row_counts[i] + col_counts[j]]
    
    return output

# Test case
input_test = [[0, 0, 5], [5, 0, 0], [0, 5, 0]]
print(solve(input_test))