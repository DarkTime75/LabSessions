matrixA = [[1, 2, 3], 
           [4, 5, 6],
           [7, 8, 9]]

matrixB = [[10, 11, 12],
           [13, 14, 15],
           [16, 17, 18]]

resultMatrix = []

for i in range(len(matrixA)):
    innerResultantMatrix = []
    for j in range(len(matrixA[0])):
        addedElements = matrixA[i][j] + matrixB[i][j]
        innerResultantMatrix.append(addedElements)
    resultMatrix.append(innerResultantMatrix)

print(resultMatrix)