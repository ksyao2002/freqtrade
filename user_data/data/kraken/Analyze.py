# pragma pylint: disable=missing-docstring, invalid-name, pointless-string-statement
# flake8: noqa: F401
# isort: skip_file
# --- Do not remove these libs ---
import numpy as np  # noqa
import pandas as pd  # noqa
from pandas import DataFrame

from scipy.fft import fft, ifft
import matplotlib.pyplot as plt

data_df = pd.read_json('BTC_USDT-1m.json')
data_df_total = data_df
data_df = data_df_total.iloc[0:int(data_df_total.shape[0]*0.8), 0:6]
testdat = data_df_total.iloc[int(data_df_total.shape[0]*0.8)+1:, 0:6]
testdat.to_json("testBTC1m.json",orient='values')
data_df.rename(columns={0:'date', 1: 'open', 2: 'high', 3: 'low', 4: 'close', 5:'volume'}, inplace=True)



#plt.plot(data_df.loc[:,"close"])

fivedaymov = np.divide(np.convolve(data_df.loc[:,"close"],np.ones(5),'valid'),5) #moving average of window 5

normalized = data_df.loc[:,"close"][4:]-fivedaymov
x = np.linspace(0.0, normalized.size, normalized.size, endpoint=False)
plt.plot(x,normalized)

fft_data = np.fft.fft(normalized)
N = fft_data.size
freq = np.fft.fftfreq(N,1)
magnitude = np.abs(fft_data)


#plt.plot(freq,magnitude)

#plt.xlim([-.0001, .0001])

X2=fft_data;#store the FFT results in another array
#detect noise (very small numbers (eps)) and ignore them
threshold = np.max(magnitude)/10000; #tolerance threshold
X2[magnitude<threshold] = 0; #maskout values that are below the threshold
phase = np.angle(X2)

max_mag = np.max(magnitude)
freq_max = freq[magnitude==max_mag]
phase_max = phase[magnitude==max_mag]


func = np.multiply(normalized,np.cos(2.0*np.pi*freq_max*x+phase_max))
plt.plot(x,func)

plt.xlim([0, 1000])

#use 80% of the data to train this fourier model.

#Start testing Sunday, August 1, 2021
