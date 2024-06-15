def solve(input):
    # Copy the input to the output to preserve the structure and modify as needed
    output = [row[:] for row in input]
    
    # Define the dimensions of the grid
    rows = len(input)
    cols = len(input[0]) if rows > 0 else 0
    
    # Function to check if a cell is surrounded by '5's
    def is_surrounded_by_5(r, c):
        # Check all surrounding cells if they are '5', considering edge cases
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if input[nr][nc] != 5:
                    return False
            else:
                return False
        return True
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # Check if the current cell is '0' and surrounded by '5's
            if input[r][c] == 0 and is_surrounded_by_5(r, c):
                output[r][c] = 2  # Change the cell to '2'
    
    return output

# Test case
input_test = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [5, 5, 5, 5, 5, 0, 0, 5, 5, 5, 5, 0], [5, 0, 0, 0, 5, 0, 0, 5, 5, 0, 5, 0], [5, 0, 0, 0, 5, 0, 0, 5, 0, 0, 5, 0], [5, 0, 0, 0, 5, 0, 0, 5, 0, 0, 5, 0], [5, 5, 5, 5, 5, 0, 0, 5, 5, 5, 5, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0], [0, 0, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0], [0, 0, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0], [0, 0, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0]]
output_test = solve(input_test)
for row in output_test:
    print(row)