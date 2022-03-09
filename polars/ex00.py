import polars as pl

df = pl.DataFrame(
    {
        "A": [1, 2, 3, 4, 5],
        "fruits": ["banana", "banana", "apple", "apple", "banana"],
        "B": [5, 4, 3, 2, 1],
        "cars": ["subaru", "audi", "beetle", "ford", "beetle"],
    }
)
print(df.sort("cars"))
