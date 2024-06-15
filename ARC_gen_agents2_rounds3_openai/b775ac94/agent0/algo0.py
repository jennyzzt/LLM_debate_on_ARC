def solve(input):
    # Initialize the output grid with the same dimensions as the input grid
    output = [[0 for _ in range(len(input[0]))] for _ in range(len(input))]
    
    # Loop through each cell in the input grid
    for i in range(len(input)):
        for j in range(len(input[0])):
            # Apply transformation rules based on the value of the current cell
            if input[i][j] == 8:
                # For value 8, replicate it and spread as observed in the demonstrations
                output[i][j] = 8
                if i+1 < len(input):
                    output[i+1][j] = 8
                if j+1 < len(input[0]):
                    output[i][j+1] = 8
                if i+1 < len(input) and j+1 < len(input[0]):
                    output[i+1][j+1] = 8
            elif input[i][j] == 4:
                # For value 4, replicate it in a specific pattern
                output[i][j] = 4
                if j+1 < len(input[0]):
                    output[i][j+1] = 4
            elif input[i][j] == 3:
                # For value 3, replicate it in a specific pattern
                output[i][j] = 3
                if i+1 < len(input):
                    output[i+1][j] = 3
            elif input[i][j] == 2:
                # For value 2, replicate it in a specific pattern
                output[i][j] = 2
                if i+1 < len(input):
                    output[i+1][j] = 2
                if j+1 < len(input[0]):
                    output[i][j+1] = 2
                if i+1 < len(input) and j+1 < len(input[0]):
                    output[i+1][j+1] = 2
            elif input[i][j] == 1:
                # For value 1, replicate it in a specific pattern
                output[i][j] = 1
                if i+1 < len(input):
                    output[i+1][j] = 1
                if i-1 >= 0:
                    output[i-1][j] = 1
                if j+1 < len(input[0]):
                    output[i][j+1] = 1
                if j-1 >= 0:
                    output[i][j-1] = 1

    # Return the transformed output grid
    return output

# Test case
input_test = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 8, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 8, 8, 2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 4, 3, 0, 0, 0, 0, 0, 0, 1, 1, 1, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Call the solve function with the test case
output_test = solve(input_test)

# Print the output grid
for row in output_test:
    print(row)