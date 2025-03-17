# the idea is that this is the "scraper" that will get manually pinged by a 
# cron job service (cron-job.org)
def handler(event, context):
    return {
        "statusCode": 200,
        "body": event,
    }