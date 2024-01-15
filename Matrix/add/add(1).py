####this time we are going to use ower own method 

A = [[1,2],[3,4]]
B = [[1,2],[3,4]]

result = [[0,0],[0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

for i in result:
    for j in  i:
        print(j,end=" ")
    print()