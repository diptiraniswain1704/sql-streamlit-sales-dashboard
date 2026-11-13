
# Sales Analytics Dashboard

An interactive sales analytics web application built using Python, SQL, SQLite, and Streamlit. The dashboard helps business users monitor revenue, analyse product performance, compare regional sales, and explore monthly sales trends.

## Features

- Interactive sales dashboard
- Total revenue, orders, units sold, and customer KPIs
- Monthly revenue trend visualization
- Product-wise revenue analysis
- Region-wise sales distribution
- Interactive filters for date, product, category, and region
- Detailed sales records
- CSV export functionality

## Tech Stack

- Python
- SQLite
- SQL
- Pandas
- Streamlit
- Plotly

## Project Structure

```text
SQL-Streamlit-Dashboard/
│
├── app.py
├── database.py
├── queries.py
├── test_queries.py
├── sales.db
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/diptiraniswain1704/sql-streamlit-sales-dashboard.git
```

2. Navigate to the project folder:

```bash
cd sql-streamlit-sales-dashboard
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Generate the sample database:

```bash
python database.py
```

5. Launch the application:

```bash
python -m streamlit run app.py
```

## Database

The project uses SQLite to store sales records.

SQL queries are used for revenue aggregation, product analysis, regional analysis, and customer statistics.

The application uses synthetic sales data for demonstration purposes.

## Future Improvements

- SQL-based dynamic filtering
- Advanced business intelligence metrics
- LLM-powered natural language SQL querying
- Cloud deployment

## Author

GitHub: https://github.com/diptiraniswain1704
## Live Demo

[View Sales Analytics Dashboard](https://business-sales-insights.streamlit.app)