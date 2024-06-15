def solve(input_grid):
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Function to check if a cell is part of a 2x2 square of 5s
    def is_part_of_square(x, y):
        return (x < len(input_grid) - 1 and y < len(input_grid[0]) - 1 and
                input_grid[x][y] == 5 and input_grid[x+1][y] == 5 and
                input_grid[x][y+1] == 5 and input_grid[x+1][y+1] == 5)
    
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            if input_grid[i][j] == 5:
                if is_part_of_square(i, j):
                    output_grid[i][j] = 4
                elif i < len(input_grid) - 1 and input_grid[i+1][j] == 5:
                    output_grid[i][j] = 3
                elif j < len(input_grid[0]) - 1 and input_grid[i][j+1] == 5:
                    output_grid[i][j] = 2
                else:
                    output_grid[i][j] = 1
                # Correct for the second cell in a 2x2 square
                if i > 0 and j > 0 and is_part_of_square(i-1, j-1):
                    output_grid[i][j] = 4
    
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

output = solve(input_grid)
for row in output:
    print(row)