import pandas as pd

begin = {
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


def get_param_for_symbol(param, ary):
    for dict in ary:
        keys = dict.keys()
        if param in keys:
            return dict[param]


def build_param_ary_for_symbol(symbolary, paramset, start):
    for param in paramset:
        print(param)
        for symbol in symbolary:
            print(symbol)
            ary = start[symbol]
            value = get_param_for_symbol(param, ary)
            print(value)


def get_symbolary_paramset(start):
    symbolary = []
    paramset = set()
    for symbol in start:
        symbolary.append(symbol)
        aryd = start[symbol]
        for dict in aryd:
            params = dict.keys()
            for param in params:
                paramset.add(param)
    return (symbolary, paramset)


if __name__ == "__main__":
    tuple = get_symbolary_paramset(begin)
    print(tuple)
    symbolary = tuple[0]
    paramset = tuple[1]
    build_param_ary_for_symbol(symbolary, paramset, begin)
