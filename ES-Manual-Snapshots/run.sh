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
# Register the snapshot directory
# python es-register-snapshot-directory.py



echo -e "4.Four"
# Create your Lambda package
cp es-snapshots.py build
cd build && zip -r es-snapshots-lambda.zip *

# Check if function exists and update if it does
if aws lambda get-function --function-name es-snapshots-lambda --profile appointments 2>/dev/null; then
  echo -e "\nUpdating es-snapshots-lambda function\n"
  aws lambda update-function-code \
      --profile appointments \
      --function-name es-snapshots-lambda \
      --zip-file fileb://es-snapshots-lambda.zip

  echo -e "\nupdate environment variables with any changes\n"
  aws lambda update-function-configuration \
      --profile appointments \
      --function-name es-snapshots-lambda \
      --environment "Variables={es_endpoint=$ESENDPOINT,es_bucket=$BUCKETNAME}"

else
  # Lambda deployment
  echo -e "\nCreating es-snapshots-lambda function\n"
  aws lambda create-function \
      --profile ${AWS_PROFILE} \
      --function-name es-snapshots-lambda \
      --environment "Variables={es_endpoint=$ESENDPOINT,es_bucket=$BUCKETNAME}" \
      --zip-file fileb://es-snapshots-lambda.zip \
      --description "Elastichsearch backup snapshots to S3" \
      --role arn:aws:iam::$AWSACCOUNTID:role/es-snapshots-lambda \
      --handler es-snapshots.lambda_handler \
      --runtime python2.7 \
      --timeout 300
fi



