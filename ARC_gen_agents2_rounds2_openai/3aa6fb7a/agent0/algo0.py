def solve(input_grid):
    # Initialize the output grid as a deep copy of the input grid
    output_grid = [row[:] for row in input_grid]
    
    # Define the dimensions of the grid
    rows = len(input_grid)
    cols = len(input_grid[0])
    
    # Function to check if a position is within the grid bounds
    def is_valid_position(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    # Directions for up, down, left, right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # If the current cell contains '8'
            if input_grid[i][j] == 8:
                # Check all adjacent cells
                for dx, dy in directions:
                    new_x, new_y = i + dx, j + dy
                    # If the adjacent cell is within bounds and not '8', change it to '1'
                    if is_valid_position(new_x, new_y) and input_grid[new_x][new_y] != 8:
                        output_grid[new_x][new_y] = 1
                        
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