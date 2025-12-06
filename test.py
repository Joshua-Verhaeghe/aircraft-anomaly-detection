# test.py
from aircraft_project import load_data, save_data
from aircraft_project import split_columns, create_time_index, normalisation
from aircraft_project import detect_abnormal_windows, get_abnormal_windows
from aircraft_project import get_filepath

df = load_data(get_filepath("dataset.csv", folder="raw"))
df = split_columns(df)
df = create_time_index(df)
df = normalisation(df, ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10", "p11"])
print(df.head())
