from sst import Resource
from praw import Reddit
from dotenv import load_dotenv
import os
import boto3
import json

load_dotenv()
def getenv(key: str) -> str:
    return os.getenv(key) or ""

# Reddit API credentials
CLIENT_ID = Resource.RedditClientID.value or getenv('REDDIT_CLIENT_ID')
CLIENT_SECRET = Resource.RedditClientSecret.value or getenv('REDDIT_CLIENT_SECRET')
USER_AGENT = "SENG3011_BRAVO"

KEYWORDS = [
    "Australia", "ASX", "BHP", "Rio Tinto", "Commonwealth Bank", "CSL", "Telstra",
    "Woolworths", "Coles", "ANZ", "Westpac", "NAB", "Qantas", "Fortescue", "Afterpay",
    "Atlassian", "Canva", "Tech", "Startup", "Innovation", "AI", "Artificial Intelligence",
    "Fintech", "Cybersecurity", "Blockchain", "Renewable Energy", "Quantum Computing"
]

SUBREDDITS = ["stocks", "investing", "ausfinance", "australia", "technology", "startups", "cybersecurity"]

reddit = Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT
)

def scrape():
    bucket_name = Resource.StorageAdage3.name

    s3 = boto3.client('s3')
    s3.put_object(
        Bucket=bucket_name,
        Key='test-s3-upload.txt',
        Body='Hello from scrape_reddit!'
    )
    # separator = '='*50
    # print("Finding posts and comments related to Australian companies and tech news...\n")

    # subreddits: dict[str, list] = {}

    # for subreddit_name in SUBREDDITS:
    #     print(f"--- Subreddit: r/{subreddit_name} ---")
    #     subreddits[subreddit_name] = []

    #     subreddit = reddit.subreddit(subreddit_name)


    #     for post in subreddit.hot(limit=10):
    #         if any(keyword.lower() in post.title.lower() for keyword in KEYWORDS):
    #             subreddits[subreddit_name].append({
    #                 "post_title": post.title,
    #                 "upvotes": post.score,
    #                 "url": post.url,
    #                 "comments": []
    #             })
    #             print(f"\nPost Title: {post.title}")
    #             print(f"Upvotes: {post.score}")
    #             print(f"URL: {post.url}")

    #             # restrict comment depth
    #             post.comments.replace_more(limit=0)

    #             for comment in post.comments.list()[:5]:
    #                 if any(keyword.lower() in comment.body.lower() for keyword in KEYWORDS):
    #                     print(comment.body)

    #     print('\n' + separator + '\n')


def handler(event, context):
    scrape()

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Reddit scrape complete.',
        })
    }


if __name__ == "__main__":
    scrape()