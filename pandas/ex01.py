import pandas as pd

start = {
    "ibm": [{"mcap": "129.284B"}, {"cashflow": "15.94B"}],
    "zm": [{"cashflow": "1.35B"}, {"mcap": "90.478B"}],
    "docu": [{"mcap": "36.23B"}, {"cashflow": "540.45M"}],
    "rdfn": [{"mcap": "5.225B"}, {"cashflow": "-46.28M"}],
    "ui": [{"cashflow": "457.15M"}, {"mcap": "17.838B"}],
}

end = {
    "cashflow": pd.Series(
        ["15.94.B", "1.35B", "540.45B", "-46.28M", "457.15M"],
        index=["ibm", "zm", "docu", "rdfn", "ui"],
    ),
    "mcap": pd.Series(
        ["129.284B", "90.478B", "36.23B", "5.225B", "17.838B"],
        index=["ibm", "zm", "docu", "rdfn", "ui"],
    ),
}


def test1():
    for symbol in start:
        print(symbol)
        aryd = start[symbol]
        for d in aryd:
            print(d)


if __name__ == "__main__":
    df = test1()
    pd.set_option("display.max_rows", None)
