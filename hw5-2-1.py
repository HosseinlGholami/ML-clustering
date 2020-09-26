import pandas as pd
import numpy  as np
path='F:\Data\data2-x.csv'
df=pd.read_csv(path)

path='F:\Data\data2-y.csv'
df1=pd.read_csv(path)

from sklearn.cluster import KMeans

score=list()

for i in [10]:    
    kmeans = KMeans(
                    n_clusters=i,   #tedad cluster
                    init='k-means++', #doortarin noghgte,
                    #ndarray ham baraye delkhah (n_clusters, n_features)
                    n_init=10, #tedad bar hayi ke algoritm bayad ejra shavad
                    max_iter=300, #maximom tekar algoritm
                    tol=0.0001,#tolerance baraye converg shodan
                    precompute_distances='auto', #if active (faster but takes more memory)copy_x=True,
                    algorithm='full'
                    )
    Learned = kmeans.fit(df)
    
    
    labels = Learned.predict(df)
    unique, counts = np.unique(labels, return_counts=True)
    unique1, counts1 = np.unique(df1, return_counts=True)
     

#    import matplotlib.pyplot as plt
#    plt.plot(unique,counts,'ro')
#    plt.xlabel(i)
#    plt.show()
print('____________clustering____________')
for i in range(10):
    print( unique[i],':',counts[i],'\n')

print('____________labaled data____________')
for i in range(10):
    print( unique1[i],':',counts1[i],'\n')

# Getting the cluster labels
# Centroid values
#centroids = kmeans.cluster_centers_