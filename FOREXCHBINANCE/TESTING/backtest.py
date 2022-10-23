#
# Librerias a instalar
# ir a https://www.lfd.uci.edu/~gohike/pythonlibs/#ta-lib
# TA-Lib  buscar la version para el SO y 64-32 bits, y guardar en la misma carpeta
# pip install TA-Lib-0.4.17-cp37-cp37m-win_amd64.whl
#  o pip intall bta-lib
#
# Para plot Downgrade until the bug in backtrader is fixed
# pip uninstall matplotlib
# pip install matplotlib==3.2.2
#

import backtrader as bt
import datetime 

class RSIStrategy(bt.Strategy):

    def _init_(self):
        self.rsi = bt.talib.RSI(self.data, period=14)

    def next(self)
        if self.rsi < 30 and not sef.position:
           self.buy(size=1)
 
        if self.rsi > 70 and self.position:
	   selfe.close()

cerebro = bt.Cerebro()

fromdate = datetime.datetime.strptime('2020-07-01', '%Y-%m-%d')
todate = datetime.datetime.strptime('2020-07-12', '%Y-%m-%d')

data = bt.feeds.GenericCSVData(datename='2020_15minute.csv', dtformat=2, compression=15, timeframe=bt.TimeFrame.Minutes, fromdate=fromdate, todate=todate)
cerebro.adddata(data)
cerebro.addstrategy(RSIStrategy) 
cerebro.run()    
cerebro.plot()    