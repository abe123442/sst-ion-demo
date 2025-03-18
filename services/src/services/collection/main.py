# the idea is that this is the "scraper" that will get manually pinged by a 
# cron job service (cron-job.org)

import services.collection.reddit as reddit

def handler(event, context):
    # run all scrapers -- maybe there is a scope to multithread this
    reddit.scrape_reddit()

    return {
        "statusCode": 200,
        "body": event,
    }

