import boto3

client = boto3.client('iam')

#established connection between aws and python and store it in a variable called client
response = client.list_users()

print(response)