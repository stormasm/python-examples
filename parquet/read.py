import argparse
import pyarrow.parquet as pq


def readfile(filename):
    table = pq.read_table(filename)
    print(table.to_pandas())


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", default="ex00.parquet")
    args = parser.parse_args()
    filename = args.filename
    readfile(filename)
