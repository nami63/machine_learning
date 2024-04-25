x=[[12,7],[4,8],[3,8]]
r=[[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        r[j][i]=x[i][j]
for i in r:
    print(r)