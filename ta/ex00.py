import pandas as pd
import ta

# Load data
df = pd.read_csv('ui.csv', sep=',')

# Clean nan values
df = ta.utils.dropna(df)

print('roc')
print(ta.momentum.roc(close=df['close']),40)
print('-----------------------------------')
print('rsi')
print(ta.momentum.rsi(close=df['close']),40)
print('-----------------------------------')
print('bollinger_mavg')
print(ta.volatility.bollinger_mavg(close=df['close']),200)
print('-----------------------------------')
print('aroon')
print(ta.trend.aroon_up(close=df['close']),200)
print(ta.trend.aroon_down(close=df['close']),200)
print('-----------------------------------')
print('dpo')
print(ta.trend.dpo(close=df['close']),200)
print('-----------------------------------')
print('ema_indicator')
print(ta.trend.ema_indicator(close=df['close']),200)
print('-----------------------------------')
