import pandas as pd

dataset_path="customer.csv"
data=pd.read_csv(dataset_path)

print(data.head())
print(data.info())

x=data[['age','income','spending_habits']]
y=data['churn']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.2)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)
from sklearn.metrics import mean_squared_error,precision_score,accuracy_score,recall_score
a=accuracy_score(y_test,y_pred)
p=precision_score(y_test,y_pred)
r=recall_score(y_test,y_pred)
