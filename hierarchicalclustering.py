from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import numpy as np


dataset = pd.DataFrame({
    'x': [59,68,32,59,44,60,26,23,67,16,61,64,37,61,57,49,13,72,30,15],
    'y':[63,51,35,15,30,24,29,65,28,47,70,46,67,72,41,59,48,36,24,45]
})

cluster = AgglomerativeClustering(n_clusters=2,metric='euclidean',linkage='ward')
cluster.fit_predict(dataset)
print(cluster.labels_)