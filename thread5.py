import threading
import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target_names[iris.target]

# Divide the dataset by variants
setosa = df[df['species'] == 'setosa']
versicolor = df[df['species'] == 'versicolor']
virginica = df[df['species'] == 'virginica']

# Find the largest and smallest flowers based on petal length
largest_setosa = setosa.nlargest(3, 'petal length (cm)')
smallest_setosa = setosa.nsmallest(3, 'petal length (cm)')

largest_versicolor = versicolor.nlargest(3, 'petal length (cm)')
smallest_versicolor = versicolor.nsmallest(3, 'petal length (cm)')

largest_virginica = virginica.nlargest(3, 'petal length (cm)')
smallest_virginica = virginica.nsmallest(3, 'petal length (cm)')

# Define thread functions
def write_largest_flowers():
    largest_flowers = pd.concat([largest_setosa, largest_versicolor, largest_virginica])
    largest_flowers.to_csv("output_file1.csv", index=False)

def write_smallest_flowers():
    smallest_flowers = pd.concat([smallest_setosa, smallest_versicolor, smallest_virginica])
    smallest_flowers.to_csv("output_file2.csv", index=False)

# Start the threads
thread1 = threading.Thread(target=write_largest_flowers)
thread2 = threading.Thread(target=write_smallest_flowers)

thread1.start()
thread2.start()

# Join the threads
thread1.join()
thread2.join()

print("Threads have finished writing to output files.")
