def solve(input_grid):
    # Initialize the output grid with zeros, matching the size of the input grid
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    # Function to mark connected components and replace them with the current number
    def fill_component(x, y, current_number):
        if x < 0 or x >= len(input_grid) or y < 0 or y >= len(input_grid[0]) or input_grid[x][y] != 5:
            return
        # Replace the number 5 with the current number in the output grid
        output_grid[x][y] = current_number
        input_grid[x][y] = 0  # Mark as visited
        
        # Recursively fill connected components
        fill_component(x+1, y, current_number)
        fill_component(x-1, y, current_number)
        fill_component(x, y+1, current_number)
        fill_component(x, y-1, current_number)
    
    # Main logic to iterate through the grid and fill components
    current_number = 1
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            if input_grid[i][j] == 5:
                fill_component(i, j, current_number)
                current_number += 1  # Increment for the next group
    
    return output_grid

# Test case
input_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 5], [0, 0, 0, 0, 0, 0, 0, 0, 0, 5], 
    [0, 0, 5, 5, 0, 5, 5, 0, 0, 5], [0, 5, 5, 0, 0, 0, 5, 0, 0, 5], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0], [5, 0, 0, 5, 5, 0, 0, 5, 0, 0], 
    [5, 0, 0, 0, 0, 0, 0, 5, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

output_grid = solve(input_grid)
for row in output_grid:
    print(row)