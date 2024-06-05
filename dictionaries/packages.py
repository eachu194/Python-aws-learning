import boto3

# specify the service are planning on working with via a client
client = boto3.client('iam') # iam_client = boto3.client('iam')

# specify the action you want to perform with 'iam'
response = client.list_roles() #response = iam_client.list_roles
print(response)