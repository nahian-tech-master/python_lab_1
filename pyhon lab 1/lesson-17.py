matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix)

print(matrix[0])
print(matrix[1])
print(matrix[2])

print(matrix[1][1])
print(matrix[2][1])

matrix[0][2] = 15
print(matrix)

for row in matrix:
    for item in row:
        print(item)
