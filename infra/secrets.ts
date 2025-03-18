const s = (name: string) => new sst.Secret(name)

export const secrets = {
    reddit: [s('RedditClientID'), s('RedditClientSecret')],
    // other secrets go here
} as const
