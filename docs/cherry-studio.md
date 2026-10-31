# Magic Hour in Cherry Studio

Draft: source-reviewed against Cherry Studio 2.1.10. Native installation, OAuth sign-in and tool calls have not been verified in Cherry Studio.

Connect Cherry Studio to Magic Hour's existing remote MCP server to use media tools from an Agent. You need a Magic Hour account and a tool-capable model configured in Cherry Studio. No local Magic Hour server or adapter is required.

## Connect once

1. Open **Settings → MCP → MCP Servers**. If Magic Hour is already connected, reuse that server.
2. Choose **Add → Import from JSON** and paste the contents of [`mcp.json`](../examples/cherry-studio/mcp.json). Review it before importing: Cherry Studio's import flow adds, trusts and starts the server.
3. Complete the normal Magic Hour authorization if Cherry Studio opens it. Review the requested access before approving. The configuration contains no API key or authorization header; Cherry Studio's client handles OAuth. If sign-in or connection fails, stop here rather than adding a key to the JSON.
4. Wait for the server to connect, then open its details and check the tools list.
5. Open **Work → Agent menu → Edit → MCP** and enable the existing Magic Hour server for the Agent you want to use. Reuse this connection for other Agents as needed.

For manual setup, choose **Quick Create**, set the name to `Magic Hour`, the type to **Streamable HTTP**, and the URL to `https://mcp.magichour.ai/`. Leave headers empty, save and enable the server. Keep the explicit transport type: URL auto-detection in 2.1.10 would otherwise select SSE for this root URL. Review any normal trust or authorization prompts.

## Check access before creating media

Keep tool approvals enabled. First ask the Agent:

> Use Magic Hour's get_account_info to show my account and credit balance. Do not create media.

Then provide the ID of an existing completed image project from your account:

> Use Magic Hour's get_image_project to retrieve this existing project: YOUR_EXISTING_PROJECT_ID. Do not create or recreate a project.

Approve only the intended read operations. Successful account access, project retrieval and a usable output link establish different parts of the connection; a visible tools list alone does not prove them.

Before approving a new creation, review the tool, inputs and credit cost. If a creation is accepted but its response or polling fails, recover the same project ID. Do not submit another creation to recover an uncertain result.

See [Magic Hour MCP](https://magichour.ai/mcp) and [Cherry Studio's MCP setup](https://docs.cherryai.com.cn/advanced-basic/extensions/mcp.md). This guide describes a custom connection, not a Cherry Studio catalog listing or verified native release.
