def solve(input_grid):
    # Copy the input grid to avoid modifying the original
    output = [row[:] for row in input_grid]
    
    # Define the relative positions of the eight directions
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    # Get the dimensions of the grid
    rows, cols = len(input_grid), len(input_grid[0])
    
    # Function to check if a cell is surrounded by '5's
    def is_surrounded_by_5s(r, c):
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # Check if the new position is within the grid bounds
            if 0 <= nr < rows and 0 <= nc < cols:
                # If any of the surrounding cells is not '5', return False
                if input_grid[nr][nc] != 5:
                    return False
            else:
                # If the cell is at the edge and doesn't have all sides covered, return False
                return False
        return True
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If the cell is '0' and surrounded by '5's, replace it with '2'
            if input_grid[r][c] == 0 and is_surrounded_by_5s(r, c):
                output[r][c] = 2
    
    return output

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

output = solve(input_grid)
for row in output:
    print(row)