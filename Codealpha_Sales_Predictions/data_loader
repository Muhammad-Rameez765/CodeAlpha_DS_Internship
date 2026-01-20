import pandas as pd
import numpy as np

def load_and_clean_data(filepath):
    """Loads advertising data and removes unnecessary columns."""
    df = pd.read_csv(filepath)
    # Remove the 'Unnamed: 0' column if it exists
    if 'Unnamed: 0' in df.columns:
        df = df.drop(axis=1, columns='Unnamed: 0')
    
    print("Dataset Loaded Successfully.")
    print(df.info())
    return df

if __name__ == "__main__":
    # Test loading
    data = load_and_clean_data('Advertising.csv')
    print(data.head())
