import pandas as pd

def test1():
    d = {
        "cashflow": pd.Series(
            ["100.0M", "200.0M", "300.0M"], index=["ibm", "ui", "zm"]
        ),
        "mcap": pd.Series(["400.0M", "500.0M", "600.0M"], index=["ibm", "ui", "zm"]),
    }
    df = pd.DataFrame(d)
    return df


if __name__ == "__main__":
    df = test1()
    pd.set_option("display.max_rows", None)
    print(df)
