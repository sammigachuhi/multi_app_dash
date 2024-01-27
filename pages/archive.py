import dash
from dash import html

dash.register_page(__name__,
                   path="/archive",
                   redirect_from=["/archive-2021", "/archive-2020"],
                   )

layout = html.Div([
    html.H1("This is our Archive page"),
    html.Div("This is our Archive page content.")
])

















