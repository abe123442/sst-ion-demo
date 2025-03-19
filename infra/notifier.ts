import { bus } from "./bus"

const handler = 'services/src/services/collection/notifier.handler'

export const notifier = new sst.aws.Function("FunctionNotifier", {
    handler,
    link: [bus],
})
