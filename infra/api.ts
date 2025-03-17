export const api = new sst.aws.Function("Scraper", {
    handler: 'functions/src/functions/api.handler',
    python: {
        container: false,
    },
    runtime: 'python3.11',
    url: true,
});