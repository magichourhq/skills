# Pabbly Connect: recover an existing Magic Hour image

Create a private Pabbly action that reads an existing image project and exposes its status and current download links to your workflow. It does not create, regenerate or purchase media.

This is a source-reviewed setup guide. Pabbly installation, saved-credential handling and a real action run remain unverified. It is not a shared app or an accepted marketplace listing.

## Before you start

You need access to the Pabbly Connect Developer Portal, a [Magic Hour API key](https://magichour.ai/developer?tab=api-keys), and the ID of an image project owned by that Magic Hour account. Start with an already completed project. Keep its original ID so recovery never requires another generation.

Use Pabbly's normal connection form for the key. Do not put it in chat, this guide, an action's default values, screenshots or an exported request.

## Create the private app and connection

1. Open Pabbly Connect's **Developer Portal → Apps**. Check your existing apps before using **Create App**. Reuse an existing Magic Hour app rather than creating another.
2. Name the app `Magic Hour` and describe it as `Retrieves existing Magic Hour image projects.` Complete the app details using your authorized branding. Pabbly specifies a 64 × 64 PNG logo.
3. Select **Bearer Token** authentication. Pabbly creates a **Token** field for workflow connections. Enter the Magic Hour key there when connecting your account, not as a hardcoded action header. Use the connection's bearer authentication for the request.

Pabbly's [app/authentication guide](https://docs.pabbly.com/pabbly/doc/how-to-configuring-details-and-authentication-method-within-pabbly-connect.2426) documents these fields. No OAuth client, webhook trigger or separate authentication request is needed for this retrieval action.

## Configure one action

Open **Actions → Create New Action**. Use the following values in **Action Event API Configuration**:

| Setting | Value |
| --- | --- |
| Action name | `Get Image Project` |
| Description | `Retrieves the status and download links of an existing image project.` |
| HTTP request method | `GET` |
| API Endpoint URL | `https://api.magichour.ai/v1/image-projects/{{project_id}}` |
| HTTP Headers | `Accept: application/json` |
| Request body | None |
| Wrap in Array | Off |

Under **Set Body/Query Parameters**, add the URL/path parameter `project_id`, label it `Project ID`, and make it required. Do not send it as a query parameter or request body. The value is the unmodified project ID, not a full URL. Pabbly documents double-curly-brace URL variables in its [action configuration guide](https://docs.pabbly.com/pabbly/doc/how-to-configure-actions-within-pabbly-connect.2428) and URL fields in its [parameter guide](https://docs.pabbly.com/pabbly/doc/how-to-set-bodyquerypath-parameters-within-pabbly-connect.21844).

Save the action. In a workflow, add a step from the **Private Apps** tab, choose your Magic Hour app and action, connect through the Token field, and supply the existing project ID. Run this read-only action once. Do not add a generation step, repeating schedule or polling loop for the initial verification.

## Check the result before using a link

The [Magic Hour response](https://docs.magichour.ai/api-reference/image-projects/get-image-details) contains these raw API fields. Pabbly may flatten their labels in its mapping UI; inspect the actual returned fields rather than assuming a label or adding a fabricated output.

Before forwarding a link, require an HTTP `200` response and all the checks below.

| API field | How to use it |
| --- | --- |
| `id` | Must match the project ID you supplied. |
| `enabled` | Must be `true` before using the asset. |
| `status` | Must be `complete` before using a download. |
| `downloads[].url` | Choose one returned HTTPS download link only after the checks pass. |
| `downloads[].expires_at` | Its timestamp must still be in the future when the next step fetches the link. |

For `queued`, `rendering` or `draft`, stop without passing a media link onward. For `error`, `canceled`, a disabled project, missing downloads or an unexpected ID, stop and inspect the project. An HTTP success alone does not mean an image is ready.

If the request times out or a download link expires, retrieve the **same project ID** again. Do not create a replacement image. For authentication or access failures, check the Pabbly connection and project ownership before another retrieval.

The response can include private project data and signed download URLs. They may appear in Pabbly's action output and run history. Check connection redaction and workspace sharing before using real credentials; do not publish raw responses or screenshots. Send a chosen link only to an approved downstream app that is allowed to receive the asset. Pabbly plan/task limits still apply.

## Private use and publication are separate

Pabbly documents manual use through **Private Apps**. For public discovery through its Workflow Builder AI, its [publication instructions](https://docs.pabbly.com/pabbly/doc/pabbly-connect-pabbly-mcp-integration-builder-connect-ai-assistants-with-pabbly-connect-jchco) require setting the relevant actions to **Live**, then **App Status → Submit for Review**. Pabbly must approve the app before that discovery is available. This guide does not submit or publish it.

Pabbly also documents [cURL import](https://docs.pabbly.com/pabbly/doc/import-curl-request.19077), but this guide supplies no connector-export JSON or credential-bearing import file. Use the documented manual fields above. Native connection, response mapping, secret redaction and end-to-end handoff still need verification before sharing a reusable app.
