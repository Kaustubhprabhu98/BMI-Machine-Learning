#invoke

import boto3
import json

runtime_client = boto3.client('sagemaker-runtime')
content_type = "application/json"
request_body = {"Input": [[38, 1, 1.778]]}
data = json.loads(json.dumps(request_body))
payload = json.dumps(data)
endpoint_name = "bmi-local-ep2023-06-05-12-33-47"

response = runtime_client.invoke_endpoint(
    EndpointName=endpoint_name,
    ContentType=content_type,
    Body=payload)
result = json.loads(response['Body'].read().decode())['Output']
print(result)
