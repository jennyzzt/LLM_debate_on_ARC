def solve(input_grid):
    # Copy the input grid to avoid modifying it directly
    output_grid = [row[:] for row in input_grid]
    
    # Dimensions of the grid
    rows, cols = len(input_grid), len(input_grid[0])
    
    # Directions for adjacent cells: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If the current cell is '8', check its adjacent cells
            if input_grid[r][c] == 8:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # If the adjacent cell is within the grid and is '0', mark it as '1'
                    if 0 <= nr < rows and 0 <= nc < cols and output_grid[nr][nc] == 0:
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

# Solve the test case and print the output grid
output_grid = solve(input_grid)
for row in output_grid:
    print(row)