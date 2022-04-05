from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

import gunicorn
from whitenoise import WhiteNoise

app = Dash(__name__)
server = app.server
server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/')

df = pd.DataFrame({
    "Fruit":
        ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount":
        [4, 1, 2, 2, 4, 5],
    "City":
        ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=False)