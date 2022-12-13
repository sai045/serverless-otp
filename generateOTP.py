import json
import boto3
import random
import time

db = boto3.resource('dynamodb')
dbTable = db.Table('OTP')

timer = 180

def lambda_handler(event,context):
    MailID = event['queryStringParameters']['MailID']

    otp = random.randint(100000,999999)

    entry = {
        'MailID':MailID,
        'otp':otp,
        'ExpiryTime':int(time.time()) + timer
    }

    response = dbTable.put_item(Item=entry)

    return "A verification code has been sent top " + MailID