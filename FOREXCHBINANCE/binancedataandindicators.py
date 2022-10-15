# librerias a instalar con siguientes comandos
# pip install  ccxt
#

import ccxt  #trabajar cn estraccion de datos cripto dif exchange
import yfinance
import pandas_ta as ta  #for tecnical analysis
import pandas as pd

exchange = ccxt.binance()

bars = exchane.fetch_ohlcv('ETH/USDT', timeframe='5m', limit=500) #max limit 1000
df = pd.DataFrame(bars, columns=['time','open','high','low','close','volume'])
#print(df)

# SOME INDICATORS
adx = ta.adx(df['high'],df['low'], df['close'])
adx = df.ta.adx()
macd = df.ta.macd(fast=14, slow=28)
#printf(macd)
rsi = df.ta.rsi()

#concatenando toda la info en un mismo data frame
df = pd.concat([df,adx,macd,rsi],axis=1)
#print(df)

df = df[df['RSI_14'] < 30] #filtrando valores con RSI<30 tambien puede hacerse RSI>70 para shorts

#print(adx.tail(20))
