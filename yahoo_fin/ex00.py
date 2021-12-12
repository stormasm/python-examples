from yahoo_fin.stock_info import get_quote_table, get_stats

info = get_quote_table("ui")
print(info)
stats = get_stats("ui")
print(stats)
