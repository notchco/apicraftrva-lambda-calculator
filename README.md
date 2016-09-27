# apicraftrva-lambda-calculator

### Summary
This repository has a very simple arithmetic calculator as an example AWS Lambda function and a series of screenshots that capture the process of creating the Lambda function and fronting it with API Gateway.


### Basic Calculator
Copy-paste the code in basic_calc.py in the 'Inline' Lambda code block.
Specify python2.7 and 'lambda_function.handler' in the Lambda function Configuration.

The Role can be AWSLambdaBasicExecutionRole (see: Identity and Access Management, Create Role).


### Basic Calculator with Dynamo DB
Copy-paste the code in basic_calc_ddb.py in the 'Inline' Lambda code block.
Specify python2.7 and 'lambda_function.handler' in the Lambda function Configuration.

Create a DynamoDB table with the name 'calculations' with the field 'timestamp' as the primary key.

The Role must have the appropriate DynamoDB access (e.g. AmazonDynamoDBFullAccess).


### API Gateway
See the screenshots folder for the steps to create an API Gateway for the calculator Lambda function.