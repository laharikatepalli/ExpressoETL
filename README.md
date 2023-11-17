# ExpressoETL

## Overview

This project focuses on extracting, transforming, and loading data from a MySQL database for a coffee shop. The ETL process involves reading data from multiple tables, performing joins, aggregations, and filtering operations using PySpark, and then loading the results into DataFrames.Additionally, a PowerBI dashboard named ExpressoETL has been created to visualize the extracted data.

## Project Structure

- **`etl_pipeline.py`**: The main PySpark script for the ETL process.
- **`requirements.txt`**: List of Python dependencies for the project.
- **`README.md`**: Documentation providing an overview, usage instructions, and any additional
                   information.
  **`Coffee_shop_Dashboard.pbix`**: PowerBI dashboard file.


## Prerequisites

Before running the ETL script, ensure the following:

1. **Kaggle Dataset:**
   - Download the Coffee Shop Sample Data from Kaggle using the following link: [Coffee Shop Sample Data](https://www.kaggle.com/ylchang/coffee-shop-sample-data-1113?select=customer.csv).
   - Place the downloaded dataset in the appropriate directory (`data/` or as specified in the script) before running the ETL script.

2. **PySpark Environment**: Set up a PySpark environment. You can install PySpark using 
     `pip install pyspark`.

3. **MySQL Connector/J JAR File**: Download and set the path for the MySQL Connector/J JAR file. 
     This file is required for connecting PySpark to MySQL. You can download it from the [official MySQL website](https://dev.mysql.com/downloads/connector/j/).

4. **MySQL Database**: Ensure that you have a MySQL database with the required tables and data. 
     Refer to the schema provided in the script (`sales_schema`, `customer_schema`, etc.).

5. **PowerBI Desktop**: Install PowerBI Desktop to view and interact with the ExpressoETL dashboard.

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

   - Open `etl_pipeline.py` and set the correct path for the MySQL Connector/J JAR file (`mysql_jar_path`).
   - Update MySQL connection properties (`DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `DB_NAME`).

4. **Run the ETL Script:**

   ```bash
   python etl_script.py
   ```

5. **View Results:**

   The script will perform various ETL operations, including joining tables, aggregating data, filtering, and computing averages. Results will be displayed for each DataFrame.

6. **Explore PowerBI Dashboard**:

   Open Coffee_shop_Dashboard.pbix in PowerBI Desktop to explore the visualizations and insights derived from the ETL process.

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