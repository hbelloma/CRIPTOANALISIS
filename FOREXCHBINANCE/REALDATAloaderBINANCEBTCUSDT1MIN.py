#
# pip install websocket_client
#

import websocket
import json
import pprint

SOCKET="wws://stream.binance.com:9443/ws/btcusdt@kline_1m"   #Conección a binance para datos en tiempo real BTCUSD 1 min data

def on_open(ws):
    print('opened connection')
def on_close(ws):
    print('close connection')
def on_message(ws,message):
    #print(message)  #imprime los datos como van llegando
    json_message = json.loads(message) #los transformamos en formato json
    pprint.pprint(json_message)


ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message) #funcion websocket para cargar datos en tiempo real
ws.run_forever()