import { reddit, handler as redditHandler } from './reddit'
import { source, handler as sourceHandler } from './source'

export const scrapers: {'resource': sst.aws.Function, 'handler': string}[] = []
scrapers.push({ resource: reddit, handler: redditHandler })
scrapers.push({ resource: source, handler: sourceHandler })
