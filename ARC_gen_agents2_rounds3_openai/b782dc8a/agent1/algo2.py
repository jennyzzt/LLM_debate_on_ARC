def solve(input_grid):
    # Initialize the output grid with the same dimensions as the input grid
    output_grid = [[8 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Iterate through the input grid to find and transform numbers other than 8
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            # Directly copy the number if it's 8
            if input_grid[i][j] == 8:
                output_grid[i][j] = 8
            else:
                # Apply a specific transformation based on the number
                num = input_grid[i][j]
                # For simplicity, let's assume a transformation that involves incrementing the number
                # and spreading it to adjacent cells, wrapping around from 4 back to 1
                if num not in [0, 8]:  # Assuming transformation is needed for numbers other than 0 and 8
                    # Apply transformation to the current cell and adjacent cells if they are not 8
                    output_grid[i][j] = (num % 4) + 1  # Transform the current cell
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        if 0 <= i + di < len(input_grid) and 0 <= j + dj < len(input_grid[0]) and output_grid[i + di][j + dj] != 8:
                            output_grid[i + di][j + dj] = ((output_grid[i + di][j + dj] - 1) % 4) + 1  # Apply transformation to adjacent cells
                else:
                    # If the number is 0, it might remain unchanged or follow a specific rule not observed in the examples
                    output_grid[i][j] = num
    
    return output_grid

# Test case
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

output_grid = solve(input_grid)
for row in output_grid:
    print(row)