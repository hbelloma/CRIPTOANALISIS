#  The following program to try to predict next day price based on past 60 days data
#  using python and neural networks with sequential data (level of accuracy not tested) 
#
# Install following libraries/packages before running program, using next console command lines :
#  pip install numpy
#  pip install pandas
#  pip install matplotlib
#  pip install pandas-datareader 
#  pip install mplfinance
#  pip install tensorflow
#  pip install sklearn
#  pip install scikit-learn

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt
import mplfinance as mpf #for ploting with japanese candles

# FOR ML MODEL
from sklearn.preprocessing import MinMaxScaler #to scale finantial data between 0 and 1
from tensorflow.keras.layers import Dense, Dropout, LSTM    # layers important for secuential data
from tensorflow.keras.models import Sequential

# GETTING DATA
crypto_currency = 'BTC'
against_currency = 'USD'
start = dt.datetime(2016,1,1)
end = dt.datetime.now()
data= web.DataReader(f'{crypto_currency}-{against_currency}','yahoo',start,end)
#mpf.plot(data, type="candle", volume=True, style="yahoo")  # japanese candle plot

# PREPARE DATA
#print(data.head()) 

scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(data['Close'],values,reshape(-1,1))

# LAST DAYS FOR PREDICTION
prediction_days = 60

x_train, y_train = [], []

for x in range(prediction_days, len(scaled_data)):
    x_train.append(scaled_data[x-prediction_days:x,0])
    y_train.append(scaled_data[x,0])

x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1],1))   #let's reshape

# CREATE THE NEURAL NETWORK  (MODEL FOR REDICTION) 
# if there are issues with numpy 1.20 downgrade  numpy 1.19.5 as follows
# pip install numpy==1.19.5 

model = Sequential()

model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(Dropout(0.2)) #to prevent overfit the network
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50))
model.add(Dropout(0.2))
model.add(Dense(units=1))  #final number that give the price

model.compile(optimizer='adam', loss='mean_squared_error') #compile
model.fit(x_train, y_train, epochs=25, batch_size=32) # train

# TESTING THE MODEL

test_start = dt.datetime(2020,1,1)
test_end = dt.datetime.now()
test_data= web.DataReader(f'{crypto_currency}-{against_currency}','yahoo',test_start,test_end)
actual_prices = test_data['Close'].values

total_dataset = pd.concat((data['Close'], test_data['Close']), axis=0)

model_inputs = total_dataset[len(total_dataset) - len(test_data) - prediction_days:].values
model_inputs = model_inuts.reshape(-1,1)
model_inputs = scaler.fit_transform(model_inputs)

x_test = []
for x in range(prediction_days, len(model_inputs)):
    x_test.append(model_inputs[x-prediction_days:x, 0])

x_test = np.array(x_test)
x_test = np.reshape(xtest, (x_test.shape[0], x_test.shape[1], 1))   #actual prices

prediction_prices = model.predict(x_test)
prediction_prices = scaler.inverse_transform(prediction_prices)  #prediction prices

# PLOTING IN MATPLOTLIB

plt.plot(actual_prices, color='black', label='Actual Prices')
plt.plot(prediction_prices, color='green', label='Predicted Prices')
plt.title(f'{crypto_currency} price prediction')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.show()
