# Recover an existing Magic Hour image in Voiceflow

Use Voiceflow's native API Tool to inspect an image project you already created. This initial setup is for an authorized owner in a private editor project. It does not generate media, publish an agent, or connect each end user to their own Magic Hour account. Source reviewed; native setup, credential handling and retrieval remain unverified.

## Protect the connection

In the intended environment, open **Secrets → New secret**. Name it `MAGIC_HOUR_API_KEY`, enter your [Magic Hour API key](https://magichour.ai/developer?tab=api-keys), and choose **Restricted**, which cannot be revealed after creation. Do not put the key in ordinary variables, instructions, chat, screenshots or this guide.

Check the selected environment and ensure the secret has no **Missing value** warning. Values are environment-specific. A draft uses its Draft value when set, otherwise Default; live versions use Default. Publishing does not promote Draft into Default. A missing value can be sent as a literal placeholder and look like a normal authentication failure. Follow the current [Secrets documentation](https://www.voiceflow.com/docs/documentation/build/data/secrets).

This is a project credential, not a separate account for every caller. Keep editor access limited to authorized people. Duplicating within the same workspace copies Main secret values; cross-workspace copies and exports carry secret names only, according to Voiceflow. Inspect access and contents before sharing or copying. Secret storage does not make returned account data or signed media links public-safe.

## Configure the native request

From the tools CMS tab, create an [API Tool](https://www.voiceflow.com/docs/documentation/build/tools/api-tool) named **Get Magic Hour Image Project**. Describe it as retrieving an existing project without creating media.

| Setting | Value |
| --- | --- |
| Method | `GET` |
| URL | `https://api.magichour.ai/v1/image-projects/{project_id}` |
| Input variable | `project_id`: the exact existing image-project ID from your own Magic Hour account, not a URL |
| Authorization header | Type `Bearer `, then insert `MAGIC_HOUR_API_KEY` using the native `{` → **Secrets** picker |
| Accept header | `application/json` |
| Query parameters / body | None |

The single curly braces are Voiceflow's input syntax. Use the secret picker rather than treating the key as an input variable. The endpoint and raw fields below follow [Magic Hour's existing-image API](https://docs.magichour.ai/api-reference/image-projects/get-image-details).

## Run once in the private editor

Open **Run**, use **Variables** to enter the existing `project_id`, then execute the request once. This performs a real authenticated GET; it is not a preview. Inspect the response panel's HTTP status and JSON body privately. The preparation of this guide made **zero** protected GETs; the editor's actual request count, timeout and masking behavior still need native verification.

Do not attach this tool to an autonomous playbook, a repeated workflow, or a public agent for the initial check. Do not assume that one manual click proves a particular underlying request count.

Only use a returned link when **all** of these checks pass:

| Source | Required value |
| --- | --- |
| HTTP response status | `200` |
| JSON `id` | Matches the supplied project ID |
| JSON `enabled` | `true` |
| JSON `status` | `complete` |
| One item in JSON `downloads` | Its `url` is HTTPS with a nonempty host, no embedded credentials or whitespace; its `expires_at` is a valid future timestamp |

These are raw response-body fields, including `expires_at`, not SDK camelCase names. HTTP success alone does not mean the image is complete. Queued, rendering, draft, canceled, error, disabled, mismatched or expired results are not ready. Treat the full response and download URLs as private; do not paste them into public transcripts or publish them in an agent.

## Mapping and recovery limits

The initial check needs no downstream mapping. If you later add a private [workflow API step](https://www.voiceflow.com/docs/documentation/build/steps/api), it maps tool inputs and can capture a whole response or an object path into a variable. Verify its actual response shape before choosing paths. Keep async execution off when a later step depends on the result, and apply the readiness checks before forwarding any URL. Capturing fields alone does not enforce those checks; a shared or public workflow needs a separate account and output-permission design.

For the separate [independent API-execution endpoint](https://www.voiceflow.com/docs/api-reference/api-tool/execute-api-tool), Voiceflow documents one saved request, a limit of the tool timeout or 18 seconds, whichever is shorter, and `408` on timeout. Its HTTP `200` envelope is not the upstream status: that is `output.status`, with JSON in `output.body`. This guide does not use that endpoint or assume its deadline applies to editor Run. The editor documentation does not establish an exact timeout or retry count.

After a timeout or other failure, stop. Check the environment/secret and response status without sharing raw errors. Retain the same project ID; when a link expires, retrieve that ID again to obtain a current link. Never create a replacement project as a recovery step. Native retrieval, response capture, secret redaction, sharing behavior and any publication remain unverified.
