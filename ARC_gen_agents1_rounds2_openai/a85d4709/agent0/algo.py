def solve(input_grid):
    # Initialize the output grid with zeros, having the same dimensions as the input grid
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Iterate through each cell in the input grid
    for row in range(len(input_grid)):
        for col in range(len(input_grid[0])):
            # Initialize count for the current cell
            count = 0
            # Count non-zero cells in the same row
            for j in range(len(input_grid[0])):
                if input_grid[row][j] != 0:
                    count += 1
            # Count non-zero cells in the same column
            for i in range(len(input_grid)):
                if input_grid[i][col] != 0:
                    count += 1
            # Subtract one if the current cell is non-zero to avoid double counting
            if input_grid[row][col] != 0:
                count -= 1
            # Assign the count to the corresponding cell in the output grid
            output_grid[row][col] = count
    
    return output_grid

# Test case
input_grid = [[0, 0, 5], [5, 0, 0], [0, 5, 0]]
output = solve(input_grid)
print(output)