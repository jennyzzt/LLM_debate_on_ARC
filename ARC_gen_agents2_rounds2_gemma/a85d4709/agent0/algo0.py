def solve(input):
    output = []
    for i in range(len(input)):
        row = []
        for j, k in enumerate(input[i]):
            row.append(input[i][j])
        output.append(row)
    return output