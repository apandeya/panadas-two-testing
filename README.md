# Pandas 2.0 what has changed ?

All new changes can be classified into two kinds:

1. Performance enhancement

2. Increased reliability

For a small dataset the performance actually seems worse:

```bash
read_csv_pyarrow_engine_and_dtype took 0.934 ms per loop. Total loops = 10000
read_csv_pyarrow_engine took 0.828 ms per loop. Total loops = 10000
read_csv_numpy took 0.676 ms per loop. Total loops = 10000
```

Running it several times even with different orders also does not produce any different result:

```bash
read_csv_numpy took 0.69 ms per loop. Total loops = 10000
read_csv_pyarrow_engine_and_dtype took 0.99 ms per loop. Total loops = 10000
read_csv_pyarrow_engine took 0.90 ms per loop. Total loops = 10000
```

But as soon as we switch to a larger file like scm export here are the resilts:

```bash
read_csv_numpy took 258.5 ms per loop. Total loops = 10
read_csv_pyarrow_engine_and_dtype took 28.5 ms per loop. Total loops = 10
read_csv_pyarrow_engine took 77.5 ms per loop. Total loops = 10
```

In none of the experiments we have specified the dtype.

If we think about it using pyarrow backend should provide parquet file performance for pretty much every dtype.

```bash
read_csv_pyarrow_engine_and_dtype took 21.6 ms per loop. Total loops = 100
read_parquet took 15.48 ms per loop. Total loops = 100
```
