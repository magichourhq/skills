# Recover a Magic Hour image in Bubble

Source-reviewed setup guide. Bubble credential storage, initialization, workflow execution and a Magic Hour marketplace plugin are not yet verified.

Use Bubble's existing **API Connector** to retrieve an image project already owned by your Magic Hour account. No custom plugin, import file or local server is required. Start in an authorized private development app with your Magic Hour API key and a known completed image project ID.

## Keep the credential on Bubble's server

1. Open the **API Connector** tab in Bubble's editor. Reuse an existing suitable Magic Hour collection and call before adding another. Otherwise, use **+ New** to create a collection named `Magic Hour`.
2. In the collection's **Authentication** settings, select **Private key in header** and set **Key name** to `Authorization`.
3. In the protected **Private key** field, enter `Bearer`, one space, then your actual Magic Hour API key. If you use Bubble's optional **Development key value**, include the same prefix there and configure the credential appropriate to that environment. Bubble adds this header to collection calls automatically.

Keep the key in these native private authentication fields. Do not duplicate it as a public parameter, page input, custom state, URL or request body. Do not use **None or self-handled**, uncheck credential privacy or enable browser-side calls to get around an authentication problem. A saved collection is not proof that credentials are masked or protected in exports; verify those boundaries before sharing the app.

Restrict this credential-bearing collection to calls on `https://api.magichour.ai`. It sends the shared authorization header to every call in the collection. Do not use it for returned asset URLs or any other origin.

## Add one deliberate read

Add a call named `Get image project` with these settings:

| Setting | Value |
| --- | --- |
| Use as | **Action** |
| Method | **GET** |
| URL | `https://api.magichour.ai/v1/image-projects/YOUR_EXISTING_PROJECT_ID` |
| Request body | None |

Replace `YOUR_EXISTING_PROJECT_ID` in the URL with the exact ID from your own account. Keep the URL fixed for this first verification. Leave **Include errors in response & allow workflow actions to continue** off, and keep the call routed through Bubble's server.

Select **Initialize call** once. This sends a real GET to Magic Hour and reads its response; it is not a simulated result. It does not create media. Use the actual response to define fields, not a fabricated manual response. If initialization fails, inspect the credential and project ownership without adding a creation call.

Review the detected fields and save the initialized call. In a private development workflow, select your Magic Hour call under **API Connections** and add it to one button-click event. Trigger that button deliberately once. Do not attach the call to page load, a data source, a recurring event or a polling loop for this first check.

Initialization and that button click are two separate live reads. Record each execution separately; initialization is not a free preview or a substitute for the workflow run.

## Admit only a usable result

Verify the actual request returned HTTP `200`, then check the raw Magic Hour fields below. Bubble may display different mapped labels. Do not invent a response-body field for the HTTP status.

| Field | Required before forwarding media |
| --- | --- |
| `id` | Matches the existing project ID. |
| `enabled` | `true`. |
| `status` | `complete`. |
| `downloads[].url` | At least one returned HTTPS download. |
| `downloads[].expires_at` | The chosen download's timestamp is still in the future. |

Stop for disabled, queued, rendering, draft, error or canceled projects, unexpected IDs, missing downloads or expired links. HTTP success or a successful initialization alone does not establish usable media. A failed or unverified condition must not pass a link downstream.

Fetch the chosen signed link exactly as returned, including its query string. Do not send your Magic Hour authorization header to that asset URL. Save the actual media in suitable durable storage rather than embedding an expiring URL in published code. If retrieval times out or a link expires, read the same project ID again; do not generate a replacement.

The response, initialization view and workflow/debug history can contain private project data and signed links. Keep them private, inspect saved sample/default values before sharing or deploying, and do not export raw responses or credential-bearing configuration. Private header storage protects the credential; it does not authorize app users to retrieve arbitrary projects. A published app needs its own user-access checks and deliberate output mapping. This private setup does not configure another app or backend automatically.

Before adding creation later, agree on the tool, inputs and credit budget. Submit once, retain the accepted ID and reconcile uncertain acceptance before retrying. Bubble workload charges and Magic Hour generation charges are separate. No creation, public deployment or plugin submission is part of this verification.

See Bubble's [API Connector guide](https://manual.bubble.io/help-guides/integrations/api/the-api-connector), [authentication](https://manual.bubble.io/help-guides/integrations/api/the-api-connector/authentication), [call settings](https://manual.bubble.io/core-resources/api/the-api-connector/adding-calls) and [security guidance](https://manual.bubble.io/help-guides/security/api-security/api-connector-security), plus Magic Hour's [Get image details](https://docs.magichour.ai/api-reference/image-projects/get-image-details) reference.
