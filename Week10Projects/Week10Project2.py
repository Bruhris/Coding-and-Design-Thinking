from bokeh.plotting import figure, show 
from bokeh.io import output_notebook

import pandas as pd
df = pd.read_csv("Week10Projects/TSLA.csv")

dates = pd.to_datetime(df['date']).tolist() 
close = df['close'].tolist()
high = df['high'].tolist()
low = df['low'].tolist()
open = df['open'].tolist()

tsla = figure(title="Tesla Close Prices", x_axis_label="Date", y_axis_label="Closing Price", x_axis_type="datetime")
tsla.circle(x=dates, y=close, size = 3, color="#000000", legend_label='Close')
tsla.circle(x=dates, y=high, size = 3, color="#2785db", legend_label='High')
tsla.circle(x=dates, y=low, size = 3, color="#d83939", legend_label='Low')
tsla.circle(x=dates, y=open, size = 3, color="#1b8c1b", legend_label='Open')
show(tsla)
