def solve(input_grid):
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    
    # Initialize the output grid with zeros
    output_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Function to check if a cell is part of a horizontal or vertical line of three or more '1's
    def is_part_of_line(r, c):
        # Check horizontal line
        horizontal_count = 1
        for i in range(c-1, -1, -1):
            if input_grid[r][i] == 1:
                horizontal_count += 1
            else:
                break
        for i in range(c+1, cols):
            if input_grid[r][i] == 1:
                horizontal_count += 1
            else:
                break
        if horizontal_count >= 3:
            return True
        
        # Check vertical line
        vertical_count = 1
        for i in range(r-1, -1, -1):
            if input_grid[i][c] == 1:
                vertical_count += 1
            else:
                break
        for i in range(r+1, rows):
            if input_grid[i][c] == 1:
                vertical_count += 1
            else:
                break
        if vertical_count >= 3:
            return True
        
        return False
    
    # Apply the transformation rules to each cell
    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] == 1:
                # If the cell is part of a line, transform it to 2
                if is_part_of_line(r, c):
                    output_grid[r][c] = 2
                else:
                    output_grid[r][c] = 1
            else:
                output_grid[r][c] = 0  # Preserve zeros
    
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

output_grid = solve(input_grid)
for row in output_grid:
    print(row)