import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,3,4,5,6])
y=np.array([2,4,6,8,10,12])

m_x=np.mean(x)
m_y=np.mean(y)

N=np.sum((x-m_x)*(y-m_y))
D=np.sum((x-m_x)**2)

m=N/D
b=m_y-m*m_x
reg=m*x+b

plt.scatter(x,y,label="points")
plt.plot(x,reg,color="blue",label="linear_regression")

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
