import pandas as pd
import os

def save_to_csv(data, filename="data/Amazon_Products.csv"):
    """Save DataFrame to CSV, creating the 'data' folder if it does not exist."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)  

    if data is not None and not data.empty:
        try:
            data.to_csv(filename, index=False)
            print(f"Data saved to {filename}")
        except Exception as e:
            print(f"Error saving data to CSV: {e}")
    else:
        print("⚠️ No data to save.")
