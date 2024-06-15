def solve(input_grid):
    # Initialize the output grid with the same values as the input grid
    output = [row[:] for row in input_grid]
    
    # Get the dimensions of the grid
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    
    # Function to check if a position is valid within the grid
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols
    
    # Directions for adjacent cells (up, down, left, right)
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If the current cell has the value 8
            if input_grid[r][c] == 8:
                # Check all adjacent cells
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # If the adjacent cell is valid and not 8, change its value to 1 in the output grid
                    if is_valid(nr, nc) and input_grid[nr][nc] != 8:
                        output[nr][nc] = 1
    
    return output

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