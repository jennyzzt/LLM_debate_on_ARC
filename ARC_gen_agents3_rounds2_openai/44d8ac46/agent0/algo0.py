def solve(input_grid):
    # Copy the input grid to the output grid
    output_grid = [row[:] for row in input_grid]
    
    # Get the dimensions of the grid
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    
    # Function to check if a cell is enclosed by '5's
    def is_enclosed_by_5(r, c):
        # Check all directions for '5's
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            rr, cc = r + dr, c + dc
            if 0 <= rr < rows and 0 <= cc < cols:
                if input_grid[rr][cc] != 5:
                    return False
            else:
                return False
        return True
    
    # Iterate through the grid and apply the transformation
    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] == 0 and is_enclosed_by_5(r, c):
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