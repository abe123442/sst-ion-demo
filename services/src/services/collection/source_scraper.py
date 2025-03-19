import json

def handler(event, context):
    print("[STUB] scraped from source!")

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Reddit scrape complete.',
        })
    }
