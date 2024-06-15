def count_adjacent_5s(grid, row, col):
    count = 0
    for i in range(max(0, row-1), min(len(grid), row+2)):
        for j in range(max(0, col-1), min(len(grid[0]), col+2)):
            if grid[i][j] == 5:
                count += 1
    return count

def solve(input_grid):
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    for row in range(len(input_grid)):
        for col in range(len(input_grid[0])):
            if input_grid[row][col] == 5:
                # If the cell itself contains a 5, reduce the count by 1 as we're counting it as well
                output_grid[row][col] = count_adjacent_5s(input_grid, row, col) - 1
            else:
                output_grid[row][col] = count_adjacent_5s(input_grid, row, col)
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