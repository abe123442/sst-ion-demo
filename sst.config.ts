/// <reference path="./.sst/platform/config.d.ts" />
export default $config({
  app(input) {
    return {
      name: "monorepo-template",
      removal: input?.stage === "production" ? "retain" : "remove",
      protect: ["production"].includes(input?.stage),
      home: "aws",
      providers: {
        aws: {
          version: "6.72.0",
          region: "ap-southeast-2",
        }, vercel: "1.14.3"
      },
    };
  },
  async run() {
    // foundational resources are first imported, then the resources that depend on them
    const { storage } = await import("./infra/storage")
    const { secrets } = await import("./infra/secrets")

    const { scrapers } = await import("./infra/scrapers")

    const { bus } = await import("./infra/bus")
    const { notifier } = await import("./infra/notifier")
    const { cron } = await import("./infra/cron")

    return {
      s3: storage.urn,
      secrets: secrets.reddit.map(s => s.name),

      scrapers: scrapers.map(({ resource }) => resource.urn),

      bus: bus.urn,
      notifier: notifier.urn,
      cron: cron.urn,
    }
  },
});
