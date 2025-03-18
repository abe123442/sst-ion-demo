import { secrets } from './secrets'
import { storage } from './storage'

export const api = new sst.aws.Function("Scraper", {
    handler: 'services/src/services/collection/main.handler',
    runtime: 'python3.11',
    url: true,
    link: [...secrets.reddit, storage]
});