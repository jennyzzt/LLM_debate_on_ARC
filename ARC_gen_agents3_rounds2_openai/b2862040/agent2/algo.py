def dfs(grid, x, y, visited):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or visited[x][y] or grid[x][y] != 1:
        return False
    
    # Mark the cell as visited
    visited[x][y] = True
    
    # Recursively visit all connecting cells
    dfs(grid, x+1, y, visited)
    dfs(grid, x-1, y, visited)
    dfs(grid, x, y+1, visited)
    dfs(grid, x, y-1, visited)
    
    return True

def solve(input_grid):
    rows, cols = len(input_grid), len(input_grid[0])
    output_grid = [row[:] for row in input_grid]  # Make a copy of the input grid
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if input_grid[i][j] == 1 and not visited[i][j]:
                # If DFS returns True, it means we have found a contiguous block of '1's.
                # We then need to transform these '1's into '8's.
                if dfs(input_grid, i, j, visited):
                    # Transform the contiguous block of '1's into '8's in the output grid.
                    # We need to run another DFS or similar logic to change the values,
                    # but since we've already marked visited cells, we can use that information.
                    for x in range(rows):
                        for y in range(cols):
                            if visited[x][y]:
                                output_grid[x][y] = 8
    
    return output_grid

# Test case
input_grid = [
    [1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9], 
    [9, 9, 9, 1, 1, 1, 1, 1, 9, 9, 9, 1, 9, 9, 9], 
    [9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 1, 9, 9, 9], 
    [9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 1, 9, 9, 9], 
    [9, 9, 9, 9, 1, 1, 1, 1, 9, 9, 9, 1, 9, 9, 1], 
    [9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 1, 1, 1, 1], 
    [1, 1, 1, 1, 9, 9, 9, 1, 9, 9, 9, 1, 9, 9, 1], 
    [1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1], 
    [1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1], 
    [1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 
    [9, 9, 9, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 9], 
    [9, 9, 9, 1, 9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9], 
    [9, 9, 9, 1, 9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9], 
    [9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 9]
]

output_grid = solve(input_grid)
for row in output_grid:
    print(row)