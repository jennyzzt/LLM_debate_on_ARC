def find_group(grid, x, y, visited, group):
    """
    Recursive function to find all cells belonging to the same group of '5's.
    """
    # Check boundaries and if the cell is part of the group (value 5) and not visited
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 5 and (x, y) not in visited:
        # Mark the cell as visited and add to the current group
        visited.add((x, y))
        group.append((x, y))
        # Recursively check all four directions
        find_group(grid, x+1, y, visited, group)
        find_group(grid, x-1, y, visited, group)
        find_group(grid, x, y+1, visited, group)
        find_group(grid, x, y-1, visited, group)

def solve(input_grid):
    visited = set()
    groups = []
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Find all distinct groups of 5s
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            if input_grid[i][j] == 5 and (i, j) not in visited:
                group = []
                find_group(input_grid, i, j, visited, group)
                groups.append(group)
    
    # Replace each group of 5s with incrementing numbers starting from 1
    for idx, group in enumerate(groups, start=1):
        for x, y in group:
            output_grid[x][y] = idx
    
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