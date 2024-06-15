def solve(input_grid):
    # Copy the input grid to avoid modifying the original grid
    output_grid = [row[:] for row in input_grid]
    
    # Get the number of rows and columns in the grid
    rows = len(input_grid)
    cols = len(input_grid[0])
    
    # Function to check if a cell is on the border of the shape
    def is_border_cell(r, c):
        # Check all four directions (up, down, left, right)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # If the adjacent cell is out of bounds or not '1', it's a border cell
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or input_grid[nr][nc] != 1:
                return True
        return False
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If the cell is '1' and not on the border, change it to '8'
            if input_grid[r][c] == 1 and not is_border_cell(r, c):
                output_grid[r][c] = 8
    
    return output_grid

# Test case
input_grid = [
    [1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9], [9, 9, 9, 1, 1, 1, 1, 1, 9, 9, 9, 1, 9, 9, 9], [9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 1, 9, 9, 9], [9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 1, 9, 9, 9], [9, 9, 9, 9, 1, 1, 1, 1, 9, 9, 9, 1, 9, 9, 1], [9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 1, 1, 1, 1], [1, 1, 1, 1, 9, 9, 9, 1, 9, 9, 9, 1, 9, 9, 1], [1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1], [1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1], [1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 9], [9, 9, 9, 1, 9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9], [9, 9, 9, 1, 9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9], [9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 9]
]

output_grid = solve(input_grid)
for row in output_grid:
    print(row)