matrixA = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrixB = [[10, 11, 12],
           [13, 14, 15],
           [16, 17, 18]]

resultMatrix = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

for i in range(len(matrixA)):
    for j in range(len(matrixB[0])):
        for k in range(len(matrixB)):
            resultMatrix[i][j] += matrixA[i][k] * matrixB[k][j]

print(resultMatrix)