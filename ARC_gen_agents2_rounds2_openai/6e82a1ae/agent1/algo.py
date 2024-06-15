def solve(input_grid):
    rows, cols = len(input_grid), len(input_grid[0])
    output_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    visited = set()

    def dfs(r, c, current_number):
        if r < 0 or r >= rows or c < 0 or c >= cols or input_grid[r][c] != 5 or (r, c) in visited:
            return
        visited.add((r, c))
        output_grid[r][c] = current_number
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            dfs(r + dr, c + dc, current_number)

    current_number = 1
    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] == 5 and (r, c) not in visited:
                dfs(r, c, current_number)
                current_number += 1

    return output_grid

# Test case
input_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 5], [0, 0, 0, 0, 0, 0, 0, 0, 0, 5], 
    [0, 0, 5, 5, 0, 5, 5, 0, 0, 5], [0, 5, 5, 0, 0, 0, 5, 0, 0, 5], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0], [5, 0, 0, 5, 5, 0, 0, 5, 0, 0], 
    [5, 0, 0, 0, 0, 0, 0, 5, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

output = solve(input_grid)
for row in output:
    print(row)