
#print(type(ui))
#<class 'pandas.core.frame.DataFrame'>

from yahoo_fin.stock_info import get_data, tickers_sp500, tickers_nasdaq, tickers_other, get_quote_table

ui = get_data("UI")
print(ui)
