import pandas as pd

df = pd.read_csv("data1.csv", dtype_backend="pyarrow", engine="pyarrow")
