def find_clusters(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    clusters = []
    
    def dfs(r, c, cluster):
        if (r, c) in visited or r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 5:
            return
        visited.add((r, c))
        cluster.append((r, c))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            dfs(r + dr, c + dc, cluster)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 5 and (r, c) not in visited:
                cluster = []
                dfs(r, c, cluster)
                clusters.append(cluster)
    return clusters

def solve(input_grid):
    clusters = find_clusters(input_grid)
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    
    for cluster in clusters:
        cluster_number = min(len(cluster), 4)  # Cap the cluster number at 4
        for r, c in cluster:
            output_grid[r][c] = cluster_number
    
    return output_grid

# Test case
input_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 5], [0, 0, 0, 0, 0, 0, 0, 0, 0, 5], 
    [0, 0, 5, 5, 0, 5, 5, 0, 0, 5], [0, 5, 5, 0, 0, 0, 5, 0, 0, 5], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0], [5, 0, 0, 5, 5, 0, 0, 5, 0, 0], 
    [5, 0, 0, 0, 0, 0, 0, 5, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

output = solve(input_grid)
for row in output:
    print(row)