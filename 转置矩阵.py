#  Copyright (c) 2019. YH Software Inc. Corp.


matrix = [[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9]]
#print(matrix)
count = 0
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if i < j:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            count += 1
# print(matrix)
# print(count)

matrix = [[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9]]
for c in range(len(matrix[0])):
    tm = [0] * len(matrix[0])
    for i in range(len(tm)):
        tm[i] = [0] * len(matrix)
    #print(tm)
    for i, row in enumerate(tm):
        #print(i,row)
        for j, col in enumerate(row):
            #print(j, col)
            #print(tm[i][j], matrix[j][i])
            tm[i][j] = matrix[j][i]
print(matrix)
print(tm)
