def solve(input_grid):
    # Copy the input grid to the output grid
    output = [row[:] for row in input_grid]
    
    # Get the number of rows and columns in the grid
    rows = len(input_grid)
    columns = len(input_grid[0])
    
    # Define the directions for adjacent cells (up, down, left, right)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Iterate through each cell in the grid
    for row in range(rows):
        for col in range(columns):
            # Check if the current cell contains the number 8
            if input_grid[row][col] == 8:
                # Check each direction for adjacent cells
                for d in directions:
                    new_row = row + d[0]
                    new_col = col + d[1]
                    # Check if the adjacent cell is within the grid bounds
                    if 0 <= new_row < rows and 0 <= new_col < columns:
                        # Mark the adjacent cell with 1 if it originally contains 0
                        if input_grid[new_row][new_col] == 0:
                            output[new_row][new_col] = 1
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