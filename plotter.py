"""
.. module:: plotter
   :platform: Unix, Windows
   :synopsis: A module for plotting financial data with various indicators.

.. moduleauthor:: ZyndramZM

"""

import pandas as pd
import talib as ta
import plotly.graph_objects as go
from plotly.subplots import make_subplots

SMA_ARG = 100
EMA_ARG = 100


# Main plotter class
class Plotter:
    """
    A class used to plot financial data with various indicators.

    ...

    Attributes
    ----------
    sma : bool
        a flag indicating whether to plot Simple Moving Average
    ema : bool
        a flag indicating whether to plot Exponential Moving Average
    rsi : bool
        a flag indicating whether to plot Relative Strength Index
    volume : bool
        a flag indicating whether to plot trading volume
    data : pd.DataFrame
        the financial data to be plotted
    plot_type : str
        the type of plot to be generated ("Liniowy", "Świecowy", "OHLC")
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the plotter object.

        Parameters
        ----------
            None
        """

        self.sma = False
        self.ema = False
        self.rsi = False

        self.volume = False

        self.data = None

        self.plot_type = "Linear"

    @property
    def ready(self):
        """
        Checks if the data is ready for plotting.

        Returns
        -------
        bool
            True if data is not None, False otherwise
        """

        return self.data is not None

    def load_data(self, data: pd.DataFrame):
        """
        Loads the financial data to be plotted.

        Parameters
        ----------
        data : pd.DataFrame
            The financial data to be plotted.

        Returns
        -------
        None
        """

        if 'Date' in data.columns:
            data.set_index('Date')
        self.data = data

    def setup(self,
              sma=False,
              ema=False,
              rsi=False,
              volume=False,
              plot_type="Linear"):
        """
        Sets up the plotter with the desired indicators and plot type.

        Parameters
        ----------
        sma : bool, optional
            Whether to plot Simple Moving Average (default is False)
        ema : bool, optional
            Whether to plot Exponential Moving Average (default is False)
        rsi : bool, optional
            Whether to plot Relative Strength Index (default is False)
        volume : bool, optional
            Whether to plot trading volume (default is False)
        plot_type : str, optional
            The type of plot to be generated ("Liniowy", "Świecowy", "OHLC") (default is "Liniowy")

        Returns
        -------
        None
        """

        self.sma = sma
        self.ema = ema
        self.rsi = rsi
        self.volume = volume
        self.plot_type = plot_type

    def generate(self):
        """
        Generates the plot with the loaded data and the set indicators. Raises an AttributeError if
        no data has been loaded.

        Raises
        ------
        AttributeError
            If no data has been loaded.

        Returns
        -------
        None
        """

        if self.data is None:
            raise AttributeError("Can't generate plot with no data.")

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
        if self.plot_type == "Linear":
            fig.add_trace(go.Scatter(x=df.index, y=df['Close'], name="Action value"),
                          row=1, col=1
                          )
        elif self.plot_type == "Candy":
            fig.add_trace(go.Candlestick(x=df.index,
                                         open=df['Open'],
                                         high=df['High'],
                                         low=df['Low'],
                                         close=df['Close'],
                                         name="Action value"),
                          row=1, col=1
                          )
        elif self.plot_type == 'OHLC':
            fig.add_trace(go.Ohlc(x=df.index,
                                  open=df['Open'],
                                  high=df['High'],
                                  low=df['Low'],
                                  close=df['Close'],
                                  name="Action value"),
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