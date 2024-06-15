def solve(input):
    # Initialize the output grid with zeros
    output = [[0 for _ in range(len(input[0]))] for _ in range(len(input))]
    
    # Define the base value for the output when '5' is in the center
    base_value = 4
    
    # Iterate through each row of the input grid
    for i, row in enumerate(input):
        # Find the index of '5' in the current row
        index_of_5 = row.index(5)
        
        # Calculate the distance of '5' from the center of the row
        distance_from_center = abs(index_of_5 - len(row) // 2)
        
        # Calculate the output value based on the distance from the center
        output_value = base_value - distance_from_center
        
        # Fill the current row of the output grid with the calculated value
        output[i] = [output_value for _ in range(len(row))]
    
    return output

# Test case
input_test = [[0, 0, 5], [5, 0, 0], [0, 5, 0]]
print(solve(input_test))