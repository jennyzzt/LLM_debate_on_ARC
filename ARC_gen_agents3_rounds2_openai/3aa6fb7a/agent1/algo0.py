def solve(input_grid):
    # Copy the input grid to avoid modifying the original grid
    output_grid = [row[:] for row in input_grid]
    
    # Get the dimensions of the grid
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    
    # Function to check if a position is valid and the cell is empty
    def is_valid_and_empty(r, c):
        return 0 <= r < rows and 0 <= c < cols and input_grid[r][c] == 0
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If the current cell contains an 8, check its adjacent cells
            if input_grid[r][c] == 8:
                # Check above
                if is_valid_and_empty(r-1, c):
                    output_grid[r-1][c] = 1
                # Check below
                if is_valid_and_empty(r+1, c):
                    output_grid[r+1][c] = 1
                # Check left
                if is_valid_and_empty(r, c-1):
                    output_grid[r][c-1] = 1
                # Check right
                if is_valid_and_empty(r, c+1):
                    output_grid[r][c+1] = 1
    
    return output_grid

# Test case
input_grid = [
    [0, 0, 0, 0, 0, 8, 8],
    [8, 8, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 8, 8, 0, 0],
    [0, 8, 0, 0, 0, 0, 0],
    [8, 8, 0, 0, 0, 0, 0]
]

output = solve(input_grid)
for row in output:
    print(row)