def solve(input):
    output = []
    for i in range(len(input)):
        row = []
        for j, k in enumerate(input[i]):
            if j == 0 or j == len(input[i]) - 1:
                row.append(input[i][j])
            else:
                row.append(input[i][j])
        output.append(row)
    return output