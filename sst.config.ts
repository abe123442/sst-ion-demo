/// <reference path="./.sst/platform/config.d.ts" />
export default $config({
  app(input) {
    return {
      name: "monorepo-template",
      removal: input?.stage === "production" ? "retain" : "remove",
      protect: ["production"].includes(input?.stage),
      home: "aws",
      providers: { aws: "6.72.0", vercel: "1.14.3" },
    };
  },
  async run() {
    await import("./infra/api");
    const { storage } = await import ("./infra/storage");
    await import("./infra/secrets")
  },
});
