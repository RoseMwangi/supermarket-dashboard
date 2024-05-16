# Supermarket Sales Dashboard

** This project is a data analytics dashboard for visualizing supermarket sales data. The dashboard is built using Dash and Bootstrap and provides insights into sales performance across different branches, customer satisfaction, and product line performances.

# Project Structure

```analytics/
    ├── main.py
    ├── supermarket_sales.csv
    ├── pages/
        ├── home.py
        ├── branchA.py
        ├── branchB.py
        ├── branchC.py
        ```

. main.py: The main application file that sets up the Dash app and the navigation bar.
. supermarket_sales.csv: The dataset containing supermarket sales data.
. pages/: Contains separate scripts for each page of the dashboard:
. home.py: Home page with an overview of sales data.
. branchA.py: Detailed analytics for Branch A.
. branchB.py: Detailed analytics for Branch B.
. branchC.py: Detailed analytics for Branch C.

# Features

. Navigation Bar: Simple and intuitive navigation between home and branch-specific pages.
. Data Visualization: Bar charts, line charts, scatter plots, and pie charts to display sales data, customer ratings, and product line . . performances.
. Responsive Design: Built with Bootstrap to ensure a responsive and user-friendly interface.

# Installation

. Clone the repository:
    git clone https://github.com/RoseMwangi/supermarket-sales-dashboard.git
    cd supermarket-sales-dashboard/analytics
. Create a virtual environment:
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

. Install the required packages:
    pip install -r requirements.txt
. Add the requirements.txt file with the necessary dependencies:
    dash
    dash-bootstrap-components
    pandas

# Usage
  python main.py

# Open your web browser and navigate to http://127.0.0.1:8080 to view the dashboard.

# Data
The dataset supermarket_sales.csv contains the following columns:

Invoice ID: Unique identifier for each invoice.
Branch: Branch identifier (A, B, C).
City: City where the branch is located.
Customer type: Type of customer (Member or Normal).
Gender: Gender of the customer.
Product line: Category of the product purchased.
Unit price: Price per unit of the product.
Quantity: Quantity of products purchased.
Tax 5%: Tax applied on the total price.
Total: Total price including tax.
Date: Date of purchase.
Time: Time of purchase.
Payment: Payment method used.
cogs: Cost of goods sold.
gross margin percentage: Gross margin percentage.
gross income: Gross income.
Rating: Customer rating.

# Screenshots\video
  https://github.com/RoseMwangi/supermarket-dashboard/assets/25637181/35d310e2-0daa-4af9-a1f5-b5c23925c150

# Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

# License
This project is licensed under the MIT License. 


