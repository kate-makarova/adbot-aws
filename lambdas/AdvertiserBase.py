import boto3
import json

def lambda_handler(event, context):
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
                'subnet-a2adf78c',
                'subnet-c5a3fb99',
                'subnet-15c4a72b',
                'subnet-bd1ef1f0',
                'subnet-7b401f1c'
            ],
            'securityGroups': [
                'sg-e86c5ab2'
            ]
        }
    },
        taskDefinition='advertisement',
        overrides={
            'containerOverrides': [
                {
                    'name': 'adbot',
                    'environment': variables
                }
            ]
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('You have asked for it. Yurgir is coming for you')
    }
