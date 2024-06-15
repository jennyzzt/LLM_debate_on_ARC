def solve(input_grid):
    # Create a copy of the input grid to modify
    output_grid = [row[:] for row in input_grid]
    
    # Define the directions to check (up, down, left, right)
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    # Get the dimensions of the grid
    rows, cols = len(input_grid), len(input_grid[0])
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If the cell contains an 8, check its neighbors
            if input_grid[r][c] == 8:
                for dr, dc in directions:
                    # Calculate the neighbor's position
                    nr, nc = r + dr, c + dc
                    # Check if the neighbor is within the grid bounds
                    if 0 <= nr < rows and 0 <= nc < cols:
                        # If the neighbor is a 0, change it to a 1 in the output grid
                        if input_grid[nr][nc] == 0:
                            output_grid[nr][nc] = 1
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