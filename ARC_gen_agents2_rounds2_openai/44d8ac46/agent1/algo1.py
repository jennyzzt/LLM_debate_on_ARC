def solve(input_grid):
    # Create a copy of the input grid to modify and return as output
    output_grid = [row[:] for row in input_grid]
    
    # Get the number of rows and columns in the grid
    rows = len(input_grid)
    columns = len(input_grid[0])
    
    # Function to check if a cell is directly surrounded by 5s
    def is_directly_surrounded_by_5s(x, y):
        # Check boundaries and then if surrounded by 5s
        if x > 0 and x < rows - 1 and y > 0 and y < columns - 1:
            return input_grid[x-1][y] == 5 and input_grid[x+1][y] == 5 and input_grid[x][y-1] == 5 and input_grid[x][y+1] == 5
        return False

    # Iterate through each cell in the grid except the border cells
    for i in range(1, rows - 1):
        for j in range(1, columns - 1):
            # Check if the current cell is directly surrounded by 5s
            if is_directly_surrounded_by_5s(i, j):
                # Change the current cell's value to 2
                output_grid[i][j] = 2
    
    return output_grid

# Test case
input_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [5, 5, 5, 5, 5, 0, 0, 5, 5, 5, 5, 0], 
    [5, 0, 0, 0, 5, 0, 0, 5, 5, 0, 5, 0], 
    [5, 0, 0, 0, 5, 0, 0, 5, 0, 0, 5, 0], 
    [5, 0, 0, 0, 5, 0, 0, 5, 0, 0, 5, 0], 
    [5, 5, 5, 5, 5, 0, 0, 5, 5, 5, 5, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0], 
    [0, 0, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0], 
    [0, 0, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0], 
    [0, 0, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0]
]

output_grid = solve(input_grid)
for row in output_grid:
    print(row)