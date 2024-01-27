import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__,
                   path="/analytics-dashboard",
                   title="Our Analytics Dashboard",
                   name="See Analytics Dashboard")

layout = html.Div([
    html.H1("This is our Analytics page"),
    html.Div([
        "Select a city: ",
        dcc.RadioItems(
            options=["New York City", "Montreal", "San Fransisco"],
            value="Montreal",
            id="analytics-input"
        )
    ]),
    html.Br(),
    html.Div(id="analytics-output")
])

@callback(
    Output("analytics-output", "children"),
    Input("analytics-input", "value")
)
def update_city_selected(input_value):
    return f"You selected: {input_value}"

























