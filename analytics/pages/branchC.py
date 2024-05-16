# branchC.py


import dash_bootstrap_components as dbc
from dash import dcc, html
import pandas as pd
import os

# Load data
sales = pd.read_csv(os.path.join(r'C:\Users\Dell\AppData\Local\Microsoft\WindowsApps\python\time_series\analytics', 'supermarket_sales.csv'))

# Convert 'Date' column to datetime
sales['Date'] = pd.to_datetime(sales['Date'])

# Filter data for Branch C
branch_C_sales = sales[sales['Branch'] == 'C'].copy()

# Group data by product line and gender, count the number of customers
gender_product_sales = branch_C_sales.groupby(['Product line', 'Gender']).size().reset_index(name='Count')

# Filter data for male and female counts separately
male_counts = gender_product_sales[gender_product_sales['Gender'] == 'Male']
female_counts = gender_product_sales[gender_product_sales['Gender'] == 'Female']

# Create traces for male and female counts
trace_male = {
    'x': male_counts['Product line'],
    'y': male_counts['Count'],
    'name': 'Male',
    'type': 'bar'
}

trace_female = {
    'x': female_counts['Product line'],
    'y': female_counts['Count'],
    'name': 'Female',
    'type': 'bar'
}
# Combine traces into a list
dataC = [trace_male, trace_female]

# Convert 'Time' column to datetime
branch_C_sales['Time'] = pd.to_datetime(branch_C_sales['Time'], format='%H:%M')

# Extract hour from 'Time' column
branch_C_sales['Hour'] = branch_C_sales['Time'].dt.floor('h').dt.time

# Group data by hour and count the number of transactions
hourly_sales = branch_C_sales.groupby('Hour').size().reset_index(name='Customer Served')

# Calculate total sales for each product line in Branch C
product_sales = branch_C_sales.groupby('Product line')['Total'].sum().reset_index()

# Aggregate ratings on a weekly basis
branch_C_sales_weekly = branch_C_sales.resample('W-Mon', on='Date')['Rating'].mean().reset_index()

# Sort data by date
branch_C_sales_weekly = branch_C_sales_weekly.sort_values(by='Date')

# Define graph layout style
graph_style = {"margin": "auto", 'marginLeft': '100px'}

layout = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(
                        id="Branch C sales across products",
                        figure={
                            'data': [
                                {
                                    'x': product_sales['Product line'],
                                    'y': product_sales['Total'],
                                    'type': 'bar',
                                    'label': 'Branch'
                                },
                            ],
                            'layout': {
                                'title': 'Branch C sales across products',
                                'xaxis': {'title': 'Product line'},
                                'yaxis': {'title': 'total sales'},
                                'height': 500,
                                'width': 500,
                                # 'style': graph_style
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
                        id='Customer Satisfaction Ratings Over Time in Branch C',
                        figure={
                            'data': [
                                {
                                    'x': branch_C_sales_weekly['Date'],
                                    'y': branch_C_sales_weekly['Rating'],
                                    'type': 'line',
                                    'name': 'Customer Ratings',
                                    'mode': 'lines+markers'
                                },
                            ],
                            'layout': {
                                'title': 'Customer Satisfaction Ratings Over Time in Branch C',
                                'xaxis': {'title': 'Date'},
                                'yaxis': {'title': 'Rating'},
                                'height': 500,
                                'width': 500,
                            }
                        }
                    )
                ])
            ], className="mb-4")
        ])
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(
                        id="Branch C sales throughout the day",
                        figure={
                            'data': [
                                {
                                    'x': hourly_sales['Hour'],
                                    'y': hourly_sales['Customer Served'],
                                    'type': 'line',
                                    # 'label': 'Branch'
                                },
                            ],
                            'layout': {
                                'title': 'Branch C sales across the day',
                                'xaxis': {'title': 'hour'},
                                'yaxis': {'title': 'sales'},
                                'height': 400,
                                'width': 500,
                                # 'style': graph_style
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
                        id="Branch C gender distribution sales across products lines",
                        figure={
                            'data': dataC,
                            'layout': {
                                'title': 'Branch C sales across products',
                                'xaxis': {'title': 'Product line'},
                                'yaxis': {'title': 'count'},
                                'barmode': 'group',
                                'height': 400,
                                'width': 500,
                                # 'style': graph_style
                            }
                        }
                    )
                ])
            ], className="mb-4")
        ])
    ])
])

