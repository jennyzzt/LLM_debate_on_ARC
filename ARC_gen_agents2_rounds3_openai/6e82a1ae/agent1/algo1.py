def dfs(grid, x, y, cluster_number):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 5:
        return
    grid[x][y] = cluster_number
    dfs(grid, x+1, y, cluster_number)
    dfs(grid, x-1, y, cluster_number)
    dfs(grid, x, y+1, cluster_number)
    dfs(grid, x, y-1, cluster_number)

def solve(input_grid):
    cluster_number = 1
    # Create a copy of the input grid to modify without altering the original input
    grid_copy = [row[:] for row in input_grid]
    for i in range(len(grid_copy)):
        for j in range(len(grid_copy[0])):
            if grid_copy[i][j] == 5:
                dfs(grid_copy, i, j, cluster_number)
                cluster_number += 1
    return grid_copy

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

output_grid = solve(input_grid)
for row in output_grid:
    print(row)