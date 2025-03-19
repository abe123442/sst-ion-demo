import { notifier } from "./notifier"

export const cron = new sst.aws.Cron("CronNotifier", {
    // function: notifier,
    function: notifier.arn,
    schedule: 'rate(1 day)',
})