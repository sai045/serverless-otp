import smtplib
from email.message import EmailMessage
import ssl


def lambda_handler(event,context):
    # print(event)
    if(event['Records'][0]['eventName'] == 'INSERT'):
        MailID = event['Records'][0]['dynamodb']['Keys']['MailID']['S']
        OTP = event['Records'][0]['dynamodb']['NewImage']['otp']['N']
        sender = "saivarshith3041@gmail.com"
        password = 'uerufsxiwffnuhrq'
    
        Subject = "OTP for server"
        body = "OTP: {}".format(OTP)
    
        em = EmailMessage()
        em['From'] = sender
        em['To'] = MailID
        em['Subject'] = Subject
    
        em.set_content(body)
    
        context = ssl.create_default_context()
    
        with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
            smtp.login(sender,password)
            smtp.sendmail(sender,MailID,em.as_string())

        return "Mail sent!"
        