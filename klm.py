import threading
import pandas as pd

# Load the Iris dataset
iris = pd.read_csv("iris.csv")
print(iris.columns)