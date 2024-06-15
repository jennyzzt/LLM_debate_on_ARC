def solve(input_grid):
    output_grid = [[0 for _ in range(len(row))] for row in input_grid]
    
    for i in range(len(input_grid)):
        for j in range(len(input_grid[i])):
            if input_grid[i][j] == 5:
                # Default transformation
                output_grid[i][j] = 1
                
                # Check for horizontal pairs
                if j + 1 < len(input_grid[i]) and input_grid[i][j + 1] == 5:
                    output_grid[i][j] = 3
                    output_grid[i][j + 1] = 2
                
                # Check for vertical pairs
                if i + 1 < len(input_grid) and input_grid[i + 1][j] == 5:
                    output_grid[i][j] = 1
                    output_grid[i + 1][j] = 3
                
                # Check for single 5s (not part of a pair)
                if (j + 1 >= len(input_grid[i]) or input_grid[i][j + 1] != 5) and \
                   (i + 1 >= len(input_grid) or input_grid[i + 1][j] != 5):
                    output_grid[i][j] = 2

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

output_grid = solve(input_grid)
for row in output_grid:
    print(row)