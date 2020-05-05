import pandas as pd
import ta

# Load data
df = pd.read_csv('ui.csv', sep=',')

# Clean nan values
df = ta.utils.dropna(df)

print('negative_volume_index')
print(ta.volume.negative_volume_index(close=df['close'],volume=df['volume']))
print('-----------------------------------')
print('on balance volume indicator')
print(ta.volume.on_balance_volume(close=df['close'],volume=df['volume']))
print('-----------------------------------')
