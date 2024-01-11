from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('pink_morcel_data.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Pink Morcel Sales', style={'textAlign':'center'}),
    dcc.RadioItems(df.region.unique(), 'north', id='radio-selection'),
    dcc.Graph(id='graph-content' )
])

@callback(
    Output('graph-content', 'figure'),
    Input('radio-selection', 'value')
)
def update_graph(value):
    dff = df[df.region==value]
    lineGraph =  px.line(dff, x='date', y='sales($)')
    # print(type(lineGraph))
    return lineGraph

if __name__ == '__main__':
    app.run(debug=True)
