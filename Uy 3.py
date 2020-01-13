from random import random
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(int(random()*10))
    matrix.append(row)
    
for row in matrix:
    print(row)

sumMain = 0
sumSecondary = 0
if i==j:
    for i in range(3):
        sumMain += matrix[i][i]
        sumSecondary += matrix[i][3-j-1]
totalSum = 0
for i in range(1,len(matrix)):
    for j in range(i):
        totalSum += matrix[3-j-1][i]
print("Below sum: ", totalSum)

totalSum = 0
for i in range(len(matrix)):
    for j in range(i+1,len(matrix)):
        totalSum += matrix[3-j-1][i+1]
print("Above sum: ", totalSum)
print(sumMain)
print(sumSecondary)
