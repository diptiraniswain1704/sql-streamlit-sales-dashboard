
import sqlite3
import random
from datetime import datetime, timedelta

# Connect to SQLite database
conn = sqlite3.connect("sales.db") #creates database
cursor = conn.cursor()

# Create sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    order_id INTEGER PRIMARY KEY,
    order_date DATE,
    product TEXT,
    category TEXT,
    region TEXT,
    quantity INTEGER,
    unit_price REAL,
    customer TEXT
)
""")

# Sample data
products = {
    "Laptop": ("Electronics", 55000),
    "Mobile": ("Electronics", 25000),
    "Headphones": ("Accessories", 2000),
    "Keyboard": ("Accessories", 1500),
    "Monitor": ("Electronics", 12000),
    "Chair": ("Furniture", 8000),
    "Table": ("Furniture", 10000),
    "Mouse": ("Accessories", 800)
}

regions = ["North", "South", "East", "West"]
customers = [f"Customer {i}" for i in range(1, 51)]

# Generate 500 sales records
sales_data = []

start_date = datetime(2026, 1, 1)

for i in range(1, 501):

    product = random.choice(list(products.keys()))
    category, price = products[product]

    order_date = start_date + timedelta(
        days=random.randint(0, 300)
    )

    region = random.choice(regions)
    quantity = random.randint(1, 5)
    customer = random.choice(customers)

    sales_data.append((
        i,
        order_date.strftime("%Y-%m-%d"),
        product,
        category,
        region,
        quantity,
        price,
        customer
    ))

# Insert records into database
cursor.executemany("""
INSERT OR IGNORE INTO sales
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", sales_data)

conn.commit()  #saves records permanently.

print("Database created successfully!")
print("500 sales records generated.")

# Check total records
cursor.execute("SELECT COUNT(*) FROM sales")
print("Total records:", cursor.fetchone()[0])

conn.close()
