# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import os
import time

import dash
from dash.dependencies import Output,Input
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import numpy as np

import plotly.io as pio

pio.templates.default = "seaborn"

from db.utils.calc_scores import get_dash_data, get_sensitivity_value
THRESH=0.1

app = dash.Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

user_id = 1
while True:
    try:
        sensitivity = get_sensitivity_value(user_id)
        y, t = get_dash_data(user_id)
        print(t)
        min_t = min(t)
        break
    except:
        pass
    print("Await a data...")
    time.sleep(5)

t = list(map(lambda x: (x-min_t)/1000, t))
# t = np.arange(0,100) # replace with times from db
# y = np.random.rand(100) # replace with scores from db

df = pd.DataFrame({'t':t, 'y':y})

above_thresh = np.sum(np.array([1 for yy in df['y'] if yy >= sensitivity]))
below_thresh = len(df['y']) - above_thresh

above_percent = above_thresh / (above_thresh + below_thresh) * 100
below_percent = 100 - above_percent

#fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
fig = px.line(df, x='t', y='y', labels={
                     "t": "time [s]",
                     "y": "Distraction score",
                 },)

fig2 = make_subplots(rows=1, cols=2, specs=[[{"type": "xy"}, {"type": "domain"}]])

fig2.add_trace(go.Histogram(x=df["y"]), row=1, col=1)
fig2.add_trace(go.Pie(values=[above_percent, below_percent], labels=['distracted', 'attentive'], scalegroup='one'), row=1, col=2)

fig2.update_xaxes(title_text="score", row=1, col=1)
fig2.update_yaxes(title_text="frequency", row=1, col=1)


app.layout = html.Div(children=[
    html.H1(children='Dashboard'),

    html.Div(children='''
        Summary of attention scores from eye-tracking data.
    '''),

    dcc.Graph(
        id='example-graph',
        animate=True
    ),

    html.Div(children='''
    '''),

    dcc.Graph(
        id='example-graph2',
        figure=fig2
    ),

    dcc.Interval(
            id='interval-component',
            interval=1*1000
        )
])

@app.callback(Output('example-graph', 'figure'), [Input('interval-component', 'interval')])
def update_example_graph(a):
    sensitivity = get_sensitivity_value(user_id)
    y, t = get_dash_data(user_id)
    print(t)
    min_t = min(t)
    t = list(map(lambda x: (x - min_t) / 1000, t))

    df = pd.DataFrame({'t': t, 'y': y})
    fig = px.line(df, x='t', y='y', labels={
        "t": "time [s]",
        "y": "Distraction score",
    })
    return fig

if __name__ == '__main__':
    if os.environ.get('PROD', False):
        print("Production dashboard is running!")
        app.run_server("0.0.0.0", 80, debug=True)
    else:
        print("Dev dashboard is running!")
        app.run_server(debug=True)