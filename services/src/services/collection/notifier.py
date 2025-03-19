from sst import Resource
import boto3
import json
from datetime import datetime


def handler(event, context):
    client = boto3.client('events')

    bus_name = Resource.Bus.name

    response = client.put_events(
        Entries=[
            {
                'EventBusName': bus_name,
                'Source': 'scrape-event',
                'DetailType': 'cron-triggered',
                'Detail': json.dumps({
                    'time': datetime.now().isoformat(),
                })
            }
        ]
    )

    print(f"Scrape notification enqueued: {response['MessageId']}")

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Event sent to bus',
            'response': response
        })
    }