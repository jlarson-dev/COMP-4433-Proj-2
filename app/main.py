from dash import Dash, html, dcc, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph')
])

app.run(debug=True)

