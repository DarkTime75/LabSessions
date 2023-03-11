matrix1 = [[0, 0, 0, 1, 0],
           [2, 0, 0, 0, 3],
           [0, 0, 0, 4, 0]]

matrix2 = [[0, 1, 0, 4, 0],
           [0, 0, 0, 3, 0],
           [1, 4, 0, 0, 2]]
 
def convertToDictionary(matrix):
    dct = {}
    for i in range(len(matrix)): # Iterate through rows
        for j in range(len(matrix[i])): # Iterate through columns
            if matrix[i][j] != 0:
                dct[i, j] = matrix[i][j]
    return dct

dictionaryMatrix1 = convertToDictionary(matrix1)
dictionaryMatrix2 = convertToDictionary(matrix2)

def addSparseMatrix(first, second):
    resultantDict = {}
    allKeys = list(first.keys()) + list(second.keys())
    for keyIterator in allKeys:
        firstValue = first.get(keyIterator, 0)
        secondValue = second.get(keyIterator, 0)
        sumOfValues = firstValue + secondValue
        if sumOfValues != 0:
            resultantDict[keyIterator] = sumOfValues
    return resultantDict

res = addSparseMatrix(dictionaryMatrix1, dictionaryMatrix2)
print(res)
