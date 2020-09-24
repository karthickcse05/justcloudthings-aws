import sys
import botocore
import boto3
import os
from botocore.exceptions import ClientError


def lambda_handler(event, context):
    service_name = event['service']
    ec2 = boto3.client('ec2')
    print('Trying to get Environment variable')
    try:
        InstanceID = os.getenv('InstanceID')
        print('Starting ec2 service for Instance ID : ' + InstanceID)

    except ClientError as e:
        print(e)
    try:
        if service_name == 'start':
            response = ec2.start_instances(
                InstanceIds=InstanceID
            )
        else:
            response = ec2.stop_instances(
                InstanceIds=InstanceID
            )
        print('Success :: ')
        print(response)

    except ClientError as e:
        print(e)
    return
    {
        'message': "Script execution completed. See Cloudwatch logs for complete output"
    }
