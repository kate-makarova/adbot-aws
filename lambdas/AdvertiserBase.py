import boto3
import json


def lambda_handler(event, context):
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    endpoints = ec2_client.describe_vpc_endpoints()
    endpoint_id = None

    for endpoint in endpoints['VpcEndpoints']:
        if endpoint['VpcEndpointType'] == 'Interface' and endpoint['ServiceName'] == 'com.amazonaws.us-east-1.ecs':
            endpoint_id = endpoint['VpcEndpointId']
            break

    if endpoint_id is None:
        response = ec2_client.create_vpc_endpoint(
            DryRun=False,
            VpcEndpointType='Interface',
            VpcId='vpc-7e177c04',
            ServiceName='com.amazonaws.us-east-1.ecs',
            SubnetIds=[
                'subnet-10f1e01f',
            ],
            SecurityGroupIds=[
                'sg-e86c5ab2',
            ],
            IpAddressType='ipv4'
        )
        endpoint_id = response['VpcEndpoint']['VpcEndpointId']

    client = boto3.client('ecs', region_name='us-east-1')

    params = event["queryStringParameters"]
    variables = [
        {
            'name': 'FORUM_ID',
            'value': params['forum_id']
        },
        {
            'name': 'TOPIC_ID',
            'value': params['topic_id']
        }
    ]

    if 'user_name' in params:
        variables.append({
            'name': 'USER_NAME',
            'value': params['user_name']
        })

    if 'password' in params:
        variables.append({
            'name': 'PASSWORD',
            'value': params['password']
        })

    response = client.run_task(
        cluster='DevCluster',
        launchType='FARGATE',
        networkConfiguration={
            'awsvpcConfiguration': {
                'assignPublicIp': 'ENABLED',
                'subnets': [
                    'subnet-10f1e01f',
                ],
                'securityGroups': [
                    'sg-e86c5ab2'
                ]
            }
        },
        #  taskDefinition='advertisement',
        taskDefinition='test_endpoints',
        overrides={
            'containerOverrides': [
                {
                    'name': 'adbot',
                    'environment': variables
                },
                {
                    'name': 'vpc_endpoint_id',
                    'environment': endpoint_id
                }
            ]
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('You have asked for it. Yurgir is coming for you')
    }