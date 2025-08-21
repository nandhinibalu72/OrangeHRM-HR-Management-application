import pandas as pd

def csv_records(path: str):
    df = pd.read_csv(path)
    return df.to_dict("records")
