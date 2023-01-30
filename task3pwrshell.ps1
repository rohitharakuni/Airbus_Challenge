# Connect to AWS Windows server using Boto3
$ssm = New-Object -TypeName Amazon.SimpleSystemsManagement.AmazonSimpleSystemsManagementClient
$chrome_version = (Invoke-Command -Command {(Get-ItemProperty -Path "HKLM:\SOFTWARE\Wow6432Node\Google\Chrome\BLBeacon").pv} -Session $ssm.StartSession().SessionId).Trim()

# Create report
$report = "Google Chrome version: $chrome_version"

# Send report via email
Send-MailMessage -From "youremail@example.com" -To "receiver@example.com" -Subject "Google Chrome Version Report" -Body $report -SmtpServer "smtp.example.com" -Port 587 -UseSsl -Credential (Get-Credential)
