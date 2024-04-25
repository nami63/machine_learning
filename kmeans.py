import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

from sklearn.cluster import KMeans

x,_=make_blobs(n_samples=300,centers=4,cluster_std=0.60,random_state=0)
kmeans=KMeans(n_clusters=4)
kmeans.fit(x)
y_means=kmeans.predict(x)
centers=kmeans.cluster_centers_


plt.figure(figsize=(8,6))
plt.scatter(x[:,0],x[:,1],s=50)
plt.scatter(centers[:,0],centers[:,1],c='red')
plt.title('k-mean')
plt.xlabel('fig1 ')
plt.ylabel('fig2 ')
plt.show()
