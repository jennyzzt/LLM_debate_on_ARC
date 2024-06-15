def dfs(grid, x, y, visited):
    # Check bounds and if the cell is already visited or not a '1'
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or visited[x][y] or grid[x][y] != 1:
        return
    
    # Mark the cell as visited and change its value to '8'
    visited[x][y] = True
    grid[x][y] = 8
    
    # Explore the four adjacent directions
    dfs(grid, x+1, y, visited)
    dfs(grid, x-1, y, visited)
    dfs(grid, x, y+1, visited)
    dfs(grid, x, y-1, visited)

def solve(input_grid):
    # Create a copy of the input grid to modify
    output_grid = [row[:] for row in input_grid]
    
    # Initialize a visited matrix to keep track of visited cells during DFS
    visited = [[False for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Perform DFS for each cell
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            if input_grid[i][j] == 1 and not visited[i][j]:
                dfs(output_grid, i, j, visited)
    
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