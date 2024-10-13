from Advertiser import Advertiser
import os

aws_id = os.environ.get("AWS_ID")
aws_key = os.environ.get("AWS_KEY")
advertiser = Advertiser(aws_id=aws_id, aws_key=aws_key)
advertiser.custom_login(url="https://kingscross.f-rpg.me", username="Assistant", password="12345")
advertiser.work(url="https://kingscross.f-rpg.me/viewtopic.php?id=7288", id=1, home_forum_id=157)
