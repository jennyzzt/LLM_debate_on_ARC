def solve(input):
    # Initialize the output grid with the same dimensions as the input grid
    output = [[0 for _ in range(len(input[0]))] for _ in range(len(input))]
    
    # Iterate through each row of the input grid
    for i, row in enumerate(input):
        # Count the number of non-zero elements in the row
        non_zero_count = sum(1 for x in row if x != 0)
        
        # Determine the output value based on the positions of non-zero elements
        # This involves understanding the pattern from the demonstrations
        if non_zero_count == 1:
            # If there's only one non-zero element, it seems to correspond to a value of 3 in the output
            output_value = 3
        elif non_zero_count == 2:
            # If there are two non-zero elements, the output value seems to depend on their adjacency
            if row[1] != 0:  # Middle element is non-zero, suggesting a pattern
                output_value = 4
            else:
                output_value = 2
        elif non_zero_count == 3:
            # If all elements are non-zero, the output is filled with 3s
            output_value = 3
        else:
            # Default case if no non-zero elements are found
            output_value = 0
        
        # Fill the corresponding row in the output grid with the determined value
        output[i] = [output_value] * len(row)
    
    return output

# Test case
input_grid = [[0, 0, 5], [5, 0, 0], [0, 5, 0]]
print(solve(input_grid))