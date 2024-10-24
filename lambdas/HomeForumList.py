import boto3
import json

from boto3.dynamodb.conditions import Key


def lambda_handler(event, context):
    user_id = 1
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    user_table = dynamodb.Table('users')
    response = user_table.query(KeyConditionExpression=Key('id').eq(user_id))
    user = response['Items'][0]

    home_forum_table = dynamodb.Table('home_forums')
    home_forums = []
    for home_forum_id in user['home_forums']:
        response = home_forum_table.query(KeyConditionExpression=Key('id').eq(home_forum_id))
        home_forums.append(response['Items'][0])

    return {
        'statusCode': 200,
        'body': json.dumps(home_forums)
    }
