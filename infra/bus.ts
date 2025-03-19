import { handler as rHandler, name as rName } from './scrapers/reddit'
import { handler as sHandler, name as sName } from './scrapers/source'

export const bus = new sst.aws.Bus('Bus')
bus.subscribe(rName, rHandler, {
    pattern: {
        source: ["scrape-event"],
    },
})

bus.subscribe(sName, sHandler, {
    pattern: {
        source: ["scrape-event"],
    },
})
