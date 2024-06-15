def solve(input):
    output = []
    for row in input:
        if row[0]!= 0:
            output.append([row[0]])
        else:
            output.append([row[1:]])
    return output