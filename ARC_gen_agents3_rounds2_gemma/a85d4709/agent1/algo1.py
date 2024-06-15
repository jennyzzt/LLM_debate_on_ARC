def solve(input):
    output = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(input)):
        for j in range(len(input[i])):
            output[i][j] = input[i][j] if input[i][j]!= 0 else output[i][j]
    return output