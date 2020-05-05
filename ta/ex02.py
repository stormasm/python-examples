import pandas as pd
import ta

# Load data
df = pd.read_csv('ui.csv', sep=',')

# Clean nan values
df = ta.utils.dropna(df)

print('money flow index')
print(ta.volume.money_flow_index(high=df['high'],low=df['low'],close=df['close'],volume=df['volume']))
print('-----------------------------------')
print('volume weighted average price')
print(ta.volume.volume_weighted_average_price(high=df['high'],low=df['low'],close=df['close'],volume=df['volume']))
print('-----------------------------------')
print('accumulation distribution index')
print(ta.volume.acc_dist_index(high=df['high'],low=df['low'],close=df['close'],volume=df['volume']))
print('-----------------------------------')
print('chaikin money flow(CMF)')
print(ta.volume.chaikin_money_flow(high=df['high'],low=df['low'],close=df['close'],volume=df['volume']))
print('-----------------------------------')
print('ease of movement')
print(ta.volume.ease_of_movement(high=df['high'],low=df['low'],volume=df['volume']))
print('-----------------------------------')
print('sma ease of movement')
print(ta.volume.sma_ease_of_movement(high=df['high'],low=df['low'],volume=df['volume']))
print('-----------------------------------')
print('average true range')
print(ta.volatility.average_true_range(high=df['high'],low=df['low'],close=df['close']))
print('-----------------------------------')
