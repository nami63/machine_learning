import pandas as pd
dataset_path="iris.csv"
dataset=pd.read_csv(dataset_path)

x=dataset[['septal_length']]
y=dataset['petal_lengeth']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=43,test_size=0.5)

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

from sklearn.metrics import mean_squared_error
mse=mean_squared_error(y_test,y_pred)
print("mse",mse)