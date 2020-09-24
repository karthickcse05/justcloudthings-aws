#!/usr/bin/python
# -*- coding: utf-8 -*-
from boto.connection import AWSAuthConnection
# import AWSAuthConnection
import os
import boto


class ESConnection(AWSAuthConnection):

    def __init__(self, region, **kwargs):
        super(ESConnection, self).__init__(**kwargs)
        self._set_auth_region_name(region)
        self._set_auth_service_name("es")

    def _required_auth_capability(self):
        return ['hmac-v4']


if __name__ == "__main__":

    client = ESConnection(
        region='eu-west-2',
        host=os.environ.get("ESENDPOINT", None),
        security_token=os.environ.get("AWSSECRETTOKEN"),
        aws_access_key_id=os.environ.get("AWSKEY"),
        aws_secret_access_key=os.environ.get("AWSSECRET"), is_secure=True)

    print('Registering Snapshot Repository')
    print('Bucket: ' + os.environ.get("BUCKETNAME"))
    print('ESENDPOINT: ' + os.environ.get("ESENDPOINT"))
    print(client)
    resp = client.make_request(method='PUT',
                               path='_snapshot/' +
                               os.environ.get("BUCKETNAME"),
                               data='{"type": "s3","settings": { "bucket": "' + os.environ.get("BUCKETNAME") + '","region": "eu-west-2","role_arn": "arn:aws:iam::' + os.environ.get("AWSACCOUNTID") + ':role/es-snapshots-lambda"}}')
    body = resp.read()
    print(body)
