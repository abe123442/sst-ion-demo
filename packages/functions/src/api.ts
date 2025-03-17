import { Handler } from "aws-lambda";

export const handler: Handler = async (event, ctx) => {
  console.log("EVENT: \n" + JSON.stringify(event, null, 2))

  return {
    statusCode: 200,
    body: `Hello there ${ctx.awsRequestId}`,
  };
};
