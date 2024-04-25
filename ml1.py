import pandas as pd

dataset_path="house.csv"
data=pd.read_csv(dataset_path)

print(data.head())
print(data.info())

x=data[['area','no_bed','loca']]
y=data['price']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.3)

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_train,y_train)

from sklearn.metrics import mean_squared_error
y_pred=model.predict(x_test)
mse=mean_squared_error(y_test,y_pred)
print(mse)



from sklearn.tree import DecisionTreeRegressor
model=DecisionTreeRegressor(random_state=42)
model.fit(x_train,y_train)

y_predd=model.predict(x_test)
msed=mean_squared_error(y_test,y_predd)
print(msed)