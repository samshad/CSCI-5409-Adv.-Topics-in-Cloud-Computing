import hashlib
import json
import requests


def lambda_handler(event, context):
    value = event['value']
    result = hashlib.md5(value.encode('utf-8')).hexdigest()

    url = "http://129.173.67.234:8080/serverless/end"

    response = {
        "banner": "B00968344",
        "result": result,
        "arn": "arn:aws:lambda:us-east-1:921369520595:function:md5_lambda",
        "action": "md5",
        "value": value
    }

    payload = json.dumps(response)

    headers = {
        'Content-Type': 'application/json'
    }

    requests.request("POST", url, headers=headers, data=payload)
