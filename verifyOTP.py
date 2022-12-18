import json
import boto3
import time

db = boto3.client('dynamodb')


def lambda_handler(event, context):
    MailID = event['queryStringParameters']['MailID']

    OTPFromUser = event['queryStringParameters']['OTPFromUser']
    # OTPFromUser = int(OTPFromUser)

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
        ExpiryTime = response['Items'][0]['ExpiryTime']['N']
        if int(response['Items'][0]['ExpiryTime']['N'])<int(time.time()):
            return {
                'statusCode': 200,
                    'headers': {
                        'Access-Control-Allow-Headers': '*',
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                    },
                'body':json.dumps( "Time Over")}
        else:
            if latestSortedOTP == OTPFromUser:
                dbTable = boto3.resource('dynamodb')
                table = dbTable.Table('OTP_Table')
                # updateResponse = table.update_item(
                #     Key = {'MailID':MailID,'ExpiryTime':ExpiryTime,'otp':latestSortedOTP},
                #     UpdateExpression="set Verified = :s",
                #     ExpressionAttributeValues = { ':s':True },
                #     # ReturnValues = "UPDATED_NEW"
                #     )
                addUser = table.put_item(Item={
                    'MailID':MailID
                })
                return {
                    'statusCode': 200,
                    'headers': {
                        'Access-Control-Allow-Headers': '*',
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                    },
                    'body':json.dumps( "Verified")}
            else:
                return {
                    'statusCode': 200,
                    'headers': {
                        'Access-Control-Allow-Headers': '*',
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                    },
                    'body':json.dumps("Not Verified")}
    