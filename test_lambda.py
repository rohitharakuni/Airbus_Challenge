import boto3
import pprint
import pytest

def test_list_instances():
    session=boto3.Session(profile_name="IAM-user",region_name='ap-south-1')
    client=session.client(service_name='ec2')
    all_regions=client.describe_regions()
    list_of_Regions=[]
    for each_reg in all_regions['Regions']:
        list_of_Regions.append(each_reg['RegionName'])
    assert len(list_of_Regions) > 0

    for each_reg in list_of_Regions:
        #print(each_reg)
        session=boto3.Session(profile_name="IAM-user",region_name=each_reg)
        resource=session.resource(service_name="ec2")

        #Lists all the instances with region
        print("List of EC2 Instances from the region: ",each_reg)
        for each_in in resource.instances.all():
            print(each_in.id,each_in.state['Name'])
        instances = resource.instances.all()
        #assert len(list(instances)) > 0
        #print (len(list(instances)))

test_list_instances()
