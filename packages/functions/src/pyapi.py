import json

def handler(event, context):
    # Log the incoming event
    print("EVENT: \n" + json.dumps(event, indent=2))

    # Return a response
    return {
        "statusCode": 200,
        "body": f"Hello there {context.aws_request_id}",
    }