// doesn't work for some reason
export const cron = new sst.aws.Cron("cron_data_collection", {
    function: {
        handler: 'functions/src/functions/api.handler',
        runtime: 'python3.11',
        timeout: '2 minutes',
        // concurrency
    },
    schedule: 'rate(5 minutes)',
})