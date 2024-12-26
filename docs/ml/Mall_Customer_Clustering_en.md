## Dataset Summary
- Total data points: 200
- Columns: 5
    - Customer: Customer ID
    - Age: Customer age
    - Annual Income (k$): Customer annual income
    - Spending Score (1-100): Customer spending score


## KMeans Modeling
K-means is one of the unsupervised learning algorithms that partitions data into k clusters.

### WSS
WCSS (Within-Cluster Sum of Squares) is a metric in K-means clustering that measures how close the data points within a cluster are to the cluster centroid.
```python
from sklearn.preprocessing import StandardScaler

# Load data
df = pd.read_csv('data/Mall_Customers.csv')

# Select necessary columns
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# KMeans modeling
wcss = []  # Within-Cluster Sum of Squares

for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Visualize the elbow graph
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('WCSS')
plt.show()

```
![](https://github.com/eungyukm/TeamPythonRun/blob/main/docs/images/Elbow.png)

## Hierarchical Clustering
### Data Loading and Preprocessing
- We perform clustering using only the Annual Income and Spending Score from the Mall Customers dataset.
- The data is standardized using StandardScaler to ensure that clustering results are not affected by scale differences.

### Dendrogram
- A dendrogram visually represents the hierarchical structure of clustering.
- The ward method minimizes variance between clusters.
- The point where the vertical line bends significantly indicates the optimal location to split clusters.

### AgglomerativeClustering
- We use AgglomerativeClustering to divide the data into 5 clusters.
- The ward method is applied to iteratively merge clusters.
- fit_predict is used to perform clustering and assign each data point to a cluster.

### Visualization
- Data points are color-coded by cluster for visualization.
- While cluster centers are not displayed, the density and distribution of clusters can be observed.
```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/Mall_Customers.csv')

# Select relevant columns (Annual Income, Spending Score)
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Plot Dendrogram
plt.figure(figsize=(12, 6))
linked = linkage(X_scaled, method='ward')
dendrogram(linked)
plt.title('Dendrogram for Hierarchical Clustering')
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.show()

# Agglomerative Clustering
agg_clustering = AgglomerativeClustering(n_clusters=5, linkage='ward')
clusters = agg_clustering.fit_predict(X_scaled)

# Add cluster results to dataframe
df['Cluster'] = clusters

# Visualize clustering results
plt.figure(figsize=(10, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters, cmap='viridis', s=100, alpha=0.7)
plt.title('Agglomerative Clustering (k=5)')
plt.xlabel('Annual Income (Standardized)')
plt.ylabel('Spending Score (Standardized)')
plt.colorbar(label='Cluster')
plt.show()

# View cluster distribution
print(df['Cluster'].value_counts())
```
![](https://github.com/eungyukm/TeamPythonRun/blob/main/docs/images/Dendrogram.png)
![](https://github.com/eungyukm/TeamPythonRun/blob/main/docs/images/Agglomerative.png)

## DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
- Density-based clustering algorithm
- Forms clusters if a minimum number of points exist within a specified distance
- Capable of distinguishing noise and outliers, effectively identifying clusters of complex shapes
```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/Mall_Customers.csv')

# Select relevant columns (Annual Income, Spending Score)
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# DBSCAN modeling
dbscan = DBSCAN(eps=0.9, min_samples=5)
clusters = dbscan.fit_predict(X_scaled)

# Add cluster results to dataframe
df['Cluster'] = clusters

# Visualize clustering results
plt.figure(figsize=(10, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters, cmap='viridis', s=100, alpha=0.7)
plt.title('DBSCAN Clustering')
plt.xlabel('Annual Income (Standardized)')
plt.ylabel('Spending Score (Standardized)')
plt.colorbar(label='Cluster')
plt.show()

# View cluster distribution
print(df['Cluster'].value_counts())
```
![](https://github.com/eungyukm/TeamPythonRun/blob/main/docs/images/DBSCAN.png)
