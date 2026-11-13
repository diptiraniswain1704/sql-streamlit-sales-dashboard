
import sqlite3
import pandas as pd

# Connect to database
def get_connection():
    return sqlite3.connect("sales.db")


# 1. Get all sales records
def get_all_sales():
    conn = get_connection()

    query = "SELECT * FROM sales"

    df = pd.read_sql_query(query, conn)
    conn.close()

    return df


# 2. Calculate total revenue
def get_total_revenue():
    conn = get_connection()

    query = """
    SELECT SUM(quantity * unit_price)
    AS total_revenue
    FROM sales
    """

    result = pd.read_sql_query(query, conn)
    conn.close()

    return result.iloc[0, 0]


# 3. Calculate total orders
def get_total_orders():
    conn = get_connection()

    query = """
    SELECT COUNT(*) AS total_orders
    FROM sales
    """

    result = pd.read_sql_query(query, conn)
    conn.close()

    return result.iloc[0, 0]


# 4. Find top-selling products by revenue
def get_top_products():
    conn = get_connection()

    query = """
    SELECT product,
           SUM(quantity * unit_price) AS revenue
    FROM sales
    GROUP BY product
    ORDER BY revenue DESC
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    return df


# 5. Calculate regional revenue
def get_region_sales():
    conn = get_connection()

    query = """
    SELECT region,
           SUM(quantity * unit_price) AS revenue
    FROM sales
    GROUP BY region
    ORDER BY revenue DESC
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    return df


# 6. Calculate monthly revenue
def get_monthly_sales():
    conn = get_connection()

    query = """
    SELECT strftime('%Y-%m', order_date) AS month,
           SUM(quantity * unit_price) AS revenue
    FROM sales
    GROUP BY month
    ORDER BY month
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    return df


# 7. Count unique customers
def get_unique_customers():
    conn = get_connection()

    query = """
    SELECT COUNT(DISTINCT customer)
    AS unique_customers
    FROM sales
    """

    result = pd.read_sql_query(query, conn)
    conn.close()

    return result.iloc[0, 0]
