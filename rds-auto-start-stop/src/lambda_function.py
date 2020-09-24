import sys
import botocore
import boto3
import os
from botocore.exceptions import ClientError


def lambda_handler(event, context):
    service_name = event['service']
    rds = boto3.client('rds')
    print('Trying to get Environment variable')
    try:
        DBcluster = os.getenv('DBClusterName')
        print('Starting RDS service for DBcluster : ' + DBcluster)

    except ClientError as e:
        print(e)
    try:
        if service_name == 'start':
            response = rds.start_db_cluster(
                DBClusterIdentifier=DBcluster
            )
        else:
            response = rds.stop_db_cluster(
                DBClusterIdentifier=DBcluster
            )
        print('Success :: ')
        print(response)

    except ClientError as e:
        print(e)
    return
    {
        'message': "Script execution completed. See Cloudwatch logs for complete output"
    }
