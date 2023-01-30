#Task 3:A python script/power shell script should be written to pull this information –
#The script should connect to  AWS windows server –
#Run the script to pull the application(any application/or google chrome  version info ) and send it through Report via email.
#These things needs to be automated using any devops tools. when we trigger the job manually it should perform the above 3 steps.

import boto3
import subprocess
import smtplib
from email.mime.text import MIMEText

# Connect to AWS Windows server using Boto3
client = boto3.client('ssm')
response = client.send_command(
    InstanceIds=['i-01234567890abcdef0'],
    DocumentName='AWS-RunPowerShellScript',
    Parameters={'commands': ['(Get-ItemProperty -Path "HKLM:\\SOFTWARE\\Wow6432Node\\Google\\Chrome\\BLBeacon").'
                             '"pv"']}
)

# Retrieve version information of Google Chrome
chrome_version = response['Command']['Output'].strip()

# Create report
report = "Google Chrome version: {}".format(chrome_version)

# Send report via email
sender = "youremail@example.com"
receiver = "receiver@example.com"
msg = MIMEText(report)
msg['Subject'] = "Google Chrome Version Report"
msg['From'] = sender
msg['To'] = receiver

with smtplib.SMTP('smtp.example.com', 587) as server:
    server.starttls()
    server.login(sender, "yourpassword")
    server.send_message(msg)
