def solve(input_grid):
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0

    # Initialize the output grid with the same dimensions as the input grid
    output_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    # Helper function to update the output grid safely
    def update_output(r, c, value):
        if 0 <= r < rows and 0 <= c < cols:
            output_grid[r][c] = value

    # Process each cell in the input grid
    for r in range(rows):
        for c in range(cols):
            # Directly copy the value from the input grid to the output grid
            output_grid[r][c] = input_grid[r][c]

            # Apply transformations based on the observed patterns
            if input_grid[r][c] == 8:
                # For '8', expand it outward
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    update_output(r + dr, c + dc, 8)
            elif input_grid[r][c] == 2:
                # For '2', apply specific transformation rules observed
                update_output(r, c, 2)  # Placeholder for specific logic
            # Implement additional transformations for other numbers as observed in the patterns

    # Additional logic for context-aware transformations
    # Placeholder for additional pattern-based logic

    return output_grid

# Test case
input_test = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # ... truncated for brevity
]

output_test = solve(input_test)
for row in output_test:
    print(row)