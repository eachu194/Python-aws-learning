import boto3

client  = boto3.client("ec2", region_name = "us-east-1") # creates a connection and store it in a variable called client

response = client.describe_volumes(
    Filters=[
        {
            'Name': 'status',
            'Values': [
                'available',
            ]
        },
        # {
        #     'Name': 'encrypted',
        #     'Values': [
        #         'true',
        #     ]
        # },
        
    ],
)
# :::::::", i["VolumeId"]
for i in response["Volumes"]:
    print("Volumes", i["VolumeId"])
    response = client.delete_volume(
    VolumeId= i["VolumeId"],
    
    )
print(response["Volumes"])
#watch the video from 2:00 to understand it better ||  
#Link to video https://us02web.zoom.us/rec/play/y68GUzI8WBRv2hyqCxdVsI3tx4C8yWnljtut-fQ81oCfrl4VXl5PjXkA_TWVFzdu3RR51-zDnhMItAev.UWRYv7JcRiGZGVbl?canPlayFromShare=true&from=share_recording_detail&continueMode=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fus02web.zoom.us%2Frec%2Fshare%2FxnijrSPogs9AarBEp4vW9YITxAYPRCqo_pLmKMb0Lb7X4m2UhBtl4ddGhHCQiBQ-.AYd5ixqPM0nsoG4x 