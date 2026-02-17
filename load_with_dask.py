import dask.dataframe as dd

# Load CSV using Dask
df = dd.read_csv("data.csv")

# Display first 10 rows
print("First 10 Rows:")
print(df.head(10))

# Show number of partitions
print("\nNumber of Partitions:")
print(df.npartitions)
