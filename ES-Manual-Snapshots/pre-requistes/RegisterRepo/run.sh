#!/usr/bin/env bash

#
# The following creates a lambda function that can be run via a Cloudwatch schedule rule
# It creates a IAM role (if it doesn't exist) and policies required to run
# It creates (or updates if exists) a lambda function called es-snapshots-lambda
# It assumes an S3 bucket $BUCKETNAME already exists for storing the ES snapshots
#

AWS_PROFILE="appointments"
ESENDPOINT="endpointname" # bucket must exist in the SAME region the deployment is taking place
BUCKETNAME="bucketname"
AWSACCOUNTID="xxxxxx"


echo -e "1.First"
# Make build dir if not exist
if [[ ! -e build ]]; then
  mkdir build
fi


echo -e "2.Second"
# Install requirements
pip install -r requirements.txt -t build

echo -e "3.Third"
# Create your Lambda package
cp register-repo.py build
cd build && zip -r register-repo.zip *





