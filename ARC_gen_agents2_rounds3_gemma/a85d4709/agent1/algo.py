def solve(input):
    output = []
    for i in range(len(input)):
        row = []
        for j, k in enumerate(input[i]):
            if input[i][j] == 0:
                row.append(0)
            elif input[i][j] == 1:
                row.append(-1)
            elif input[i][j] == 2:
                row.append(1)
        output.append(row)
    return output