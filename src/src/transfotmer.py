import pandas as pd

def transform(data):
    df = pd.DataFrame(data)
    df["quote_length"] = df["quote"].apply(len)
    return df