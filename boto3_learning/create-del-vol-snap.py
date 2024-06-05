# this block create ebs volume
import boto3

client  = boto3.client("ec2", region_name = "us-east-1") # creates a connection and store it in a variable called client

# response = client.create_volume(
#     AvailabilityZone='us-east-1a',
#     Iops=100,
#     Size=4,
#     VolumeType="gp3",
#     Encrypted=False,
# )

# print(response)
#---------------------------------------------------------------------------------------------------

#this block describes the volume ie it will to the aws account using the profile details and list the details of the volume(s)
response = client.describe_volumes(
    Filters=[
        {
            'Name': 'status',
            'Values': [
                'available',
            ]
        },
    ]
)
for i in response["Volumes"]:
    print("Volumes::::::", i["VolumeId"])


    response = client.create_snapshot(
        Description='Create volume snapshot',
        VolumeId=i["VolumeId"],

    )

    print(response)
    response = client.delete_volume(
        VolumeId=i["VolumeId"],
        
    )


    
