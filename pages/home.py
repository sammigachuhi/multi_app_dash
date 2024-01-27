import dash
from dash import html

dash.register_page(__name__, path="/",
                   title="Home Page",
                   description="Custom Home Page Description",
                   image_url="https://images.unsplash.com/photo-1622015663084-307d19eabbbf?q=80&w=1942&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                   )

layout = html.Div([
    html.H1("This is our Home page."),
    html.Div("This is our Home page content.")
])



















