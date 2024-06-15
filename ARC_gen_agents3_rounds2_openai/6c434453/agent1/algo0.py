def solve(input_grid):
    # Initialize the output grid with the same dimensions as the input grid
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Function to check if a cell should be turned into a 2 based on its neighbors
    def should_turn_to_two(x, y):
        # Check horizontal neighbors
        horizontal = 1
        for dx in [-1, 1]:
            nx = x + dx
            while 0 <= nx < len(input_grid) and input_grid[nx][y] == 1:
                horizontal += 1
                nx += dx
        
        # Check vertical neighbors
        vertical = 1
        for dy in [-1, 1]:
            ny = y + dy
            while 0 <= ny < len(input_grid[0]) and input_grid[x][ny] == 1:
                vertical += 1
                ny += dy
        
        # Return True if either horizontal or vertical count is 3 or more
        return horizontal >= 3 or vertical >= 3
    
    # Iterate through each cell in the input grid
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            if input_grid[i][j] == 1:
                # If the cell is a '1', check if it should turn into a '2'
                if should_turn_to_two(i, j):
                    output_grid[i][j] = 2
                else:
                    output_grid[i][j] = 1
            else:
                # If the cell is not a '1', it remains unchanged
                output_grid[i][j] = input_grid[i][j]
    
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

output = solve(input_grid)
for row in output:
    print(row)