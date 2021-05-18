# This example takes as input our intermediate dict file called begin
# and transforms it into a dict called end which gets passed into the dataframe

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


def build_param_ary_for_param(symbolary, paramset, start):
    dict_df = {}
    for param in paramset:
        paramary = []
        for symbol in symbolary:
            ary = start[symbol]
            value = get_param_for_symbol(param, ary)
            paramary.append(value)
        dict_df[param] = pd.Series(paramary, index=symbolary)
    return dict_df


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
    symbolary = tuple[0]
    paramset = tuple[1]
    d = build_param_ary_for_param(symbolary, paramset, begin)
    df = pd.DataFrame(d)
    pd.set_option("display.max_rows", None)
    print(df)
