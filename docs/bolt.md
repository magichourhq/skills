# Read existing Magic Hour projects in Bolt.new

Prepare a private, read-only connection from Bolt's authoring assistant to Magic Hour's hosted MCP. Setup must stop at the authentication check below. This does not add Magic Hour authentication to your published app. Native authentication, tool filtering, retrieval and privacy behavior remain unverified.

## Add the private connection

Follow Bolt's [custom MCP connector instructions](https://support.bolt.new/integrations/mcp):

1. Open **+ → Connectors → Manage connectors → Custom MCP server**.
2. Enter name `Magic Hour`, URL `https://mcp.magichour.ai/`, transport **HTTP**, and select authentication **API key**. Do not enter a secret or submit the connection yet.
3. **Stop for a key-free form inspection.** Bolt's public instructions do not establish how this mode constructs its authorization header. Verify from the actual field labels/help and vendor documentation that it supports Magic Hour's required `Authorization: Bearer` authentication. Do not guess whether to enter a raw key, a prefixed value or a custom header. If the normal form cannot establish that contract, keep setup blocked without entering a key. Do not substitute OAuth.
4. Only after that contract is verified, use Bolt's native credential control with your [Magic Hour API key](https://magichour.ai/developer?tab=api-keys). Keep it out of chat and project source. Leave **Auto-enable for all projects** off, then connect.
5. Before using the connector, open **⋯ → Edit**. Deselect every tool except `get_account_info` and `get_image_project`, then **Save changes**. If you cannot restrict the available tools, stop before asking Bolt to use it.
6. Enable Magic Hour only in the intended private project through **+ → Connectors**.

Bolt's [connector overview](https://bolt.new/blog/introducing-connectors) explains that connections belong to your account. Tool selections apply across projects, while each project can enable or disable the connector. All tools initially start enabled. Prefer a new connection when no safe suitable existing one exists. Do not change a shared existing allowlist without checking its other projects. Keep creation, editing, deletion, upload and wait tools disabled for this check; a chat instruction alone is not that restriction.

Bolt documents API-key entry but not its exact HTTP authorization construction or credential storage/export guarantees. Magic Hour requires bearer authentication for manual-key clients. A connected status or public tool discovery is insufficient proof. See [Magic Hour MCP setup](https://docs.magichour.ai/integration/model-context-protocol).

## Verify the account, then read one existing image

After the authentication contract, connection and read-only allowlist are verified, use the private authoring chat:

```text
Call Magic Hour get_account_info once to confirm authenticated access. Do not
repeat the call or print account fields. Do not generate, edit, delete, upload,
download, or change my app. Report only whether the account read succeeded.
```

Proceed only after an actual successful authenticated account response. A health response or tool list is not authorization proof. Then use an image-project ID you already own:

```text
Call Magic Hour get_image_project once with id YOUR_EXISTING_IMAGE_PROJECT_ID.
Report only its matching id, status and enabled value. Do not create a replacement,
poll, download media, publish a link, or modify my app. Stop after this read.
```

Use the exact discovered names, including any prefix Bolt adds. These requests intend one account read and one project read; actual call counts must be verified from native tool activity. This guide's preparation made zero protected calls.

The [current image response](https://docs.magichour.ai/api-reference/image-projects/get-image-details) is ready only when its ID matches, `enabled` is `true`, and `status` is `complete`. Before separately using a returned `downloads` item, check that its exact `url` is HTTPS with a nonempty host, no embedded credentials or whitespace, and that `expires_at` is a valid future timestamp. Do not strip query parameters or append expiry metadata to the URL.

Account responses and project results are sent to Bolt. Treat them and signed download URLs as private, even when the assistant is asked not to repeat them. Do not put them in shared chats, committed code or a public app. Public-user account isolation needs a separate application design.

## Recover without another generation

An authentication error, incomplete result, timeout or expired link does not justify creation. Stop, retain the original ID, and resolve the connection or retrieve that same ID later. No automatic retry or polling is configured here.

Bolt automatically discovers newly published server tools. Recheck the allowlist after refreshing a connection or catalog changes; do not assume new tools remain disabled. Turn the connector off for projects that no longer need it. This guide does not establish OAuth compatibility, a marketplace listing, native secret redaction or a completed Bolt integration.
