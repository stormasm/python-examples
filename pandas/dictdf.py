import pandas as pd


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


def process_intermediate_dict(idict):
    tuple = get_symbolary_paramset(idict)
    symbolary = tuple[0]
    paramset = tuple[1]
    d = build_param_ary_for_param(symbolary, paramset, idict)
    return d
