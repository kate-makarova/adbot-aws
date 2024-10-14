from Advertiser import Advertiser
import os
import boto3
from boto3.dynamodb.conditions import Key

aws_id = os.environ.get("AWS_ID")
aws_key = os.environ.get("AWS_KEY")
username = os.environ.get("USER_NAME", None)
password = os.environ.get("PASSWORD", None)
forum_id = os.environ.get("FORUM_ID")
topic_id = os.environ.get("TOPIC_ID")

dynamodb = boto3.resource('dynamodb',
                          region_name='us-east-1',
                          aws_access_key_id=aws_id,
                          aws_secret_access_key=aws_key
                          )
table = dynamodb.Table('forums')
data = []
response = table.query(
    KeyConditionExpression=Key('id').eq(int(forum_id))
)
forum = response['Items'][0]


advertiser = Advertiser(aws_id=aws_id, aws_key=aws_key)
if username is not None:
    advertiser.custom_login(url=forum['domain'], username=username, password=password)
advertiser.work(url=forum['domain']+"/viewtopic.php?id="+topic_id, id=1, home_forum_id=forum_id)
