#
# install binance library
#  pip install python-binance
#
#

import config, csv
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET) #cargado desde config.py

#prices =client.get_all_tickers()
#for price in prices
#    print(price)

csvfile = open('2020_15minute.csv', 'w', newline='')   #abrimos csv con formato w write
candlestick_writer = csv.writer(csvfile, delimiter=',') # escribimos csv con espacios delimitados por ,

candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jul, 2020", "12 Ju, 2020")
#candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2020", "12 Ju, 2020")  

for candlestick in candlesticks:
    candlestick[0] = candlestick[0] / 1000
    candlestick_writer.writerow(candlestick)

csvfile.close()    
