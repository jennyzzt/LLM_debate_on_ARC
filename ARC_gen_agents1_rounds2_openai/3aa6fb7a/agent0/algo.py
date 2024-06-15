def solve(input_grid):
    # Initialize the output grid with the same dimensions as the input grid.
    output = [[cell for cell in row] for row in input_grid]
    
    # Define the dimensions of the grid.
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    
    # Function to check if a position is valid within the grid.
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols
    
    # Iterate through each cell in the grid.
    for r in range(rows):
        for c in range(cols):
            # If the current cell contains an 8, check its neighbors.
            if input_grid[r][c] == 8:
                # List of possible neighbor positions (up, down, left, right).
                neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
                for nr, nc in neighbors:
                    # If the neighbor position is valid and the cell is empty (0), fill it with a 1.
                    if is_valid(nr, nc) and input_grid[nr][nc] == 0:
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

# Solve the test case and print the output grid.
output = solve(input_grid)
for row in output:
    print(row)