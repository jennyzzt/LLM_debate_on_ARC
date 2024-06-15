def solve(input_grid):
    output_grid = [[0 for _ in range(len(row))] for row in input_grid]
    
    for i in range(len(input_grid)):
        for j in range(len(input_grid[i])):
            if input_grid[i][j] == 5:
                # Check for single 5
                if (i == 0 or input_grid[i-1][j] != 5) and (j == 0 or input_grid[i][j-1] != 5) and (i == len(input_grid)-1 or input_grid[i+1][j] != 5) and (j == len(input_grid[i])-1 or input_grid[i][j+1] != 5):
                    output_grid[i][j] = 2
                # Check for horizontal pair of 5s
                elif j+1 < len(input_grid[i]) and input_grid[i][j+1] == 5:
                    output_grid[i][j] = 3
                    output_grid[i][j+1] = 3
                # Check for vertical pair of 5s
                elif i+1 < len(input_grid) and input_grid[i+1][j] == 5:
                    output_grid[i][j] = 3
                    output_grid[i+1][j] = 3
                # Check for cluster of four 5s
                elif i+1 < len(input_grid) and j+1 < len(input_grid[i]) and input_grid[i+1][j] == 5 and input_grid[i][j+1] == 5 and input_grid[i+1][j+1] == 5:
                    output_grid[i][j] = 1
                    output_grid[i+1][j] = 1
                    output_grid[i][j+1] = 1
                    output_grid[i+1][j+1] = 1
                # Default case for any other patterns (if any)
                else:
                    output_grid[i][j] = 2 # Assuming single 5s transform to 2s as a default case
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