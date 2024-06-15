def solve(input):
    # Create a copy of the input grid to modify
    output = [row[:] for row in input]
    
    # Get the dimensions of the grid
    rows = len(input)
    cols = len(input[0])
    
    # Function to check if a cell is on the border of a pattern
    def is_border_cell(r, c):
        # Check all eight directions around the cell
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # If the adjacent cell is out of bounds or not a '1', it's a border cell
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or input[nr][nc] != 1:
                return True
        return False
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If the cell is a '1' and not on the border, change it to '8'
            if input[r][c] == 1 and not is_border_cell(r, c):
                output[r][c] = 8
    
    return output

# Test case
input_test = [
    [1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9],
    [9, 9, 9, 1, 1, 1, 1, 1, 9, 9, 9, 1, 9, 9, 9],
    # ... (rest of the input grid)
    [9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 9]
]

# Since the input is incomplete, this is just a demonstration of how to use the function.
# output_test = solve(input_test)
# print(output_test)