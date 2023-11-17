# ExpressoETL

## Overview

This project focuses on extracting, transforming, and loading data from a MySQL database for a coffee shop. The ETL process involves reading data from multiple tables, performing joins, aggregations, and filtering operations using PySpark, and then loading the results into DataFrames.

## Project Structure

- **`etl_script.py`**: The main PySpark script for the ETL process.
- **`requirements.txt`**: List of Python dependencies for the project.
- **`README.md`**: Documentation providing an overview, usage instructions, and any additional information.

## Prerequisites

Before running the ETL script, ensure the following:

1. **PySpark Environment**: Set up a PySpark environment. You can install PySpark using `pip install pyspark`.

2. **MySQL Connector/J JAR File**: Download and set the path for the MySQL Connector/J JAR file. This file is required for connecting PySpark to MySQL. You can download it from the [official MySQL website](https://dev.mysql.com/downloads/connector/j/).

3. **MySQL Database**: Ensure that you have a MySQL database with the required tables and data. Refer to the schema provided in the script (`sales_schema`, `customer_schema`, etc.).

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/coffee-shop-etl.git
   cd coffee-shop-etl
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Edit Configuration:**

   - Open `etl_script.py` and set the correct path for the MySQL Connector/J JAR file (`mysql_jar_path`).
   - Update MySQL connection properties (`DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `DB_NAME`).

4. **Run the ETL Script:**

   ```bash
   python etl_script.py
   ```

5. **View Results:**

   The script will perform various ETL operations, including joining tables, aggregating data, filtering, and computing averages. Results will be displayed for each DataFrame.

## Additional Information

- **Tables and Schema:** Check the provided MySQL schema and ensure that your actual database matches the expected structure.

- **Sample Data:** The provided MySQL tables include sample data. Replace it with your actual coffee shop data.

- **SparkSession Configuration:** Customize the SparkSession configuration in the script based on your environment and requirements.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and enhancements are welcome!

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize this README based on your project's specific details and requirements.