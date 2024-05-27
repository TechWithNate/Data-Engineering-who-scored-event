import boto3
import zipfile
import os
import psycopg2
import tempfile

ASW_ACCESS_KEY = "AKIA6AZGBOISXXHI24F5"
AWS_SECRETE_KEY = "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"
bucket_name = 'yahoo-finance'
AWS_REGION = "us-east-1"



# AWS and Redshift configuration
s3_bucket_name = 'yahoo-finance'
s3_zip_file_key = 'yahoo-data-finances.zip'
s3_extracted_csv_key = 'extracted-data/yahoo-data-finances.csv'
redshift_endpoint = 'yahoo-test-endpoint-lpi9eomto1hw2ctt1b00.963763073573.us-east-1.redshift-serverless.amazonaws.com'
redshift_user = 'yahoo-test'
redshift_password = 'password'
redshift_db = 'dev'
redshift_port = 5439
iam_role = 'arn:aws:iam::963763073573:role/service-role/AmazonRedshift-CommandsAccessRole-20240521T123913'

# Initialize S3 client
s3 = boto3.client(
    service_name = 's3',
    region_name = AWS_REGION,
    aws_access_key_id = ASW_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRETE_KEY
)

# Step 1: Download the zip file from S3
with tempfile.TemporaryDirectory() as tmpdirname:
    local_zip_file_path = os.path.join(tmpdirname, 'file.zip')
    s3.download_file(s3_bucket_name, s3_zip_file_key, local_zip_file_path)

    # Step 2: Extract the CSV file from the zip
    with zipfile.ZipFile(local_zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(tmpdirname)
        extracted_files = zip_ref.namelist()

    # Assuming the zip contains only one CSV file or you know the name
    csv_file_name = extracted_files[0]  # or specify the CSV file name
    local_csv_file_path = os.path.join(tmpdirname, csv_file_name)

    # Optional Step 3: Upload the CSV file back to S3 if necessary
    s3.upload_file(local_csv_file_path, s3_bucket_name, s3_extracted_csv_key)

    # Step 4: Load data from the extracted CSV file into Redshift
    # Connect to Redshift
    conn = psycopg2.connect(
        dbname=redshift_db,
        user=redshift_user,
        password=redshift_password,
        host=redshift_endpoint,
        port=redshift_port
    )
    cur = conn.cursor()

    # SQL COPY command
    copy_cmd = f"""
    COPY yahoo-finances-table
    FROM 's3://{s3_bucket_name}/{s3_extracted_csv_key}'
    IAM_ROLE '{iam_role}'
    FORMAT AS CSV
    IGNOREHEADER 1;
    """

    try:
        # Execute the COPY command
        cur.execute(copy_cmd)
        conn.commit()
        print("Data loaded successfully.")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        # Close the connection
        cur.close()
        conn.close()
