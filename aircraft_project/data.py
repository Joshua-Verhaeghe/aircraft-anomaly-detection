import pandas as pd
import os
from .config import get_filepath


def load_data(filename):
    
    file_path = get_filepath(filename, folder="raw")
    df = pd.read_csv(file_path)

    return df

def save_data(df, filename):

    file_path = get_filepath(filename, folder="processed")
    df.to_csv(file_path, index=False)