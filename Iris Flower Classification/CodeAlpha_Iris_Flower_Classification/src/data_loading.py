import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    if 'Id' in df.columns:
        df.drop('Id', axis=1, inplace=True)

    X = df.drop('Species', axis=1)
    y = df['Species']

    return df, X, y