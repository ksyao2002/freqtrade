To backtest the algorithm, make sure Freqtrade is setup following instructions. Then, run 

```freqtrade backtesting --strategy FourierStrategy --timerange=-20211215```

The files in data/ are downloaded BTC/USDT data. There is also a file called Analyze.py there that contains the Fourier analysis code for generating the figures and determining the dominant cos frequency. Our Fourier strategy is implemented under strategies/FourierStrategy.py
