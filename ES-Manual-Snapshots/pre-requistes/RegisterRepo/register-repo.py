import boto3
import requests
from requests_aws4auth import AWS4Auth
import os

# include https:// and trailing /
host = 'https://' + os.environ.get("es_endpoint", None)
region = 'eu-west-2'  # e.g. us-west-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key,
                   region, service, session_token=credentials.token)

# Register repository

# the Elasticsearch API endpoint
path = '/_snapshot/'+os.environ.get("es_bucket")
url = host + path

payload = {
    "type": "s3",
    "settings": {
        "bucket": os.environ.get("es_bucket"),
        # "endpoint": "s3.amazonaws.com", # for us-east-1
        "region": "eu-west-2",  # for all other regions
        "role_arn": "arn:aws:iam::" + os.environ.get("es_accountid") + ":role/es-snapshots-lambda"
    }
}

headers = {"Content-Type": "application/json"}

r = requests.put(url, auth=awsauth, json=payload, headers=headers)

print(r.status_code)
print(r.text)
