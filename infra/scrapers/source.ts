const name = "SourceScraper"
const handler = 'services/src/services/collection/source_scraper.handler'

const source = new sst.aws.Function(name, {
    handler,
    runtime: 'python3.11',
});

export { source, handler, name }