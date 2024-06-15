def transform_value(value, i, j, input_grid):
    if value != 5:
        return 0  # No transformation needed for non-5 values
    
    # Simplified assumption for transformation
    # Check for neighbors to determine transformation
    neighbors = 0
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if 0 <= i + di < len(input_grid) and 0 <= j + dj < len(input_grid[0]):
                if input_grid[i + di][j + dj] == 5:
                    neighbors += 1
    
    # Simplified transformation based on neighbors
    if neighbors <= 2:
        return 3  # Edge or corner
    elif neighbors <= 4:
        return 2  # Middle of a cluster
    else:
        return 1  # Inside a cluster

def solve(input_grid):
    output = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            output[i][j] = transform_value(input_grid[i][j], i, j, input_grid)
    
    return output

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