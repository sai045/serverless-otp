import json
import boto3
import random
import time

db = boto3.resource('dynamodb')
dbTable = db.Table('OTP')

timer = 180

def lambda_handler(event,context):
    MailID = event['queryStringParameters']['MailID']
    users = []
    OTP_Verified = db.Table('OTP_Table')
    response = OTP_Verified.get_item(
        Key={
            'MailID':MailID
        })
    try:
        users.extend(response['Item'])
        length = len(users)
        if length>0:
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Headers': '*',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                },
                'body':json.dumps('User Already Verified')}
    except KeyError:
        pass
    otp = random.randint(100000,999999)

    entry = {
        'MailID':MailID,
        'otp':otp,
        'Verified':False,
        'ExpiryTime':int(time.time()) + timer
    }

    response = dbTable.put_item(Item=entry)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body':json.dumps( "A verification code has been sent top " + MailID)}