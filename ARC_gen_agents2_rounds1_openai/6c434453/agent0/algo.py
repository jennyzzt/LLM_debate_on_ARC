def solve(input_grid):
    # Initialize the output grid with the same dimensions as the input grid, filled with zeros
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Function to check if a cell should be transformed into a 2
    def should_transform(r, c):
        # Check horizontal line of three 1s
        if c < len(input_grid[0]) - 2 and input_grid[r][c] == 1 and input_grid[r][c+1] == 1 and input_grid[r][c+2] == 1:
            return True
        # Check vertical line of three 1s
        if r < len(input_grid) - 2 and input_grid[r][c] == 1 and input_grid[r+1][c] == 1 and input_grid[r+2][c] == 1:
            return True
        return False
    
    # Apply the transformation rules to each cell in the input grid
    for r in range(len(input_grid)):
        for c in range(len(input_grid[0])):
            if input_grid[r][c] == 1:
                # If the cell is part of a cluster that should be transformed, set it to 2
                if should_transform(r, c):
                    output_grid[r][c] = 2
                else:
                    # Otherwise, copy the value from the input grid
                    output_grid[r][c] = input_grid[r][c]
    
    return output_grid

# Test case
input_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1], [0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0], [0, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0, 0, 0, 0, 1, 1]
]

output = solve(input_grid)
for row in output:
    print(row)