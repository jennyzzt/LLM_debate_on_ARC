def solve(input_grid):
    # Copy the input grid to the output grid.
    output_grid = [row[:] for row in input_grid]
    
    # Get the dimensions of the grid.
    rows = len(input_grid)
    cols = len(input_grid[0])
    
    # Directions for adjacent cells (up, down, left, right).
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    # Iterate over each cell in the grid.
    for x in range(rows):
        for y in range(cols):
            # If the current cell is '8', check its adjacent cells.
            if input_grid[x][y] == 8:
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # If the adjacent cell is within bounds and is '0', change it to '1'.
                    if 0 <= nx < rows and 0 <= ny < cols and input_grid[nx][ny] == 0:
                        output_grid[nx][ny] = 1
    
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