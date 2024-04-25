import numpy as np
from sklearn.datasets import load_iris

data=load_iris()
x=data.data
y=data.target

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.25)

from sklearn.ensemble import RandomForestRegressor
regressor=RandomForestRegressor(n_estimators=100,random_state=42)
regressor.fit(x_train,y_train)

from sklearn.metrics import mean_squared_error
y_pred=regressor.predict(x_test)
mse=mean_squared_error(y_test,y_pred)

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
plt.figure(figsize=(16,3))
plot_tree(regressor.estimators_[0],feature_names=data.feature_names,class_names=data.target_names,filled=True)
plt.show()