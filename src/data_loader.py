import pandas as pd
import os

def load_data(path="data/sample_sales_data.csv"):
    """
    Load sales data from a CSV file.

    Args:
        path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded DataFrame, or empty DataFrame if file not found.
    """
    if not os.path.exists(path):
        return pd.DataFrame()  # Return empty DataFrame if file does not exist
    try:
        df = pd.read_csv(path, parse_dates=["Date"])
        return df
    except Exception as e:
        # Optionally, log the error or print for debugging
        print(f"Error loading data: {e}")
        return pd.DataFrame()
