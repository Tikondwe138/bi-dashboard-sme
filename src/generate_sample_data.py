# src/generate_sample_data.py

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

def generate_sample_data(output_path="data/sample_sales_data.csv", num_days=100):
    np.random.seed(42)
    random.seed(42)

    regions = ['Central', 'Northern', 'Southern']
    products = ['Maize Seeds', 'Fertilizer', 'Pesticides', 'Irrigation Kit', 'Animal Feed']
    genders = ['Male', 'Female']

    start_date = datetime(2024, 1, 1)
    dates = [start_date + timedelta(days=i) for i in range(num_days)]

    data = []
    for date in dates:
        region = random.choice(regions)
        product = random.choice(products)
        sales = random.randint(1000, 10000)
        profit = int(sales * random.uniform(0.1, 0.3))
        age = random.randint(18, 65)
        gender = random.choice(genders)

        data.append({
            "Date": date.strftime("%Y-%m-%d"),
            "Region": region,
            "Product": product,
            "Sales": sales,
            "Profit": profit,
            "Customer Age": age,
            "Customer Gender": gender
        })

    df = pd.DataFrame(data)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"Sample data saved to {output_path}")

if __name__ == "__main__":
    generate_sample_data()
