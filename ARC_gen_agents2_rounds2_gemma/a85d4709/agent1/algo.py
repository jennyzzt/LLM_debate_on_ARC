def solve(input):
    output = []
    for i in range(len(input)):
        new_i = 0
        for j in range(len(input[i])):
            new_i += input[i][j]
        output.append(new_i)
    return output