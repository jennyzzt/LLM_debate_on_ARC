def solve(input):
    output = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(input)):
        if input[i][0] == input[i][1] == input[i][2]:
            output[i] = input[i]
    return output