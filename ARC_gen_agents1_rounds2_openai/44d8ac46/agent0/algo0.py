def solve(input_grid):
    # Copy the input grid to avoid modifying the original input
    output = [row[:] for row in input_grid]
    rows = len(input_grid)
    cols = len(input_grid[0])

    # Function to check if a cell is surrounded by cells with value 5
    def is_surrounded_by_5(r, c):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or input_grid[nr][nc] != 5:
                return False
        return True

    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] == 5 and is_surrounded_by_5(r, c):
                output[r][c] = 2  # Change the value to 2 if surrounded by 5s

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