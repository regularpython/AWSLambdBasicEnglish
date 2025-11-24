import json

# import requests


def lambda_handler(event, context):

    print("Hello RegularPython")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",

        }),
    }
