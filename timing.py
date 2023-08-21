from timeit import timeit

import pandas as pd

filename = "de-2022-W46-scm-export.csv"
file_parquet = "de-2022-W46-scm-export.parquet"

number = 100


def read_csv_pyarrow_engine_and_dtype():
    return pd.read_csv(filename, dtype_backend="pyarrow", engine="pyarrow", sep=";")


def read_csv_numpy():
    return pd.read_csv(filename, sep=";")


def read_csv_pyarrow_engine():
    return pd.read_csv(filename, engine="pyarrow", sep=";")


def read_parquet():
    return pd.read_parquet(file_parquet)


# number = 10

# time_numpy = timeit('read_csv_numpy()', globals=globals(), number=number)
# print(f"read_csv_numpy took {time_numpy*1000/number} ms per loop. Total loops = {number}")

time_pyarrow = timeit("read_csv_pyarrow_engine_and_dtype()", globals=globals(), number=number)
print(
    f"read_csv_pyarrow_engine_and_dtype took {time_pyarrow*1000/number} ms per loop. Total loops = {number}"
)

# time_pyarrow = timeit('read_csv_pyarrow_engine()', globals=globals(), number=number)
# print(f"read_csv_pyarrow_engine took {time_pyarrow*1000/number} ms per loop. Total loops = {number}")

# df = read_csv_pyarrow_engine_and_dtype()

# df.to_parquet(file_parquet)

time_parquet = timeit("read_parquet()", globals=globals(), number=number)
print(f"read_parquet took {time_parquet*1000/number} ms per loop. Total loops = {number}")
