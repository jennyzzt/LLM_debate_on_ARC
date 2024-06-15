def flood_fill(grid, x, y, new_value):
    # Base case: if the current position is out of bounds or not equal to 5, return 0.
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 5:
        return 0
    
    # Replace the current cell with the new value.
    grid[x][y] = new_value
    
    # Count the current cell.
    count = 1
    
    # Recursively count and fill the connected cells in all four directions.
    count += flood_fill(grid, x + 1, y, new_value)
    count += flood_fill(grid, x - 1, y, new_value)
    count += flood_fill(grid, x, y + 1, new_value)
    count += flood_fill(grid, x, y - 1, new_value)
    
    return count

def solve(input_grid):
    # Create a copy of the input grid to modify.
    output_grid = [row[:] for row in input_grid]
    
    # Iterate through each cell in the grid.
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            # If the current cell is a 5, perform a flood fill to count and replace the group.
            if input_grid[i][j] == 5:
                count = flood_fill(output_grid, i, j, -1) # Temporarily mark with -1.
                flood_fill(output_grid, i, j, count) # Replace -1 with the actual count.
    
    return output_grid

# Test case
input_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 5], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 5], 
    [0, 0, 5, 5, 0, 5, 5, 0, 0, 5], 
    [0, 5, 5, 0, 0, 0, 5, 0, 0, 5], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [5, 0, 0, 5, 5, 0, 0, 5, 0, 0], 
    [5, 0, 0, 0, 0, 0, 0, 5, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

output = solve(input_grid)
for row in output:
    print(row)