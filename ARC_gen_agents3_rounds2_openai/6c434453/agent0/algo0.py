def solve(input_grid):
    # Initialize the output grid with the same dimensions as the input grid
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Function to check if a '1' should be transformed into a '2'
    def should_transform_to_2(r, c):
        # Check horizontally
        if c > 0 and c < len(input_grid[0]) - 1 and input_grid[r][c-1] == 1 and input_grid[r][c+1] == 1:
            return True
        # Check vertically
        if r > 0 and r < len(input_grid) - 1 and input_grid[r-1][c] == 1 and input_grid[r+1][c] == 1:
            return True
        return False
    
    # Apply the transformation rules to each cell
    for r in range(len(input_grid)):
        for c in range(len(input_grid[0])):
            if input_grid[r][c] == 1:
                output_grid[r][c] = 2 if should_transform_to_2(r, c) else 1
            else:
                output_grid[r][c] = 0
                
    return output_grid

# Test case
input_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1], 
    [0, 1, 1, 1, 0, 0, 0, 0, 1, 0], 
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0], 
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 1], 
    [0, 1, 1, 1, 0, 0, 0, 0, 1, 1]
]

output_grid = solve(input_grid)
for row in output_grid:
    print(row)