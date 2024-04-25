import pandas as pd

# Specify the dataset path
dataset_path = "Insurance.csv"

data = pd.read_csv(dataset_path)

# Print the column names
print("Columns:")
print(data.columns)

selected_columns=['age','bmi','children','charges']
summary=data[selected_columns].describe(percentiles=[.25,.5,.75])

summary=summary.rename(index={'25%':'25%','50%':'50%','75%':'75%'})
print(summary)