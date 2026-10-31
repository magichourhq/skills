# Magic Hour in Replit Agent

Source-reviewed setup draft. Native Replit compatibility, authenticated tool calls and a curated Replit listing are not yet verified.

Connect Replit Agent to Magic Hour's hosted creation MCP to create or retrieve media while building. You need a Replit account and a Magic Hour account. No local Magic Hour server or adapter is required.

## Connect once

Reuse an existing Magic Hour connection before adding another.

[Add Magic Hour to Replit](https://replit.com/integrations?mcp=eyJkaXNwbGF5TmFtZSI6Ik1hZ2ljIEhvdXIiLCJiYXNlVXJsIjoiaHR0cHM6Ly9tY3AubWFnaWNob3VyLmFpLyJ9)

This link contains only the display name `Magic Hour` and endpoint `https://mcp.magichour.ai/`. It contains no credentials. Review the endpoint and complete Replit's normal connection and Magic Hour authorization prompts.

To configure it manually:

1. Open Replit's **MCP Servers** settings pane and choose **+ Add MCP server**.
2. Set the display name to `Magic Hour` and the HTTPS URL to `https://mcp.magichour.ai/`.
3. Leave custom headers empty for this OAuth setup, then select **Test & save**. Complete the authorization flow if prompted and review the requested access.
4. Check the saved connection's status and tools. Keep normal tool confirmations enabled. If authentication or Replit's security scanner rejects the connection or a tool, stop at that step rather than bypassing it.

Replit also supports custom authentication headers through **Advanced settings**. Do not put credentials in an install link, chat message or committed configuration. This guide uses the normal OAuth path rather than supplying a bearer key.

## Add the existing media skill

In Agent, select **+ → Use a skill**, paste this public folder URL, then choose **Preview skills**:

```text
https://github.com/magichourhq/skills/tree/main/skills/magic-hour-media
```

Review the detected skill and choose **Import**. Reuse it if already installed. Replit's preview checks file structure; it does not verify the instructions or connect the MCP server. The [media skill](../skills/magic-hour-media/SKILL.md) supplies workflow guidance; authentication is separate.

## Verify reads before spending

First ask Agent:

> Use only Magic Hour's get_account_info to verify access. Show the relevant credit balance, without creating media or exposing private account details.

Then provide one existing completed image project ID from your own account:

> Use Magic Hour's get_image_project with id YOUR_EXISTING_PROJECT_ID. Retrieve this existing project only. Do not create or recreate media.

Approve only the intended read operations. Tool discovery alone does not prove authenticated access or a usable output.

Before creating media, establish the tool, inputs and an approved credit budget, including repairs. Submit once and retain the accepted project ID. If submission times out without an ID, reconcile the original request before retrying. If polling or downloading fails, retrieve the same project; do not create another paid job to recover it.

For an asset used in an app, save and inspect the completed file in the project or durable storage. Do not embed an expiring signed download URL in production code. This MCP connection equips Replit Agent; it does not automatically configure the published app's backend. A backend calling Magic Hour needs its own server-side API integration and private secrets.

See Replit's [connection guide](https://docs.replit.com/build/connect-via-mcp), [install-link contract](https://docs.replit.com/features/mcp/overview#share-your-own-install-link) and [Agent Skills guide](https://docs.replit.com/features/agent/skills), plus Magic Hour's [workflow guidance](workflow-guide.md).
