
import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# DATABASE CONNECTION
# -----------------------------

def load_data():
    conn = sqlite3.connect("sales.db")
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    conn.close()

    df["order_date"] = pd.to_datetime(df["order_date"])
    df["revenue"] = df["quantity"] * df["unit_price"]

    return df


df = load_data()

# -----------------------------
# DASHBOARD TITLE
# -----------------------------

st.title("📊 Sales Analytics Dashboard")

st.markdown(
    "An interactive dashboard for analysing sales "
    "performance using Python, SQL and Streamlit."
)

st.divider()

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------

st.sidebar.header("Dashboard Filters")

regions = st.sidebar.multiselect(
    "Select Region",
    options=sorted(df["region"].unique()),
    default=sorted(df["region"].unique())
)

categories = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df["category"].unique()),
    default=sorted(df["category"].unique())
)

products = st.sidebar.multiselect(
    "Select Product",
    options=sorted(df["product"].unique()),
    default=sorted(df["product"].unique())
)

min_date = df["order_date"].min().date()
max_date = df["order_date"].max().date()

date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# -----------------------------
# APPLY FILTERS
# -----------------------------

filtered_df = df[
    (df["region"].isin(regions)) &
    (df["category"].isin(categories)) &
    (df["product"].isin(products))
].copy()

if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
    start_date, end_date = date_range

    filtered_df = filtered_df[
        (filtered_df["order_date"].dt.date >= start_date) &
        (filtered_df["order_date"].dt.date <= end_date)
    ]
else:
    filtered_df = filtered_df.iloc[0:0]

# -----------------------------
# KEY PERFORMANCE INDICATORS
# -----------------------------

total_revenue = filtered_df["revenue"].sum()
total_orders = len(filtered_df)
total_quantity = filtered_df["quantity"].sum()
unique_customers = filtered_df["customer"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Revenue",
    f"₹{total_revenue/10000000:.2f} Cr"
)

col2.metric(
    "Total Orders",
    f"{total_orders:,}"
)

col3.metric(
    "Units Sold",
    f"{total_quantity:,}"
)

col4.metric(
    "Unique Customers",
    f"{unique_customers:,}"
)

st.divider()

if filtered_df.empty:
    st.warning("No sales records found for the selected filters.")
    st.stop()

# -----------------------------
# MONTHLY REVENUE CHART
# -----------------------------

st.subheader("Monthly Revenue Trend")

monthly_sales = (
    filtered_df.groupby(
        filtered_df["order_date"].dt.to_period("M")
    )["revenue"]
    .sum()
    .reset_index()
)

monthly_sales["month"] = monthly_sales["order_date"].astype(str)

fig1 = px.line(
    monthly_sales,
    x="month",
    y="revenue",
    markers=True,
    title="Revenue Over Time"
)

st.plotly_chart(fig1, use_container_width=True)

# -----------------------------
# PRODUCT AND REGION ANALYSIS
# -----------------------------

col1, col2 = st.columns(2)

with col1:
    st.subheader("Revenue by Product")

    product_sales = (
        filtered_df.groupby("product")["revenue"]
        .sum()
        .reset_index()
        .sort_values("revenue", ascending=False)
    )

    fig2 = px.bar(
        product_sales,
        x="product",
        y="revenue",
        title="Product Performance"
    )

    st.plotly_chart(fig2, use_container_width=True)

with col2:
    st.subheader("Revenue by Region")

    region_sales = (
        filtered_df.groupby("region")["revenue"]
        .sum()
        .reset_index()
    )

    fig3 = px.pie(
        region_sales,
        names="region",
        values="revenue",
        title="Regional Revenue Distribution"
    )

    st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# SALES DATA TABLE
# -----------------------------

st.divider()

st.subheader("Detailed Sales Records")

st.dataframe(
    filtered_df.sort_values("order_date", ascending=False),
    use_container_width=True,
    hide_index=True
)

# -----------------------------
# DOWNLOAD DATA
# -----------------------------

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Sales Data",
    data=csv,
    file_name="sales_data.csv",
    mime="text/csv"
)
st.success("Dashboard loaded successfully!")
