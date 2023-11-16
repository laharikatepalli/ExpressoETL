import pandas as pd
from sqlalchemy import create_engine
import os

# MySQL database connection details
DB_USER = 'root'
DB_PASSWORD = 'your_Password'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'coffee_shop'

# Create a MySQL connection
engine = create_engine(f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Extract Data
tables = ['customer', 'Dates', 'generations', 'pastry_inventory', 'product', 'sales_targets', 'sales_outlet', 'staff', '201904_sales_reciepts']

dfs = {}  # Dictionary to store DataFrames for each table
for table in tables:
    table_name = table.replace(' ', '_').lower()
    file_path = os.path.join('C:/Users/Lahari/Downloads/dataset/', f'{table_name}.csv')
    print(f"Reading file: {file_path}")
    dfs[table_name] = pd.read_csv(file_path)

# Transform and Load Data
for table_name, df in dfs.items():
    try:
        print(f"Attempting to write {table_name} table to MySQL...")
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"{table_name} table successfully written to MySQL.")
    except Exception as e:
        print(f"Error writing {table_name} table to MySQL: {e}")

# Close the database connection
engine.dispose()
