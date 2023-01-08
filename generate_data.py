import yfinance
from plotter import Plotter

# Download data
GOOGLE_info = yfinance.Ticker("AAPL")
GOOGLE_info.history(period='3y').to_csv('./samples/apple_3y.csv')
# print(GOOGLE_info.history(period='max').index)

# Visualise data
p = Plotter()
p.load_data(GOOGLE_info.history(period='3y'))
p.setup(sma=True, ema=True, rsi=True, volume=True)
p.generate()
