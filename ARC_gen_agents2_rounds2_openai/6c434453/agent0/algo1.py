def solve(input_grid):
    rows, cols = len(input_grid), len(input_grid[0])
    output_grid = [[cell for cell in row] for row in input_grid]  # Copy input grid to output grid
    
    # Helper function to check for horizontal or vertical line of three '1's
    def is_part_of_line(r, c):
        horizontal = c > 0 and c < cols - 1 and input_grid[r][c-1] == 1 and input_grid[r][c] == 1 and input_grid[r][c+1] == 1
        vertical = r > 0 and r < rows - 1 and input_grid[r-1][c] == 1 and input_grid[r][c] == 1 and input_grid[r+1][c] == 1
        return horizontal or vertical
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If the cell is '1' and part of a line, change it to '2'
            if input_grid[r][c] == 1 and is_part_of_line(r, c):
                output_grid[r][c] = 2
    
    return output_grid

# Test case
input_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1], 
    [0, 1, 1, 1, 0, 0, 0, 0, 1, 0], 
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0], 
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 1], 
    [0, 1, 1, 1, 0, 0, 0, 0, 1, 1]
]

output = solve(input_grid)
for row in output:
    print(row)