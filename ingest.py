import boto3

ASW_ACCESS_KEY = "your_key"
AWS_SECRETE_KEY = "your_key"
bucket_name = 'yahoo-finance'
AWS_REGION = "us-east-1"


s3 = boto3.client(
    service_name = 's3',
    region_name = AWS_REGION,
    aws_access_key_id = ASW_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRETE_KEY
)

local_file_path = 'transformed_data.zip'

s3_key = 'yahoo-data-finances.zip'

response = "This is the response"

try:
    response = s3.upload_file(local_file_path, bucket_name, s3_key)
    print(f'File uploaded succesfully to s3 bucket{response}')
except Exception as e:
    print(f'Failed to upload file: {e}')

print('End of code')

#s3.upload_file(r'D:\Tech\Data eng\Emile Project\Project\Yahoo Finances', 'yahoo-finance', 'yahoo-data-finances.zip')