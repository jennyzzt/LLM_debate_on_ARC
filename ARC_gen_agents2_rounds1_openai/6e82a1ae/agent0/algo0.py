def solve(input_grid):
    # Initialize the output grid with zeros, matching the size of the input grid
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Iterate through the grid to apply the transformation rules
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            # Check for a block of four 5s forming a square
            if i < len(input_grid) - 1 and j < len(input_grid[0]) - 1:
                if input_grid[i][j] == 5 and input_grid[i+1][j] == 5 and input_grid[i][j+1] == 5 and input_grid[i+1][j+1] == 5:
                    output_grid[i][j] = 1
                    output_grid[i+1][j] = 1
                    output_grid[i][j+1] = 1
                    output_grid[i+1][j+1] = 1
            
            # Check for pairs of adjacent 5s (either horizontally or vertically)
            if input_grid[i][j] == 5:
                if i < len(input_grid) - 1 and input_grid[i+1][j] == 5:
                    output_grid[i][j] = 3
                    output_grid[i+1][j] = 3
                if j < len(input_grid[0]) - 1 and input_grid[i][j+1] == 5:
                    output_grid[i][j] = 3
                    output_grid[i][j+1] = 3
            
            # Check for single 5s
            if input_grid[i][j] == 5:
                if output_grid[i][j] == 0:  # Only update if it hasn't been set by previous rules
                    output_grid[i][j] = 2
    
    # Correcting overwrites: If a cell is part of a 4-block, it should not be overwritten by the pair rule
    for i in range(len(input_grid) - 1):
        for j in range(len(input_grid[0]) - 1):
            if output_grid[i][j] == 1:
                if output_grid[i+1][j] == 3: output_grid[i+1][j] = 1
                if output_grid[i][j+1] == 3: output_grid[i][j+1] = 1
                if output_grid[i+1][j+1] == 3: output_grid[i+1][j+1] = 1

    return output_grid

# Test case
input_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 5, 5, 0, 5, 5, 0, 0, 5],
    [0, 5, 5, 0, 0, 0, 5, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 5, 5, 0, 0, 5, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 5, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print(solve(input_grid))