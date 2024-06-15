def solve(input_grid):
    # Copy the input grid to avoid modifying the original grid
    output_grid = [row[:] for row in input_grid]
    
    # Get the dimensions of the grid
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    
    # Directions for adjacent cells (up, down, left, right)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If the current cell contains an 8
            if input_grid[r][c] == 8:
                # Check all adjacent cells
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # If the adjacent cell is within bounds and not an 8, change it to 1
                    if 0 <= nr < rows and 0 <= nc < cols and input_grid[nr][nc] != 8:
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

output_grid = solve(input_grid)

# Print the output grid
for row in output_grid:
    print(row)