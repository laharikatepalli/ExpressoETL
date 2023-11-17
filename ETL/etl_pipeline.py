from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Set the MySQL Connector/J JAR file path
mysql_jar_path = "C:/Program Files/MySQL/mysql-connector-j-8.2.0/mysql-connector-j-8.2.0.jar"

# SparkSession configuration
spark = SparkSession.builder \
    .appName("YourAppName") \
    .config("spark.jars", mysql_jar_path) \
    .getOrCreate()

# Define your MySQL connection properties
DB_USER = 'root'
DB_PASSWORD = 'Your_Password'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'coffee_shop'

# Define your sales schema (replace this with your actual schema)
sales_schema = ...

# Define your JDBC URL
jdbc_url = f"jdbc:mysql://{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Read data from MySQL
sales_data = spark.read \
    .format("jdbc") \
    .option("url", jdbc_url) \
    .option("dbtable", "201904_sales_reciepts") \
    .option("user", DB_USER) \
    .option("password", DB_PASSWORD) \
    .load(schema=sales_schema)

# Perform your ETL operations here

# ETL Operation 2: Joining with the 'customer' table
customer_schema = StructType([
    StructField("customer_id", IntegerType(), True),
    StructField("home_store", IntegerType(), True),
    StructField("customer_first_name", StringType(), True),
    StructField("customer_email", StringType(), True),
    StructField("customer_since", StringType(), True),
    StructField("loyalty_card_number", StringType(), True),
    StructField("birthdate", StringType(), True),
    StructField("gender", StringType(), True),
    StructField("birth_year", IntegerType(), True),
])

customer_data = spark.read \
    .format("jdbc") \
    .option("url", jdbc_url) \
    .option("dbtable", "customer") \
    .option("user", DB_USER) \
    .option("password", DB_PASSWORD) \
    .load(schema=customer_schema)

# Perform the join operation
joined_data = sales_data.join(customer_data, sales_data["customer_id"] == customer_data["customer_id"], "left")

# Show the resulting DataFrame
joined_data.show()

# ETL Operation 3: Aggregating sales data by product
product_sales_data = sales_data.groupBy("product_id").agg({"quantity": "sum", "line_item_amount": "sum"})

# Show the resulting DataFrame
product_sales_data.show()

# ETL Operation 4: Filtering data based on a condition
filtered_data_2 = sales_data.filter((sales_data["quantity"] > 1) & (sales_data["unit_price"] > 3.0))

# Show the resulting DataFrame
filtered_data_2.show()

# ETL Operation 5: Computing average sales amount per transaction
avg_sales_amount = sales_data.groupBy("transaction_id").agg({"line_item_amount": "avg"})

# Show the resulting DataFrame
avg_sales_amount.show()

# Stop the SparkSession
spark.stop()
