def solve(input_grid):
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = [[cell for cell in row] for row in input_grid]

    # Function to check if a cell is on the border of a contiguous block of 1s
    def is_on_border(r, c):
        if input_grid[r][c] != 1:
            return False
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or input_grid[nr][nc] != 1:
                return True
        return False

    # Mark cells to be changed to 8
    to_change = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] == 1 and not is_on_border(r, c):
                to_change.append((r, c))

    # Apply the transformation
    for r, c in to_change:
        output_grid[r][c] = 8

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

output_test = solve(input_test)
for row in output_test:
    print(row)