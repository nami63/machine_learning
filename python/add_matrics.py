x=[[12,3,5],[4,5,6],[7,8,9]]
y=[[5,9,2],[4,5,6],[2,5,6]]

r=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        r[i][j]=x[i][j]+y[i][j]

for i in r:
    print(i)

r_multiplication = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Perform matrix multiplication
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            r_multiplication[i][j] += x[i][k] * y[k][j]

# Print the result of matrix multiplication
print("\nMatrix Multiplication:")
for row in r_multiplication:
    print(row)