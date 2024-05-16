# home.py

from dash import html, dcc
import pandas as pd
import os
import dash_bootstrap_components as dbc

# Define colors for each branch
branch_colors = {
    'A': 'green',
    'B': 'teal',
    'C': 'purple'
}

# Load data
sales = pd.read_csv(os.path.join(r'C:\Users\Dell\AppData\Local\Microsoft\WindowsApps\python\time_series\analytics', 'supermarket_sales.csv'))

# Define graph layout style
graph_style = {"margin": "auto"}

# Filter data for customer ratings and branches
customer_ratings = sales[['Branch', 'Rating']]

# Calculate mean rating for each branch
mean_ratings = customer_ratings.groupby('Branch')['Rating'].mean().reset_index()

layout = html.Div(children=[

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(
                        id="Sales graph",
                        figure={
                            'data': [
                                {
                                    'x': sales['Branch'],
                                    'y': sales['Total'],
                                    'type': 'bar',

                                    'label': 'Branch',
                                    'marker': {'color': [branch_colors[Branch] for Branch in sales['Branch']]}
                                },
                            ],
                            'layout': {
                                'title': 'Sales across all branches',
                                'xaxis': {'title': 'Branch'},
                                'yaxis': {'title': 'Sales'},
                                'height': 400,
                                'width': 500,
                            }
                        }
                    )
                ])
            ], className="mb-4")
        ]),

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(
                        id="Overall Branch satisfaction",
                        figure={
                            'data': [
                                {
                                    'x': mean_ratings['Branch'],
                                    'y': mean_ratings['Rating'],
                                    'type': 'scatter',
                                    'label': 'Branch',
                                    'marker': {'color': [branch_colors[Branch] for Branch in mean_ratings['Branch']]}
                                },
                            ],
                            'layout': {
                                'title': 'Customer satisfaction across all branches',
                                'xaxis': {'title': 'Branch'},
                                'yaxis': {'title': 'Customer Rating'},
                                'height': 400,
                                'width': 500,
                            }
                        }
                    )
                ])
            ], className="mb-4")
        ])
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(
                        id="product line sales",
                        figure={
                            'data': [
                                {
                                    'labels': sales['Product line'],
                                    'values': sales['Total'],
                                    'type': 'pie',
                                    'name': 'Product line sales'
                                },
                            ],
                            'layout': {
                                'title': 'Sales among product lines',
                                'height': 350
                            }
                        }
                    )
                ])
            ], className="mb-4")
        ], width=4),

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(
                        id="preferred payment option",
                        figure={
                            'data': [
                                {
                                    'labels': sales['Payment'],
                                    'values': sales['Total'],
                                    'type': 'pie',
                                    'name': 'Preferred payment option'
                                },
                            ],
                            'layout': {
                                'title': 'Preferred payment options',
                                'height': 350
                            }
                        }
                    )
                ])
            ], className="mb-4")
        ], width=4),

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(
                        id="General product lines performances",
                        figure={
                            'data': [
                                {
                                    'x': sales['Product line'],
                                    'y': sales['Total'],
                                    'type': 'bar',
                                    'label': 'product line',
                                },
                            ],
                            'layout': {
                                'title': 'product lines performances',
                                'xaxis': {'title': 'Product line'},
                                'yaxis': {'title': 'Total'},
                                'height': 350
                            }
                        }
                    )
                ])
            ], className="mb-4")
        ], width=4)
    ])

])
