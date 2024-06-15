def solve(input_grid):
    # Copy the input grid to avoid modifying the original grid
    output_grid = [row[:] for row in input_grid]
    
    # Define the dimensions of the grid
    rows, cols = len(input_grid), len(input_grid[0])
    
    # Define the directions to check for adjacent cells
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If the current cell contains an '8'
            if input_grid[r][c] == 8:
                # Check all adjacent cells based on the defined directions
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # If the adjacent cell is within bounds and contains a '0', change it to '1'
                    if 0 <= nr < rows and 0 <= nc < cols and input_grid[nr][nc] == 0:
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

# Solve the test case and print the output
output = solve(input_grid)
for row in output:
    print(row)