def solve(input):
    output = []
    for row in input:
        if row[0] == 0:
            output.append([0] * len(row) for _ in range(len(row))]
        else:
            output.append(row)
    return output