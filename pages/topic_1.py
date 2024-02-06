import dash
from dash import html

import dash_bootstrap_components as dbc

from .side_bar import sidebar

dash.register_page(__name__, name="Topics")

topic_test = []
topic_tes2 = []
def layout():
    return dbc.Row(
        [dbc.Col(
            sidebar(), width=2),
        dbc.Col(html.Div("Topics Home Page"), width=10)]
    )














