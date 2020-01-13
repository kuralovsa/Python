matrix = [[i+j for j in range(4)] for i in range(4)]

for row in matrix:
    print(" ".join(list(map(str,row))))

totalSum = 0
for i in range(1,len(matrix)):
    for j in range(i):
        totalSum += matrix[i][j]
print("Below sum: ", totalSum)

totalSum = 0
for i in range(len(matrix)):
    for j in range(i+1,len(matrix)):
        totalSum += matrix[i][j]
print("Above sum: ", totalSum)
