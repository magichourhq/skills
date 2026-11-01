# Retrieve an existing Magic Hour image in Botpress

Use a Botpress Studio **Execute Code** card to retrieve an image project you already own. This example is source-reviewed; it has not been run in Botpress. It does not create media, download a file, or publish a bot.

Start in an existing **private, unpublished bot**. Keep the project ID operator-controlled for this first check. A public bot needs a separate design that authorizes each user to access their own projects; hiding an API key alone does not provide that authorization.

## Set up the card

1. Open **Bot Settings → Configuration Variables → +**. Add `MAGIC_HOUR_API_KEY` and enter your Magic Hour API key as its value. Botpress documents these variables as encrypted and makes them available to code through `env`.
2. In your Workflow's Variables panel, create the following **Workflow** variables. Set `magicHourProjectId` to an existing image project ID from your Magic Hour account.

   | Name | Type | Purpose |
   | --- | --- | --- |
   | `magicHourProjectId` | String | Existing project to retrieve |
   | `magicHourStatus` | String | Returned project status |
   | `magicHourReady` | Boolean | Whether a usable download was found |
   | `magicHourDownloadUrl` | String | Private signed download URL |
   | `magicHourExpiresAt` | String | Download expiry timestamp |

3. Create a new, isolated **Standard Node** containing only this **Execute Code** card, with no outgoing transitions to other cards or Autonomous Nodes. Paste [recover-image.js](../examples/botpress/recover-image.js) into its code editor. Playing this node must not run unrelated bot behavior. This is Studio card code, with top-level `await`, `workflow`, `env`, and the preinstalled global `axios`. Do not add imports or install a package. An Autonomous Node or AI-controlled Action is unnecessary for this check.
4. Select that Standard Node and press **Play** to start the Studio Emulator there once. Inspect the Workflow variables privately. Do not add a chat message that prints the key or signed URL, and do not use Share or Publish for this check.

The card makes one `GET /v1/image-projects/{id}` request to Magic Hour. It clears its output fields before the request, checks the HTTP response and matching project ID, then sets `magicHourReady` only when the project is enabled, its status is `complete`, and a download has an HTTPS URL with a parseable future `expires_at`.

## Read the result

- **Ready is true:** the URL and expiry fields contain the exact returned download. Treat the URL as private. A later download step must use that URL without the Magic Hour `Authorization` header and save the actual file in your own private storage before the URL expires.
- **Ready is false:** do not use a previous URL. The project may be pending, disabled, failed, canceled, or have no usable download. Inspect its status privately and retrieve the **same project ID** later when appropriate. The card does not poll or retry.
- **The card fails:** check the configuration and project ID privately. The fixed error deliberately omits the HTTP error object, response body, and request headers, which could contain credentials. Do not add `console.log(error)` or print the Axios response/configuration while debugging.

Keep the key in Configuration Variables. Do not copy it into Workflow, User, or Conversation variables, prompts, messages, logs, or shared examples. Workflow outputs, emulator/debug history, and signed URLs also require private handling. Native execution, exact installed Axios behavior, and Botpress's runtime masking/storage behavior remain unverified by this example.

Before adding paid generation, confirm the tool, inputs, current price, credit balance, and spending limit, including any repair allowance. Submit once, preserve the accepted project ID, and recover that same ID after interruption or uncertain acceptance. Do not create a replacement merely because a response was lost. See the [workflow guide](workflow-guide.md) for the broader creation and recovery sequence.

## References

- [Botpress Execute Code](https://botpress.com/docs/studio/concepts/cards/execute-code/), [available code packages](https://botpress.com/docs/studio/guides/advanced/use-code/), and [Standard Nodes and Play](https://botpress.com/docs/studio/concepts/nodes/introduction/)
- [Configuration Variables](https://botpress.com/docs/studio/concepts/variables/scopes/configuration/), [variable types](https://botpress.com/docs/studio/concepts/variables/overview/), and [Workflow scope](https://botpress.com/docs/studio/concepts/variables/scopes/workflow/)
- [Magic Hour image project details](https://docs.magichour.ai/api-reference/image-projects/get-image-details)
