
from queries import *

print("\n===== SALES DASHBOARD TEST =====")

print("Total Revenue:", get_total_revenue())

print("Total Orders:", get_total_orders())

print("\nTop Products:")
print(get_top_products())

print("\nRegional Sales:")
print(get_region_sales())

print("\nMonthly Sales:")
print(get_monthly_sales())

print("\nUnique Customers:", get_unique_customers())

print("\nAll Sales Records:")
print(get_all_sales().head())
