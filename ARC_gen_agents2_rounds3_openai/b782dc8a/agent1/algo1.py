def solve(input):
    # Initialize the output grid with the same dimensions as the input grid
    output = [[8 for _ in range(len(input[0]))] for _ in range(len(input))]
    
    # Iterate through the input grid to find and transform numbers other than 8
    for i in range(len(input)):
        for j in range(len(input[0])):
            # Directly copy the number if it's 8
            if input[i][j] == 8:
                output[i][j] = 8
            else:
                # Apply a transformation rule for numbers other than 8
                # This is a simplified example of how one might start to implement the transformation
                # based on the observed patterns. It needs to be refined.
                num = input[i][j]
                if num == 0:
                    output[i][j] = 0  # Assuming 0 remains unchanged
                elif num == 4:
                    # Spread the 4 in some pattern, for example, to adjacent cells
                    output[i][j] = 4
                    if i > 0: output[i-1][j] = 3  # Example transformation
                    if j > 0: output[i][j-1] = 2  # Example transformation
                elif num == 3:
                    output[i][j] = 3  # Assuming 3 remains unchanged or follows a specific pattern
                # Additional transformation rules for 1 and 2 can be added here
    
    return output

# Test case
input_grid = [
    [8, 8, 0, 8, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 8, 8, 8, 8, 4, 8, 8, 8, 8, 8, 8, 8],
    [0, 8, 0, 0, 0, 0, 4, 3, 8, 0, 0, 0, 0, 0, 8],
    # ... (rest of the input grid)
]

output_grid = solve(input_grid)
for row in output_grid:
    print(row)