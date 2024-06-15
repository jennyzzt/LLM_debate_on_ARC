def solve(input_grid):
    # Copy the input grid to avoid modifying the original input directly
    output_grid = [row[:] for row in input_grid]
    
    # Get the number of rows and columns in the grid
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    
    # Function to check and mark adjacent cells
    def mark_adjacent(r, c):
        # List of possible directions (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            # Check if the new position is within the grid bounds
            if 0 <= new_r < rows and 0 <= new_c < cols:
                # Mark the cell with a "1" if it's empty
                if output_grid[new_r][new_c] == 0:
                    output_grid[new_r][new_c] = 1
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If the cell contains an "8", mark its adjacent cells
            if input_grid[r][c] == 8:
                mark_adjacent(r, c)
    
    return output_grid

# Test case
input_grid = [
    [0, 0, 0, 0, 0, 8, 8],
    [8, 8, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 8, 8, 0, 0],
    [0, 8, 0, 0, 0, 0, 0],
    [8, 8, 0, 0, 0, 0, 0]
]

output = solve(input_grid)
for row in output:
    print(row)