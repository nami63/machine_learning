import numpy as np
from sklearn.datasets import load_iris

data=load_iris()
x=data.data
y=data.target

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(x,y,random_state=40,test_size=0.45)

from sklearn.tree import DecisionTreeRegressor
clf=DecisionTreeRegressor()
clf.fit(X_train,y_train)

from sklearn.metrics import accuracy_score
y_pred=clf.predict(X_test)
print("train accuracy:",accuracy_score(y_true=y_train,y_pred=clf.predict(X_train)))
print("train accuarcy:",accuracy_score(y_true=y_test,y_pred=y_pred))
      
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
plot_tree(clf,feature_names=data.feature_names,class_names=data.target_names,filled=True)
plt.show()