def solve(input_grid):
    # Copy the input grid to avoid modifying the original grid
    output_grid = [row[:] for row in input_grid]
    
    # Get the dimensions of the grid
    rows = len(input_grid)
    cols = len(input_grid[0])
    
    # Function to count the number of '5' cells adjacent (horizontally or vertically) to a given cell
    def count_adjacent_fives(r, c):
        adjacent_fives = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Directions: up, down, left, right
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and input_grid[nr][nc] == 5:
                adjacent_fives += 1
        return adjacent_fives
    
    # Iterate through the grid and apply the transformation rule
    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] == 0 and count_adjacent_fives(r, c) >= 2:
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