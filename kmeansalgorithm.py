import pandas as pd

# Goal is to imgaine a swarm of fireflies scattered across a garden at night.
# The task is to group these fireflies based on their poximity to each other using k-means unsupervised learning algorithm

dataset = pd.DataFrame({
    'x': [59,68,32,59,44,60,26,23,67,16,61,64,37,61,57,49,13,72,30,15],
    'y':[63,51,35,15,30,24,29,65,28,47,70,46,67,72,41,59,48,36,24,45]
})

from sklearn import cluster
import matplotlib.pyplot as plt
# Next step is to specify number of clusters (k) how many clusters we want to divide our data into
kmeans = cluster.KMeans(n_clusters=2)
# Next step is to train our KMeans model with out datasheet we made before.
kmeans.fit(dataset)

# Last step is to look into the labels and the cluster centers

labels = labels = kmeans.labels_
centers = kmeans.cluster_centers_
print(labels)

print(centers)

#lastly we visualize our clusters and plot our data points. here we look for the centers of clusters (centroids)

plt.scatter(dataset['x'], dataset['y'],c=labels)
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='red')
plt.show()