def solve(input):
    # Initialize the output grid with zeros
    output = [[0 for _ in range(len(input[0]))] for _ in range(len(input))]
    
    # Iterate through each row of the input grid
    for i, row in enumerate(input):
        # Count the number of non-zero elements and their positions
        non_zero_positions = [index for index, value in enumerate(row) if value != 0]
        
        # If there are no non-zero elements, continue to the next row
        if not non_zero_positions:
            continue
        
        # Calculate the number of steps needed to move the non-zero elements to form a continuous line
        steps = max(non_zero_positions) - min(non_zero_positions) + 1
        
        # Fill the corresponding row in the output grid with the calculated steps
        output[i] = [steps] * len(row)
    
    return output

# Test case
input_grid = [[0, 0, 5], [5, 0, 0], [0, 5, 0]]
print(solve(input_grid))