
#print(type(ui))
#<class 'pandas.core.frame.DataFrame'>

from yahoo_fin.stock_info import get_stats

ui = get_stats("UI")
print(ui)
#print(ui.dtypes)
#print(ui.tail(100))
#ui.to_csv('ui.csv')
