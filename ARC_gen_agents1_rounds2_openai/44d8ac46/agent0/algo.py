def solve(input_grid):
    # Determine the size of the grid
    rows = len(input_grid)
    cols = len(input_grid[0])
    
    # Create a copy of the input grid to store the output
    output = [[cell for cell in row] for row in input_grid]
    
    # Function to check if a cell is surrounded by 5s
    def is_surrounded_by_5(r, c):
        # Check all four directions
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Left, Right, Up, Down
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # If any of the surrounding cells is not 5, return False
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or input_grid[nr][nc] != 5:
                return False
        return True
    
    # Iterate through the grid and apply the transformation rule
    for r in range(1, rows - 1):  # Exclude the outermost rows
        for c in range(1, cols - 1):  # Exclude the outermost columns
            if input_grid[r][c] == 5 and is_surrounded_by_5(r, c):
                output[r][c] = 2  # Change the cell value to 2
    
    return output

# Test case
input_test = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [5, 5, 5, 5, 5, 0, 0, 5, 5, 5, 5, 0], 
    [5, 0, 0, 0, 5, 0, 0, 5, 5, 0, 5, 0], 
    [5, 0, 0, 0, 5, 0, 0, 5, 0, 0, 5, 0], 
    [5, 0, 0, 0, 5, 0, 0, 5, 0, 0, 5, 0], 
    [5, 5, 5, 5, 5, 0, 0, 5, 5, 5, 5, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0], 
    [0, 0, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0], 
    [0, 0, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0], 
    [0, 0, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0]
]

# Solve the test case
output_test = solve(input_test)

# Print the output grid
for row in output_test:
    print(row)