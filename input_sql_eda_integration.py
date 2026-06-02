import sqlite3
import pandas as pd

# Connect to SQLite Database
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

# Create Sales Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER,
    product TEXT,
    category TEXT,
    amount INTEGER,
    city TEXT
)
""")

# Insert Sample Data
sales_data = [
    (1, "Laptop", "Electronics", 50000, "Hyderabad"),
    (2, "Mobile", "Electronics", 25000, "Vijayawada"),
    (3, "Chair", "Furniture", 5000, "Chennai"),
    (4, "Table", "Furniture", 8000, "Hyderabad"),
    (5, "Laptop", "Electronics", 55000, "Chennai"),
    (6, "Mobile", "Electronics", 27000, "Vijayawada"),
    (7, "Chair", "Furniture", 4500, "Hyderabad"),
    (8, "Table", "Furniture", 9000, "Chennai")
]

cursor.execute("DELETE FROM sales")
cursor.executemany(
    "INSERT INTO sales VALUES (?, ?, ?, ?, ?)",
    sales_data
)

conn.commit()

# SQL Queries
print("\n=== COMPLETE DATASET ===")
query = "SELECT * FROM sales"
df = pd.read_sql_query(query, conn)
print(df)

print("\n=== ELECTRONICS PRODUCTS ===")
electronics = pd.read_sql_query(
    "SELECT * FROM sales WHERE category='Electronics'",
    conn
)
print(electronics)

print("\n=== SORT BY SALES AMOUNT DESC ===")
sorted_sales = pd.read_sql_query(
    "SELECT * FROM sales ORDER BY amount DESC",
    conn
)
print(sorted_sales)

# EDA Analysis Using Pandas
print("\n=== DATA INFORMATION ===")
print(df.info())

print("\n=== SUMMARY STATISTICS ===")
print(df.describe())

print("\n=== TOTAL RECORDS ===")
print(len(df))

print("\n=== AVERAGE SALES ===")
print(df["amount"].mean())

print("\n=== HIGHEST SALE ===")
print(df["amount"].max())

print("\n=== LOWEST SALE ===")
print(df["amount"].min())

print("\n=== CATEGORY-WISE SALES ===")
print(df.groupby("category")["amount"].sum())

print("\n=== CATEGORY-WISE AVERAGE SALES ===")
print(df.groupby("category")["amount"].mean())

print("\n=== CITY-WISE SALES ===")
print(df.groupby("city")["amount"].sum())

# Close Connection
conn.close()
