def solve(input_grid):
    # Copy the input grid to avoid modifying the original grid
    output_grid = [row[:] for row in input_grid]
    
    # Define the dimensions of the grid
    rows, cols = len(input_grid), len(input_grid[0])
    
    # Function to check if a position is within the grid bounds
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # Check if the current cell contains an '8'
            if input_grid[r][c] == 8:
                # Check all four adjacent cells (up, down, left, right)
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    # If the adjacent cell is within bounds and contains a '0', change it to '1'
                    if is_valid(nr, nc) and input_grid[nr][nc] == 0:
                        output_grid[nr][nc] = 1
                        
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