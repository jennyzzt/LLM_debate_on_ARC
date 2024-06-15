def flood_fill(input, x, y, visited):
    if x < 0 or x >= len(input) or y < 0 or y >= len(input[0]) or input[x][y] != 5 or visited[x][y]:
        return 0
    visited[x][y] = True
    return 1 + flood_fill(input, x+1, y, visited) + flood_fill(input, x-1, y, visited) + \
                flood_fill(input, x, y+1, visited) + flood_fill(input, x, y-1, visited)

def solve(input):
    output = [[0 for _ in range(len(input[0]))] for _ in range(len(input))]
    visited = [[False for _ in range(len(input[0]))] for _ in range(len(input))]
    
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 5 and not visited[i][j]:
                cluster_size = flood_fill(input, i, j, visited)
                # Convert cluster size to the corresponding number, with a cap at 4
                cluster_value = min(cluster_size, 4)
                # Perform another flood fill to update the output grid
                fill_output(output, input, i, j, cluster_value, visited)
    
    return output

def fill_output(output, input, x, y, value, visited):
    if x < 0 or x >= len(input) or y < 0 or y >= len(input[0]) or input[x][y] != 5 or output[x][y] != 0:
        return
    output[x][y] = value
    fill_output(output, input, x+1, y, value, visited)
    fill_output(output, input, x-1, y, value, visited)
    fill_output(output, input, x, y+1, value, visited)
    fill_output(output, input, x, y-1, value, visited)

# Test case
input_test = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 5], [0, 0, 0, 0, 0, 0, 0, 0, 0, 5], [0, 0, 5, 5, 0, 5, 5, 0, 0, 5], [0, 5, 5, 0, 0, 0, 5, 0, 0, 5], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [5, 0, 0, 0, 0, 0, 0, 0, 0, 0], [5, 0, 0, 5, 5, 0, 0, 5, 0, 0], [5, 0, 0, 0, 0, 0, 0, 5, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
output_test = solve(input_test)
for row in output_test:
    print(row)