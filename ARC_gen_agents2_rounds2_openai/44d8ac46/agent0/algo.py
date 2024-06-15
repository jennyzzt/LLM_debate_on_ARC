def solve(input_grid):
    # Copy the input grid to the output grid to avoid modifying the original grid.
    output_grid = [row[:] for row in input_grid]
    
    # Get the number of rows and columns in the grid.
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    
    # Function to count the number of '5's adjacent to a given cell.
    def count_adjacent_fives(r, c):
        adjacent_fives = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Directions: up, down, left, right
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and input_grid[nr][nc] == 5:
                adjacent_fives += 1
        return adjacent_fives
    
    # Iterate through each cell in the grid.
    for i in range(rows):
        for j in range(cols):
            # If the cell is '0' and has at least two adjacent '5's, change it to '2'.
            if input_grid[i][j] == 0 and count_adjacent_fives(i, j) >= 2:
                output_grid[i][j] = 2
    
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