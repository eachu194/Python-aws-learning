import boto3

client  = boto3.client("ec2", region_name = "us-east-1") # creates a connection and store it in a variable called client

response = client.describe_volumes(
   Filters=[
        {
            'Name': 'status',
            'Values': [
                'available', #'in-use',
            ]
        },
        # {
        #     'Name': 'encrypted',
        #     'Values': [
        #         'true'],
        # },
    ],
)
for i in response["Volumes"]:

    print("Volume:::", i["VolumeId"])

    #this will get the volime from the loop and delete. this has to be in the loop
    response = client.delete_volume( 
        VolumeId = i["VolumeId"],
        
    )     

    print(response)

    
