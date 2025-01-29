import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'data.xlsx'  # Ubah dengan path file Anda
df = pd.read_excel(file_path)

# Ekstraksi longitude dan latitude dari kolom "LongLat"
df[['Latitude', 'Longitude']] = df['LongLat'].str.split(',', expand=True).astype(float)

# Buang baris dengan nilai NaN pada latitude atau longitude
df_cleaned = df.dropna(subset=['Latitude', 'Longitude'])

# Ambil koordinat untuk clustering
coordinates = df_cleaned[['Latitude', 'Longitude']]

# Clustering dengan K-Means
kmeans = KMeans(n_clusters=12, random_state=42, n_init=10)
df_cleaned['Cluster'] = kmeans.fit_predict(coordinates)

# Simpan hasil clustering ke file baru
output_file = 'clustered_data.xlsx'
df_cleaned.to_excel(output_file, index=False)

# Visualisasi hasil clustering
plt.figure(figsize=(10, 6))
for cluster in range(12):
    cluster_data = df_cleaned[df_cleaned['Cluster'] == cluster]
    plt.scatter(cluster_data['Longitude'], cluster_data['Latitude'], label=f'Cluster {cluster}')

plt.scatter(kmeans.cluster_centers_[:, 1], kmeans.cluster_centers_[:, 0], 
            color='black', marker='x', s=100, label='Centroids')
plt.title('Clustering Wilayah')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.grid(True)
plt.show()
