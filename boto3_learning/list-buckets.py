import boto3

# Initialize a boto3 S3 client
s3_client = boto3.client('s3')
# List all buckets
response = s3_client.list_buckets()
# Get the first 3 buckets
buckets = response['Buckets']
# Print the names of the first 3 buckets
for bucket in buckets:
    print(bucket['Name'])