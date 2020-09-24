import boto3


def lambda_handler(event, context):
    ecsregion = event['region']
    cluster_name = event['cluster']
    service_name = event['service']
    task_count = event['taskCount']
    ecs_client = boto3.client('ecs', region_name=ecsregion)
    response = ecs_client.update_service(
        cluster=cluster_name, service=service_name, desiredCount=int(task_count))
    print(response)
