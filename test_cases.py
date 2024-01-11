from contextvars import copy_context

import plotly
from dash import html
from dash._callback_context import context_value
from dash._utils import AttributeDict

# Import the names of callback functions you want to test
from pink_morcel_visualizer import  update_graph

def test_update_graph_callback():
    output = update_graph('south')

    print('hello')
    print(output)
    print('hello')
    assert output !=0



