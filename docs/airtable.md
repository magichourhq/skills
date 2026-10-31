# Recover a Magic Hour image in Airtable

Draft: this native automation example is source-reviewed. Airtable installation, Secrets access, authenticated retrieval and output mapping have not been verified in an Airtable workspace.

Use Airtable's **Run a script** automation action to retrieve an image you already created. This example makes one GET request. It does not create media, buy credits, poll, download files or update records itself. No local server, SDK or additional dependency is needed.

## Configure the script

1. In your existing base, open **Automations** and add a **Run a script** action after your chosen trigger. Preserve existing automations and fields. You need permission to configure automations and access to this action; it is not available on Team plan trials.
2. In the action's **Script input** sidebar, add `projectId`. Map it to the triggering record's existing Magic Hour image-project ID. For an initial manual test, enter an already completed image project's ID from your own account. Do not create another image for this example.
3. In the script editor's **Secrets** tab, add or select `MAGIC_HOUR_API_KEY` with your existing [Magic Hour API key](https://magichour.ai/developer?tab=api-keys). Grant access only to the people who need it. Do not use an ordinary script input, cell, pasted code, chat, command argument or screenshot for the key.
4. Paste [`recover-image.js`](../examples/airtable/recover-image.js) into the script editor. It uses `input.config()` for the project ID and `input.secret("MAGIC_HOUR_API_KEY")` for the secret.
5. Test the action using that saved project. Inspect only the intended outputs. Test and review the later steps before enabling the automation.

The Secrets function follows Airtable's [official employee announcement](https://community.airtable.com/announcements-6/introducing-secrets-in-automations-secure-your-api-keys-and-sensitive-data-45092). The current [Run a script help article](https://support.airtable.com/articles/6328053615-airtable-automation-action-run-a-script) contains a conflicting property-style example, while the public input reference omits Secrets. This example uses the documented function form without a fallback. Actual workspace behavior remains unverified.

## Use the outputs

After a successful test, later automation actions can select these values through the blue **+** mapping control:

| Output | Type | Meaning |
| --- | --- | --- |
| `projectId` | Text | The same saved image-project ID |
| `status` | Text | `queued`, `rendering`, `complete`, `error`, `canceled` or `draft` |
| `ready` | Boolean | True only for an enabled, complete project with an unexpired HTTPS download link |
| `downloadUrl` | Text | One exact signed URL, emitted only when `ready` is true |
| `expiresAt` | Text | That URL's API-provided expiration timestamp, emitted only when `ready` is true |

Use an already completed image for the first test so the URL outputs can be discovered. Add a conditional group that runs only when `ready` is true before using `downloadUrl`. For an **Update record** action, use the record ID from your trigger and map only your intended URL and expiration fields. A separate status update can use `status`; do not clear an existing output field merely because this lookup is not ready. No particular base schema is required or changed by the script.

For `queued` or `rendering`, this run ends without waiting. Check the same saved ID in a later run. For `error`, `canceled`, `draft`, a disabled project or an unavailable/expired link, do not use a download URL from this run. Inspect the original project before deciding what to do next. Network, HTTP and unexpected-response failures stop with fixed messages; private API response bodies and raw exceptions are not printed.

## Keep results private and recover the same job

The API key stays out of script outputs, but project IDs and signed download links are still private data. A signed URL can grant access to the media until it expires. Outputs may be visible in automation run history, downstream steps and any base fields you populate. Do not expose them in public views, shared templates, screenshots or logs. Review the permissions of every destination before mapping a result there.

This script retrieves metadata only. It does not verify or copy the media bytes, and the signed URL is not a permanent asset. If a lookup times out or a link expires, keep the original project ID and retrieve that same job again. Never create or recreate media to recover an uncertain lookup. Any later file-download step should use the URL exactly as returned without forwarding the Magic Hour Authorization header.

## Source contract and limits

The request is `GET https://api.magichour.ai/v1/image-projects/{id}` with Bearer authentication. The raw REST response uses `downloads[].expires_at`, not the SDK's camelCase `expiresAt`. See [Get image details](https://docs.magichour.ai/api-reference/image-projects/get-image-details) and the [official SDK source](https://github.com/magichourhq/magic-hour-node/blob/54fa009c1f6de34e37965bd30f7f6b70fa7ea8e6/src/types/v1-image-projects-get-response.ts).

Airtable's automation fetch has a 30-second timeout. Its overall script limit is currently temporarily 120 seconds; this example does not rely on that allowance to wait for a render. It uses one buffered metadata request and rejects redirects. See Airtable's [input](https://airtable.com/developers/scripting/api/input), [output](https://airtable.com/developers/scripting/api/output) and [fetch](https://airtable.com/developers/scripting/api/fetch) references.

This is a custom automation example, not an Airtable Marketplace listing or a verified native release.
