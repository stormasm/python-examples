import pandas as pd
import ta

# Load data
df = pd.read_csv('ui.csv', sep=',')

# Clean nan values
df = ta.utils.dropna(df)

print('money flow index')
print(ta.volume.money_flow_index(high=df['high'],low=df['low'],close=df['close'],volume=df['volume']))
print('-----------------------------------')
