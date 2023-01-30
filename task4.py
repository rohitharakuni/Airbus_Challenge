#Close port 22 for the new account creation
#whenevr a new user is created in AWS. 
#The port 22 should be disabled. The user should not be allowed for ssh.
#A Python script needs to be created which should check for new accounts and disable the port.


import boto3

# Connect to the IAM service
iam = boto3.client('iam')

# Define the function to disable port 22
def disable_port_22(user_name):
    # Get the user's current access keys
    access_keys = iam.list_access_keys(UserName=user_name)

    # Iterate through the access keys
    for access_key in access_keys['AccessKeyMetadata']:
        # Deactivate the access key
        iam.update_access_key(UserName=user_name, 
                              AccessKeyId=access_key['AccessKeyId'],
                              Status='Inactive')

    # Get the user's current policies
    policies = iam.list_user_policies(UserName=user_name)

    # Iterate through the policies
    for policy_name in policies['PolicyNames']:
        # Delete the policy
        iam.delete_user_policy(UserName=user_name, PolicyName=policy_name)

    # Get the user's current groups
    groups = iam.list_groups_for_user(UserName=user_name)

    # Iterate through the groups
    for group in groups['Groups']:
        # Remove the user from the group
        iam.remove_user_from_group(UserName=user_name, GroupName=group['GroupName'])

# Use the `create_user` method of the IAM service to create a new user and disable port 22
def create_user(user_name):
    iam.create_user(UserName=user_name)
    disable_port_22(user_name)

create_user("new_user")
