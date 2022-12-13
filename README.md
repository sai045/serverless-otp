# Serverless-otp
 
 ## Plan of the project
![Serverless-OTP](https://user-images.githubusercontent.com/85741790/207326881-597cdefd-9e8b-4303-bf37-f8ffdbea0da9.png)

# Technologies Used

## Angular:
- This is a javascript library that is used for building library.
- THis works by dynamically updating DOM thus giving us fast and reactive applications.

## Bootstrap:
- This is a styling framework that helps us write responsive web apps with custom writen classes.

## AWS Lambda:
- This is a function as a service that gives us high scalability.

## AWS API Gateway:
- It is a service provided by amazon web services to integrate lambda functions. This is configured with Lambda proxy to get an customised request and response body.
- This is identical to having API endpoints from a NodeJS application.

## DynamoDB:
- This is NoSQL database. We are using TTL feature that deletes data after a set time which helps us reduce storage requirements.
- This can be easily inegrated to AWS Lambda.

## Amazon SES:
- Simple email service is a service provided by Amazon that is used to send transactional emails. This uses SMTP.

## Amazon Cloudfront:
- Used to monitor logs and solve bugs between AWS Lambda Triggers and DynamoDB Triggers

## SMTPLIB:
- Used to send Emails to the users.