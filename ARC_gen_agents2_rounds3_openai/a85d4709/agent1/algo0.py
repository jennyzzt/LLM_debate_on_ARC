def solve(input):
    # Initialize the output grid with the same dimensions as the input grid
    output = [[0 for _ in range(len(input[0]))] for _ in range(len(input))]
    
    # Iterate through each cell in the input grid
    for i in range(len(input)):
        for j in range(len(input[i])):
            # Initialize the count of 5s for the current cell
            count = 0
            
            # Count the number of 5s in the current row
            count += input[i].count(5)
            
            # Count the number of 5s in the current column
            for row in input:
                if row[j] == 5:
                    count += 1
            
            # Since we counted the cell itself twice if it's 5, subtract 1 if it's the case
            if input[i][j] == 5:
                count -= 1
            
            # Fill the corresponding cell in the output grid with the count
            output[i][j] = count
    
    return output

# Test case
input_test = [[0, 0, 5], [5, 0, 0], [0, 5, 0]]
print(solve(input_test))