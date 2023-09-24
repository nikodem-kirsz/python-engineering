def connected_cell(matrix):
    def recursive(i, j):
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] == 0:
            return 0
        
        matrix[i][j] = 0  # Mark the cell as visited
        size = 1
        
        # Check all 8 adjacent cells
        size += recursive(i-1, j-1)
        size += recursive(i-1, j)
        size += recursive(i-1, j+1)
        size += recursive(i, j-1)
        size += recursive(i, j+1)
        size += recursive(i+1, j-1)
        size += recursive(i+1, j)
        size += recursive(i+1, j+1)
        
        return size

    max_region_size = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                region_size = recursive(i, j)
                max_region_size = max(max_region_size, region_size)

    return max_region_size

# Example usage:
grid = [
    [1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1]
]

result = connected_cell(grid)
print(f"The size of the largest connected region is {result}")
