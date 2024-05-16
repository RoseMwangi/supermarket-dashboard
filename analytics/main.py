#main.py

import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash import dcc, html
from pages import home, branchA, branchB, branchC

# Define the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the navbar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/", active="exact")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Branch A", href="/branch-A"),
                dbc.DropdownMenuItem("Branch B", href="/branch-B"),
                dbc.DropdownMenuItem("Branch C", href="/branch-C"),
            ],
            nav=True,
            in_navbar=True,
            label="Branches",
        ),
    ],
    brand="Welcome to Bidii supermarket sales",
    brand_href="/",
    color="primary",
    dark=True,
)

# Define the app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    dbc.Container(id='page-content', className='pt-4')
])

# Define callback to render page content based on URL pathname
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def render_page_content(pathname):
    if pathname == '/branch-A':
        return branchA.layout
    elif pathname == '/branch-B':
        return branchB.layout
    elif pathname == '/branch-C':
        return branchC.layout
    else:
        return home.layout

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
