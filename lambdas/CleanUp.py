import json
import boto3

def lambda_handler(event, context):
    print('Cleanup called')
    print(event)

    client = boto3.client('ecs', region_name='us-east-1')

    response = client.list_tasks(
    cluster='DevCluster',
    maxResults=5,
    desiredStatus='RUNNING'
    )

    if not len(response['taskArns']):
        endpoint_id = False
        overrides = event['detail']['overrides']['containerOverrides'][0]['environment']
        for override in overrides:
            if override['name'] == 'vpc_endpoint_id':
                endpoint_id = override['value']
                break
        if endpoint_id:
            response = client.delete_vpc_endpoints(
            DryRun=False,
            VpcEndpointIds=[
                endpoint_id,
            ])

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
