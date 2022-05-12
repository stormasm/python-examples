import pyarrow.parquet as pq

table = pq.read_table("ex00.parquet")
print(table.to_pandas())
