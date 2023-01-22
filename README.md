********************  Welcome to Airbus_Challenge  ************************

1.Deploying an EC2 Machine using TF:

A. Terraform AWS EC2 Instance

Prerequisites:

1. Terraform must be installed on your machine.

2. An AWS account with the necessary permissions to create and manage EC2 instances.

3. Access and secret keys for your AWS account.

Usage:

1.Clone or download this repository.

2.In the 'provider' block, update the 'region', 'access_key', and 'secret_key' fields with the values for your AWS account.

3.In the 'resource' block, update the 'ami' and 'instance_type' fields to match the desired values for your EC2 instance.

4.Run 'terraform init' to initialize the Terraform working directory.

5.Run 'terraform apply' to create the EC2 instance.

6.Once the EC2 instance is created, you can use the 'terraform show' command to view details about the instance and the 'terraform destroy' command to delete the instance.

Note:>

1.The 'tags' block is used to add a tag to the instance, with a key of "Name" and a value of "firstserver-instance".You can add more tags or update the existing ones as per your requirement.

2.Be mindful that creating EC2 instances can incur charges on your AWS account, so be sure to delete the instances when you are done using them.

B. Write a python program to list the all EC2 instance per region:

This script is used to retrieve a list of all available AWS regions and instances in those regions. It utilizes the boto3 library to interact with the AWS EC2 service.

Prerequisites:

1.Python must be installed on your machine.

2.boto3 library must be installed.

3.An AWS account with the necessary permissions to list regions and instances.

4.Access and secret keys for your AWS account.

This code is written in Python and uses the boto3 library to interact with the AWS EC2 service.

It creates a session using the specified IAM user profile and region, and then uses the client object to retrieve a list of all available AWS regions. It then loops through the regions, creating a new session for each one, and uses the resource object to retrieve a list of all EC2 instances for that region. It then prints the instance ID and state for each instance.

It will print the list of all regions first then for each region it will print the id and state of all instances.

It will use the IAM user's credentials and the specified region to connect to AWS. The code assumes that the IAM user has the necessary permissions to list regions and instances in the specified profile.

Usage:

1.Clone or download this repository.

2.Update the profile_name and region_name fields in the script with the values for your AWS account.

3.Run the script using python scriptname.py command.

4.The script will print the list of all regions first then for each region it will print the id and state of all instances.

Note:

1.Be mindful that using this script will consume some of your AWS resources and may incur charges on your AWS account.

2.This script should be run in environment where the IAM user has the necessary permissions and access key and secret keys are set.

3.It is recommended to test the script in a test environment before running it in production.

4.This script can only be used to get the information of running instances and their id and state, it doesn't have any functionality of creating or terminating instances.

C. Test this code using pytest:

This code is a Python script that uses the 'boto3' library to interact with the AWS EC2 service and 'pytest' library for testing.

It defines a function 'test_list_instances()' that does the following:

1.It creates a session using the specified IAM user profile and region, and then uses the 'client' object to retrieve a list of all available AWS regions.

2.It then loops through the regions, creating a new session for each one, and uses the 'resource' object to retrieve a list of all EC2 instances for that region. It then prints the instance ID and state for each instance.

3.The script runs the test_list_instances() function which will print the list of all the regions, for each region it will print the id and state of all instances.
It checks if the count of list of regions is greater than zero and it will return an assertion error if the count of regions is zero.

4.It will use the IAM user's credentials and the specified region to connect to AWS. The code assumes that the IAM user has the necessary permissions to list regions and instances in the specified profile.

This script should be run in environment where the IAM user has the necessary permissions and access key and secret keys are set.

Prerequisites:

1.Clone or download this repository.

2.Update the profile_name and region_name fields in the script with the values for your AWS account.

3.Run the script using python scriptname.py command.

4.The script will run the test_list_instances() function which will print the list of all the regions, for each region it will print the id and state of all instances.

5.The script will check if the count of list of regions is greater than zero and it will return an assertion error if the count of regions is zero.

Note:

Be mindful that using this script will consume some of your AWS resources and may incur charges on your AWS account.

This script should be run in environment where the IAM user has the necessary permissions and access key and secret keys are set.

It is recommended to test the script in a test environment before running it in production.

2. Deployment of python code/Lambda using Jenkins pipeline:

Here is a Jenkinsfile that can be used to deploy the code to AWS Lambda using Jenkins,

Please find above for the jenkinsfile

-> This Jenkinsfile defines a pipeline with three stages:

1.The first stage, "Checkout", checks out the code from the specified git repository.

2.The second stage "Build" runs a shell command that installs the dependencies listed in a requirements.txt file.

3.The third stage, "Deploy", uses the AWS CLI to package the code and its dependencies into a zip file, upload it to an S3 bucket and create a new AWS Lambda function using this zip.

You'll need to replace the placeholders '<your-repo>', '<your-code>', '<YOUR-ACCOUNT-ID>' with the appropriate values for your repository, code and account id.

It also assumes that your Jenkins agent has the necessary permissions to access the AWS account.
You will also need to configure AWS credentials in Jenkins.

It is recommended to test this pipeline in a test environment before running it in production.
Please also make sure that the 'lambda_execution_role' and 'lambda_deployment_bucket' exists and the role should have enough permissions to create and access lambda and s3.

Deployment of EC2 instance listing to AWS Lambda using Jenkins:-

This Jenkinsfile is used to deploy a Python script that lists all available AWS regions and instances in those regions to AWS Lambda using Jenkins.

Prerequisites:

1.Jenkins must be installed and configured with necessary plugins (e.g. 'Pipeline plugin')
2.The Jenkins agent must have the necessary permissions to access the AWS account and necessary software installed (e.g. AWS CLI)
3.AWS credentials must be configured in Jenkins
4.An S3 bucket must be created and configured to store the deployment package
5.An IAM role 'lambda_execution_role' must be created with permissions to create, update and access Lambda and S3 services
6.The script should be checked in to a git repository

Usage:

1.Create a new Jenkins pipeline job and configure it to use the Jenkinsfile.

2.Update the git repository URL, '<your-repo>', '<your-code>', '<YOUR-ACCOUNT-ID>', 'lambda_execution_role' and 'lambda_deployment_bucket' fields in the Jenkinsfile with the appropriate values for your repository, code, account id, role and bucket.
3.Run the pipeline.
4.The pipeline will check



THANK YOU !!!






