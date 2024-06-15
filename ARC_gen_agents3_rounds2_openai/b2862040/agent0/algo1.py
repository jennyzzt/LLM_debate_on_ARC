def solve(input_grid):
    # Copy the input grid to the output grid.
    output_grid = [row[:] for row in input_grid]
    
    # Get the number of rows and columns in the grid.
    rows = len(input_grid)
    cols = len(input_grid[0])
    
    # Define a helper function to check if a '1' is surrounded by '9's.
    def is_surrounded_by_nines(r, c):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Left, Right, Up, Down
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if input_grid[nr][nc] != 9:
                    return False
            else:
                # Edge cells are considered not surrounded by '9's.
                return False
        return True
    
    # Iterate through each cell in the grid except the border cells.
    for i in range(rows):
        for j in range(cols):
            # Check if the current cell is '1'.
            if input_grid[i][j] == 1:
                # If the '1' is not surrounded by '9's, change it to '8'.
                if not is_surrounded_by_nines(i, j):
                    output_grid[i][j] = 8
    
    return output_grid

# Test case
input_test = [
    [1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9],
    [9, 9, 9, 1, 1, 1, 1, 1, 9, 9, 9, 1, 9, 9, 9],
    [9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 1, 9, 9, 9],
    [9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 1, 9, 9, 9],
    [9, 9, 9, 9, 1, 1, 1, 1, 9, 9, 9, 1, 9, 9, 1],
    [9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 1, 1, 1, 1],
    [1, 1, 1, 1, 9, 9, 9, 1, 9, 9, 9, 1, 9, 9, 1],
    [1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1],
    [1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1],
    [1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 9],
    [9, 9, 9, 1, 9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9],
    [9, 9, 9, 1, 9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9],
    [9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 9]
]

# Solve the test case
output_test = solve(input_test)

# Print the output grid
for row in output_test:
    print(row)