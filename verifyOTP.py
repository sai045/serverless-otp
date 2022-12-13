import json
import boto3
import time

db = boto3.client('dynamodb')


def lambda_handler(event, context):
    MailID = event['queryStringParameters']['MailID']

    OTPFromUser = event['queryStringParameters']['OTPFromUser']

    response = db.query(
        TableName='OTP',
        KeyConditionExpression='MailID = :MailID',
        ExpressionAttributeValues={
            ':MailID': {'S': MailID}
        }, ScanIndexForward=False, Limit=1
    )

    if response['Count'] == 0:
        return "No such OTP was generated"
    else:
        latestSortedOTP = response['Items'][0]['otp']['N']
        if int(response['Items'][0]['ExpiryTime']['N'])<int(time.time()):
            return "Time Over"
        else:
            if latestSortedOTP == OTPFromUser:
                return "Verified"
            else:
                return "Wrong OTP"