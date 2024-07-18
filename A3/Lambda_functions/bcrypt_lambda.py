import bcrypt
import json
import requests


def lambda_handler(event, context):
    value = event['value']
    hashed = bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt(12)).decode('utf-8')

    url = "http://129.173.67.234:8080/serverless/end"

    response = {
        "banner": "B00968344",
        "result": hashed,
        "arn": "arn:aws:lambda:us-east-1:921369520595:function:bcrypt_lambda",
        "action": "bcrypt",
        "value": value
    }

    payload = json.dumps(response)

    headers = {
        'Content-Type': 'application/json'
    }

    requests.request("POST", url, headers=headers, data=payload)
