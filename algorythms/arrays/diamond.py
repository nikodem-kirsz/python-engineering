def find_largest_diamond(matrix):
    if not matrix:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])

    upper_half = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if i == 0:
                upper_half[i][j] = matrix[i][j]
            elif matrix[i][j] == 1:
                upper_half[i][j] = upper_half[i-1][j] + 1

    max_diamond_size = 0
    max_diamond_center = (0,0)

    for row in upper_half:
        print(row)

    for i in range (rows):
        for j in range(cols):
            diamond_size = upper_half[i][j]
            print(f"diamond_size: {diamond_size}")

            for k in range(1, diamond_size + 1): # Check if diamond is valid
                print(f"k: {k}, i,j: [{i},{j}]")
                if (
                    i + k < rows and i - k >= 0
                    and j + k < cols and j - k >= 0
                    and upper_half[i + k][j] >= k
                    and upper_half[i - k][j] <= k
                    and upper_half[i][j+k] <= k
                    and upper_half[i][j-k] <= k
                ):
                    print(f"Found diamond of radius: {k}")
                    print(f"Lenght of diamond is: {2 * k + 1}")
                    print(f"Size of diamond is: {4 * (k ** 2) + 1}")
                    max_diamond_size = max(max_diamond_size, k)
                    max_diamond_center = (i, j)

    return max_diamond_size, max_diamond_center

input_array = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

input_array2 = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0]
]

max_diamond_size = find_largest_diamond(input_array2)
print(max_diamond_size)