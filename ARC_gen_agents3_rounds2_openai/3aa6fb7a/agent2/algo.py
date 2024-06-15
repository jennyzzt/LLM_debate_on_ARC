def solve(input_grid):
    # Copy the input grid to avoid modifying the original input directly
    output_grid = [row[:] for row in input_grid]
    
    # Define the number of rows and columns
    rows = len(input_grid)
    cols = len(input_grid[0])
    
    # Define the directions to check for adjacent cells
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Iterate through each cell in the grid
    for row in range(rows):
        for col in range(cols):
            # Check if the current cell contains an '8'
            if input_grid[row][col] == 8:
                # Check each of the four adjacent cells
                for dx, dy in directions:
                    new_row, new_col = row + dx, col + dy
                    # Ensure the new position is within the grid boundaries
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        # If the adjacent cell is '0', change it to '1' in the output grid
                        if input_grid[new_row][new_col] == 0:
                            output_grid[new_row][new_col] = 1
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