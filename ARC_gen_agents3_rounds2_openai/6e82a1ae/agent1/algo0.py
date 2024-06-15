def flood_fill(input, x, y, fill_value):
    # Check for out-of-bounds or if the cell is not equal to 5
    if x < 0 or x >= len(input) or y < 0 or y >= len(input[0]) or input[x][y] != 5:
        return
    
    # Replace the current cell with the fill_value
    input[x][y] = fill_value
    
    # Recursively apply flood fill to adjacent cells
    flood_fill(input, x+1, y, fill_value)
    flood_fill(input, x-1, y, fill_value)
    flood_fill(input, x, y+1, fill_value)
    flood_fill(input, x, y-1, fill_value)

def solve(input):
    output = [[cell for cell in row] for row in input]  # Create a copy of the input grid
    fill_value = 1  # Start filling with value 1
    
    for i in range(len(input)):
        for j in range(len(input[i])):
            if output[i][j] == 5:  # Found a new group to fill
                flood_fill(output, i, j, fill_value)
                fill_value += 1  # Increment for the next group
    
    return output

# Test case
input_test = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 5], [0, 0, 0, 0, 0, 0, 0, 0, 0, 5], [0, 0, 5, 5, 0, 5, 5, 0, 0, 5], [0, 5, 5, 0, 0, 0, 5, 0, 0, 5], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [5, 0, 0, 0, 0, 0, 0, 0, 0, 0], [5, 0, 0, 5, 5, 0, 0, 5, 0, 0], [5, 0, 0, 0, 0, 0, 0, 5, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
output_test = solve(input_test)
for row in output_test:
    print(row)