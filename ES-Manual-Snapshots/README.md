# Elasticsearch Snapshots backup to S3

**Purpose** ES only keeps 14 days of automated snapshots. To archive more than this requires taking manual snapshots; see `http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains-snapshots.html`

This Lambda function takes a snapshot of all the indices on the target ES cluster and stores them in a Snapshot directory (S3).  Ensure you have created a S3 bucket before attempting to deploy this Lambda.

It will create a IAM role with the relevant policies for the Lambda function, register the snapshot directory for the ES domain, build the lambda package, and either update (if the function already exists) or create a lambda function.

The function can be run via a schedule rule.

To schedule lambda functions use **CloudWatch** `>` **Rules** `>` **Create rule** `>` **Schedule** `>` **Add target** `>` **Function**


# Get started

The deployment process is done through `run.sh` under root folder.

* You need to run the commands under pre-requistes folder in order to create S3 bucket, IAM Role and register the repo using the lambda under RegisterRepo Folder.

* You need to update es_snapshotbucket.json with the S3 bucket you intend to use for the Snapshots.

* After Executing the run.sh under root folder, need to run the commands under cloudwatch event folder to create the cloudwatch events

To check the snapshot has been created try `curl -XGET 'https://my-es-domain-endpoint/_snapshot/my-s3-bucket/_all?pretty'`.  If you get an anonymous access error, check your ES domain access policy.

**N.B.** To restore snapshots see `http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains-snapshots.html#es-managedomains-snapshot-restore`

Reference: https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains-snapshots.html 