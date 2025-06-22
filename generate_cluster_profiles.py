import pandas as pd

# Load data with cluster labels
df = pd.read_csv('personality_dataset_with_clusters.csv')

# Get numeric columns
numeric_cols = df.select_dtypes(include='number').columns

# Group by cluster and calculate mean values
cluster_summary = df.groupby('Cluster')[numeric_cols].mean().reset_index()
cluster_summary.to_csv('cluster_profiles.csv', index=False)
print("Cluster profiles saved to cluster_profiles.csv")