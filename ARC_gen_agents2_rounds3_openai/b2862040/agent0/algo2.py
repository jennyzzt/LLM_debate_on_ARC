def solve(input_grid):
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = [[cell for cell in row] for row in input_grid]

    # Function to check if a cell is on the border of a shape
    def is_border(r, c):
        if input_grid[r][c] != 1:
            return False
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or input_grid[nr][nc] != 1:
                return True
        return False

    # Function to fill the interior of a shape with 8s
    def fill_shape(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or input_grid[r][c] != 1 or is_border(r, c):
            return
        output_grid[r][c] = 8
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            fill_shape(r + dr, c + dc)

    # Apply transformation
    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] == 1 and not is_border(r, c):
                fill_shape(r, c)

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