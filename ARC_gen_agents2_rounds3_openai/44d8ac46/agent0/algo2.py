def solve(input_grid):
    # Copy the input grid to avoid modifying the original input
    output_grid = [row[:] for row in input_grid]
    
    # Get the dimensions of the grid
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    
    # Function to check if a cell is surrounded by '5's
    def is_surrounded_by_fives(r, c):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or input_grid[nr][nc] != 5:
                return False
        return True
    
    # Iterate through the grid and apply the transformation rule
    for r in range(1, rows-1):  # Adjusted to avoid checking the border cells
        for c in range(1, cols-1):  # Adjusted to avoid checking the border cells
            if input_grid[r][c] == 0 and is_surrounded_by_fives(r, c):
                output_grid[r][c] = 2
    
    return output_grid

# Test case
input_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [5, 5, 5, 5, 5, 0, 0, 5, 5, 5, 5, 0], 
    [5, 0, 0, 0, 5, 0, 0, 5, 5, 0, 5, 0], 
    [5, 0, 0, 0, 5, 0, 0, 5, 0, 0, 5, 0], 
    [5, 0, 0, 0, 5, 0, 0, 5, 0, 0, 5, 0], 
    [5, 5, 5, 5, 5, 0, 0, 5, 5, 5, 5, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0], 
    [0, 0, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0], 
    [0, 0, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0], 
    [0, 0, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0]
]

output_grid = solve(input_grid)
for row in output_grid:
    print(row)