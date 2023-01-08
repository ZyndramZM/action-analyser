import numpy as np
import pandas as pd
import talib as ta
import plotly.graph_objects as go
from plotly.subplots import make_subplots

SMA_ARG = 100
EMA_ARG = 100


# Main plotter class
class Plotter:
    def __init__(self):
        self.sma = False
        self.ema = False
        self.rsi = False

        self.volume = False

        self.data = None

    def load_data(self, data: pd.DataFrame):
        self.data = data

    def setup(self,
              sma=False,
              ema=False,
              rsi=False,
              volume=False):
        self.sma = sma
        self.ema = ema
        self.rsi = rsi
        self.volume = volume

    def generate(self):
        if self.data is None:
            raise DataError("Can't generate plot with no data.")

        rows_heights = [1]
        if self.volume:
            rows_heights = [0.8, 0.2]
        if self.rsi:
            rows_heights[0] -= 0.2
            rows_heights.append(0.2)

        fig = make_subplots(rows=len(rows_heights), cols=1, shared_xaxes=True,
                            vertical_spacing=0.03,
                            row_heights=rows_heights)

        df = self.data

        # Main plot
        fig.add_trace(go.Scatter(x=df.index, y=df['Close'], name="Analiza akcji"),
                      row=1, col=1
                      )

        if self.sma:
            df['SMA'] = ta.SMA(df['Close'], SMA_ARG)
            fig.add_trace(go.Scatter(x=df.index, y=df['SMA'], name='SMA'), row=1, col=1)

        if self.ema:
            df['EMA'] = ta.EMA(df['Close'], EMA_ARG)
            fig.add_trace(go.Scatter(x=df.index, y=df['EMA'], name='EMA'), row=1, col=1)

        if self.rsi:
            df['RSI'] = ta.RSI(df['Close'])
            fig.add_trace(go.Scatter(x=df.index, y=df['RSI'], name='RSI'), row=2, col=1)
            fig.add_hline(y=30, row=2, col=1, line_dash='dash', line_color='green')
            fig.add_hline(y=70, row=2, col=1, line_dash='dash', line_color='red')

        # Bar trace for volumes on 2nd row without legend
        if self.volume:
            fig.add_trace(go.Bar(x=df.index, y=df['Volume'], showlegend=False, name='Wolumin', marker_color='red'),
                          row=len(rows_heights), col=1)

        # Do not show OHLC's rangeslider plot
        fig.update(layout_xaxis_rangeslider_visible=False)
        fig.show()


# TESTING
if __name__ == '__main__':
    import yfinance
    from pandas.errors import DataError

    GOOGLE_info = yfinance.Ticker("AAPL")
    # GOOGLE_info.history(period='1y').to_csv(r'Q:\Dokumenty\!Studia\!Projects\action-analyser\samples\apple_1y.csv')
    # print(GOOGLE_info.history(period='max').index)

    p = Plotter()
    p.load_data(GOOGLE_info.history(period='1y'))
    p.setup(sma=True, ema=True, rsi=True, volume=True)
    p.generate()
