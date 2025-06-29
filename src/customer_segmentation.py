import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def segment_customers(df, n_clusters=3):
    """
    Cluster customers based on Age and Sales.
    Returns dataframe with a 'Segment' column added.
    """
    # Ensure required columns exist
    if 'Customer Age' not in df.columns or 'Sales' not in df.columns:
        raise ValueError("DataFrame must contain 'Customer Age' and 'Sales' columns.")

    features = df[['Customer Age', 'Sales']].copy()
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df = df.copy()
    df['Segment'] = kmeans.fit_predict(features_scaled)
    return df
