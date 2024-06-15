def solve(input_grid):
    # Initialize the output grid with the same dimensions as the input grid
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Copy the input grid to the output grid as a starting point
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            output_grid[i][j] = input_grid[i][j]
    
    # Apply transformation based on observed patterns
    for i in range(1, len(input_grid) - 1):
        for j in range(1, len(input_grid[0]) - 1):
            # Check for special numbers (other than 8 and 0) and apply a transformation
            if input_grid[i][j] not in [0, 8]:
                # As an example, let's attempt to increment surrounding numbers
                # This is a simplified assumption and might not reflect the actual pattern
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if input_grid[i + di][j + dj] not in [0, 8]:
                            output_grid[i + di][j + dj] = (input_grid[i + di][j + dj] + 1) % 5
                        elif input_grid[i + di][j + dj] == 0:
                            # Attempt to spread the value to empty spaces
                            output_grid[i + di][j + dj] = (input_grid[i][j] + 1) % 5
    
    return output_grid

# Test case input
test_input = [
    [8, 8, 0, 8, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 8, 8, 8, 8, 4, 8, 8, 8, 8, 8, 8, 8],
    [0, 8, 0, 0, 0, 0, 4, 3, 8, 0, 0, 0, 0, 0, 8],
    # ... remaining rows omitted for brevity
]

# Solve the test case
test_output = solve(test_input)

# Print the output grid
for row in test_output:
    print(row)