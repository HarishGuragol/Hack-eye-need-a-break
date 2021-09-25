# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import numpy as np

from db.utils.calc_scores import get_dash_data
THRESH=0.8

app = dash.Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

y, t = get_dash_data(1)
print(t)
min_t = min(t)
t = list(map(lambda x: (x-min_t)/60, t))
# t = np.arange(0,100) # replace with times from db
# y = np.random.rand(100) # replace with scores from db

df = pd.DataFrame({'t':t, 'y':y})

above_thresh = np.sum(np.array([1 for yy in df['y'] if yy >= THRESH]))
below_thresh = len(df['y']) - above_thresh

above_percent = above_thresh / (above_thresh + below_thresh) * 100
below_percent = 100 - above_percent

#fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
fig = px.line(df, x='t', y='y', labels={
                     "t": "time [ms]",
                     "y": "Attention score",
                 },)

fig2 = make_subplots(rows=1, cols=2, specs=[[{"type": "xy"}, {"type": "domain"}]])

fig2.add_trace(go.Histogram(x=df["y"]), row=1, col=1)
fig2.add_trace(go.Pie(values=[above_percent, below_percent]), row=1, col=2)

app.layout = html.Div(children=[
    html.H1(children='Dashboard'),

    html.Div(children='''
        Summary of attention scores from eye-tracking data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    html.Div(children='''
        Summary of attention scores from eye-tracking data.
    '''),

    dcc.Graph(
        id='example-graph2',
        figure=fig2
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)