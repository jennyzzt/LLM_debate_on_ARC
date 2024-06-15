def solve(input_grid):
    # Copy the input grid to avoid modifying it directly
    output = [row[:] for row in input_grid]
    
    # Get the dimensions of the grid
    rows = len(input_grid)
    cols = len(input_grid[0])
    
    # Directions to check around each '8' (up, down, left, right)
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If the cell contains an '8'
            if input_grid[r][c] == 8:
                # Check each of the four directions
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    # If the adjacent cell is within bounds and empty, place a '1'
                    if 0 <= new_r < rows and 0 <= new_c < cols and input_grid[new_r][new_c] == 0:
                        output[new_r][new_c] = 1
                        
    return output

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