
#print(type(ui))
#<class 'pandas.core.frame.DataFrame'>

from yahoo_fin.stock_info import get_data

ui = get_data("UI").round(2)
#print(ui.dtypes)
print(ui.tail(100))
#ui.to_csv('ui.csv')
