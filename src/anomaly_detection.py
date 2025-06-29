import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_sales_anomalies(df, contamination=0.05):
    """
    Detect anomalies in sales data using Isolation Forest.
    Assumes df has columns: 'Date', 'Sales'.
    Returns df with an additional 'Anomaly' boolean column.
    """
    if df.empty or 'Sales' not in df.columns:
        raise ValueError("DataFrame must contain 'Sales' column and not be empty.")

    df_sorted = df.sort_values('Date').copy()
    model = IsolationForest(contamination=contamination, random_state=42)
    df_sorted['Anomaly'] = model.fit_predict(df_sorted[['Sales']])
    df_sorted['Anomaly'] = df_sorted['Anomaly'] == -1
    return df_sorted
