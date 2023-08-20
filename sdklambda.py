import json
import boto3

# Create a Boto3 lambda client

lambda_client = boto3.client('lambda')
print("Invoking another lambda function.......")
# Define the parameters for the Lambda invocations
function_name = "TestFun"
payload = {'type' : "write",'key2' : "value2"}

# Invoke the lambda function


response = lambda_client.invoke(
    FunctionName=function_name,
    InvocationType='RequestResponse',
    Payload=json.dumps(payload)
    )

# Extract the response from the incvocations
response_payload = response['Payload'].read().decode('utf8')
print(response_payload)

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
