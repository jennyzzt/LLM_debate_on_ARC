def solve(input_grid):
    # Initialize the output grid with the same dimensions as the input grid
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Apply a hypothetical transformation based on observed patterns
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            # Directly copy the cell value from input to output as a base case
            output_grid[i][j] = input_grid[i][j]
            
            # Apply hypothetical transformations based on the cell's value and its adjacency to 8
            if input_grid[i][j] in [1, 2, 3, 4]:
                # Check adjacency to 8 (up, down, left, right) and apply transformations
                adjacent_to_8 = False
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < len(input_grid) and 0 <= nj < len(input_grid[0]) and input_grid[ni][nj] == 8:
                        adjacent_to_8 = True
                        break
                
                # Apply a hypothetical rule based on adjacency to 8
                if adjacent_to_8:
                    if input_grid[i][j] == 4:
                        output_grid[i][j] = 1
                    elif input_grid[i][j] == 3:
                        output_grid[i][j] = 2
                    # Further refine or add rules as necessary based on the pattern observed
    
    # Return the transformed output grid
    return output_grid

# Test case input
input_grid = [
    [8, 8, 0, 8, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 8, 8, 8, 8, 4, 8, 8, 8, 8, 8, 8, 8],
    [0, 8, 0, 0, 0, 0, 4, 3, 8, 0, 0, 0, 0, 0, 8],
    [0, 8, 8, 8, 8, 8, 8, 4, 8, 8, 8, 0, 8, 8, 8],
    [0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 8, 0, 8, 0, 0],
    [8, 8, 8, 8, 8, 0, 8, 8, 8, 0, 8, 0, 8, 0, 8],
    [0, 0, 0, 0, 8, 0, 0, 0, 8, 0, 8, 0, 8, 0, 8],
    [8, 8, 8, 0, 8, 8, 8, 0, 8, 0, 8, 0, 8, 8, 8],
    [0, 0, 8, 0, 0, 0, 8, 0, 8, 0, 8, 0, 0, 0, 0],
    [8, 0, 8, 8, 8, 0, 8, 8, 8, 0, 8, 8, 8, 0, 8],
    [8, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 8, 0, 8],
    [8, 8, 8, 0, 8, 0, 8, 8, 8, 8, 8, 8, 8, 0, 8],
    [0, 0, 8, 0, 8, 0, 8, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 8, 8, 8, 0, 8, 0, 8, 8, 8, 8, 8, 8, 8],
    [8, 0, 0, 0, 0, 0, 8, 0, 8, 0, 0, 0, 0, 0, 0]
]

# Solve the test case
output_grid = solve(input_grid)

# Print the output grid
for row in output_grid:
    print(row)