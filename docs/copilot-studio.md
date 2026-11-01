# Magic Hour MCP in Microsoft Copilot Studio

Source-reviewed setup guide for a private, unpublished agent using Copilot Studio's standard harness. Native connection, credential handling, authenticated tools and marketplace availability remain unverified. This is a native MCP connection, separate from the existing Power Platform REST connector, Microsoft Agent Framework SDK and GitHub Copilot setup.

You need an authorized Copilot Studio tenant/environment, maker access, a plan and capacity that support the MCP connector, and your own Magic Hour account/API key. A Teams-only plan does not provide all standalone connector capabilities. Tenant data policies can block the connection. Use existing authorized access; do not change tenant policies or purchase a plan to work around a missing option.

## Add the normal API-key connection

Magic Hour's hosted creation server uses Streamable HTTP at `https://mcp.magichour.ai/`. Copilot Studio supports this transport; do not substitute the deprecated SSE transport or guess a different path.

1. Open the agent's **Tools** page. Reuse a suitable existing Magic Hour connection first. Otherwise choose **Add a tool → New tool → Model Context Protocol**.
2. Set **Server name** to `Magic Hour`, **Server description** to `Retrieve existing Magic Hour media and inspect the connected account. Creation tools remain disabled for this verification.`, and **Server URL** to `https://mcp.magichour.ai/`.
3. Select **API key** authentication, type **Header**, with header name `Authorization`. Select **Create**.
4. In **Add tool**, choose **Create a new connection** or your existing authorized connection. In the native credential form, enter the word `Bearer`, one space, then your actual Magic Hour API key as the header's value. Keep it out of chat, descriptions, URLs, agent instructions and exported configuration.
5. Complete the normal connection and consent prompts, then select **Add to agent**. Keep this operator connection private. Do not share maker-provided credentials across users.

This uses the API-key authentication option documented by both services. Magic Hour also advertises OAuth discovery and dynamic registration, but its current source restricts OAuth callback URLs and does not include Microsoft's callback host. Copilot Studio OAuth interoperability is therefore not established. Do not select **None**, invent an OAuth client ID/secret, or change callback security to make this setup work. If the normal API-key form rejects the connection, stop at the exact error without exposing credentials.

## Enable only the two reads

Before any test conversation, open the Magic Hour server's settings under **Tools**. All MCP tools are enabled by default. Turn **Allow all** off, then leave only `get_account_info` and `get_image_project` on. Turn every other tool off, including creation, upload, deletion and wait tools. With **Allow all** off, newly added server tools stay off by default.

In **Details**, keep end-user authentication for the intended account and set **Ask the end user before running** to **Yes**. Preserve all native connection/tool confirmations. Verify the actual prompts rather than assuming that connecting, a read-only annotation or a successful sign-in supplies future spending approval. If the expected controls or tools are absent, do not start the test or bypass the tenant restriction.

## Verify reads before creating media

In the agent's private test pane, ask:

> Use only Magic Hour's get_account_info. Verify access and summarize the relevant credit balance. Do not create media or expose private account details.

Review the actual activity/trace, not just the agent's answer. It must show the intended successful tool call without an authentication or tool error. Connection status and tool discovery alone do not prove API access.

Then supply a known completed image project ID owned by the same Magic Hour account:

> Use only Magic Hour's get_image_project with id YOUR_EXISTING_PROJECT_ID. Retrieve that existing project once. Do not create, recreate, delete or modify media.

Check the actual result for the expected ID, `enabled: true`, `status: complete` and at least one HTTPS download whose `expires_at` is still in the future. Do not forward disabled, pending, failed, canceled, missing or expired output. A successful MCP transport response alone does not establish a usable project.

Keep account data, signed links and test/chat history private. Fetch an approved download exactly as returned without sending the API authorization header to the asset URL, then save the file in appropriate durable storage. For a timeout or expired link, retrieve the same project ID again. Do not create a replacement to recover a read or download.

Before enabling creation later, establish the tool, inputs, current price, credit balance and approved budget, including repairs. Submit once and retain the accepted project ID. Reconcile uncertain acceptance before retrying. Copilot Studio capacity charges are separate from Magic Hour generation credits. Publishing, tenant approval and per-user project authorization are separate release steps; this connection does not configure a published app's backend or grant users access to another account's projects.

See Microsoft's [MCP onboarding wizard](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent), [MCP tool selection](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-components-to-agent), [tool settings and confirmations](https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-tools-custom-agent) and [access requirements](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing-subscriptions), plus Magic Hour's [MCP guide](https://docs.magichour.ai/mcp).
