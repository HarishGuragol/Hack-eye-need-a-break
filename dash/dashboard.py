# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np

app = dash.Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

t = np.arange(0,100) # replace with times from db
y = np.random.rand(100) # replace with scores from db

df = pd.DataFrame({'t':t, 'y':y})


#fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
fig = px.line(df, x='t', y='y', title='attention score')

app.layout = html.Div(children=[
    html.H1(children='Dashboard'),

    html.Div(children='''
        Summary of attention scores from eye-tracking data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)