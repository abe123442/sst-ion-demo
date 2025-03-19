import { secrets } from '../secrets'
import { storage } from '../storage'

const name = "RedditScraper"
const handler = 'services/src/services/collection/reddit_scraper.handler'

const reddit = new sst.aws.Function(name, {
    handler,
    runtime: 'python3.11',
    link: [...secrets.reddit, storage]
});

export { reddit, handler, name }