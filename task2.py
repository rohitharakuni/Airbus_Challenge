#Task 2:
#Write a python/shell script which can perform the following:
#We need alerts to notify us when A VPC is getting full

import boto3

# Set the threshold for when to send the alert (in GB)
THRESHOLD = 80

# Connect to the VPC service
client = boto3.client('ec2')

# Get the VPC usage statistics
vpcs = client.describe_vpcs()

# Iterate through each VPC
for vpc in vpcs['Vpcs']:
    # Get the VPC ID
    vpc_id = vpc['VpcId']
    
    # Get the VPC usage statistics
    usage = client.describe_vpc_attribute(VpcId=vpc_id, Attribute='enableDnsSupport')
    
    # Check if the VPC is above the threshold
    print(usage['VpcId'])
    if usage['VpcId'] > THRESHOLD:
        # Send the alert
        print(f'VPC {vpc_id} is above the threshold at {usage["VpcId"]} GB')
