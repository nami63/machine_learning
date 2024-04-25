import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x=np.array([1,2,3,4,5]).reshape(-1,1)
y=np.array([2,4,5,7,9])

model=LinearRegression()
model.fit(x,y)
prediction=model.predict(x)

plt.scatter(x,y,color="blue",label="points")
plt.plot(x,prediction,label="linear regression")
plt.xlabel("x")
plt.ylabel("y")
plt.show()