import psycopg2
import pymysql
import pandas as pd

# Redshift connection parameters
redshift_params = {
    'dbname': 'your_redshift_dbname',
    'user': 'username',
    'password': 'password',
    'host': 'yahoo-test-endpoint-lpi9eomto1hw2ctt1b00.963763073573.us-east-1.redshift-serverless.amazonaws.com',
    'port': 5439
}

# RDS connection parameters
rds_params = {
    'host': 'your_rds_host',
    'user': 'username',
    'password': 'password',
    'db': 'yahoo-finances',
    'port': 3306
}

def fetch_from_redshift():
    try:
        redshift_conn = psycopg2.connect(**redshift_params)
        print("Connected to Redshift")
        query = "SELECT * FROM your_table"
        df = pd.read_sql(query, redshift_conn)
        print("Data fetched from Redshift")
        redshift_conn.close()
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None

def insert_into_rds(df):
    try:
        rds_conn = pymysql.connect(**rds_params)
        print("Connected to RDS")
        insert_query = """
        INSERT INTO your_table (column1, column2, column3, ...)
        VALUES (%s, %s, %s, ...)
        """
        data_tuples = [tuple(x) for x in df.to_numpy()]
        with rds_conn.cursor() as cursor:
            cursor.executemany(insert_query, data_tuples)
            rds_conn.commit()
            print("Data inserted into RDS")
        rds_conn.close()
    except Exception as e:
        print(f"Error: {e}")

def main():
    df = fetch_from_redshift()
    if df is not None:
        insert_into_rds(df)

if _name_ == "_main_":
    main()