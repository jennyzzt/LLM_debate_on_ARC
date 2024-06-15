def dfs(grid, x, y, cluster_number):
    # Base condition to stop recursion
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 5:
        return
    # Mark the current cell with the cluster number
    grid[x][y] = cluster_number
    # Recursively explore adjacent cells (up, down, left, right)
    dfs(grid, x+1, y, cluster_number)
    dfs(grid, x-1, y, cluster_number)
    dfs(grid, x, y+1, cluster_number)
    dfs(grid, x, y-1, cluster_number)

def solve(input_grid):
    cluster_number = 1  # Initialize cluster numbering from 1
    # Create a copy of the input grid to modify and return as output
    output_grid = [row[:] for row in input_grid]
    for i in range(len(output_grid)):
        for j in range(len(output_grid[0])):
            if output_grid[i][j] == 5:
                # Start a DFS for each '5' to label the entire cluster
                dfs(output_grid, i, j, cluster_number)
                cluster_number += 1  # Increment for the next cluster
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

output_grid = solve(input_grid)
for row in output_grid:
    print(row)