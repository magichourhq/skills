# Magic Hour in Lovable chat

Source-reviewed setup draft. Native Lovable compatibility, authenticated tool calls and a prebuilt Lovable catalog listing are not yet verified.

Connect Lovable's project chat or Chats to Magic Hour's hosted creation MCP to create or retrieve media while building. You need a Lovable account and a Magic Hour account. Custom MCP connections are personal: other workspace members connect with their own accounts.

## Connect once

Reuse an existing Magic Hour chat connection before adding another.

1. Open **Connectors → Add custom → MCP server**. If your workspace has disabled custom MCP servers, resolve that permission through its administrator.
2. Enter `Magic Hour` as the server name. Keep **Direct connection** if the connection selector appears.
3. Enter `https://mcp.magichour.ai/` as the server URL. This is the creation endpoint; `https://docs.magichour.ai/mcp` searches documentation.
4. Keep **OAuth** selected and choose **Add & authorize**. Complete the normal Magic Hour sign-in and review the requested access before approving.
5. Check the saved connection and ask Lovable to use it. Review any normal tool confirmations and approve only the intended operations. If authorization or a tool fails, retain that failure as a connection gap; do not change permissions or authentication to bypass it.

Lovable also documents bearer-token and API-key authentication. This guide's OAuth setup needs no key in a URL, chat message, source file or published frontend. Keep any separately configured credential in the platform's supported authentication flow.

## Verify reads before spending

First ask:

> Use only Magic Hour's get_account_info to verify access. Show the relevant credit balance, without creating media or exposing private account details.

Then provide one existing completed image project ID from your account:

> Use Magic Hour's get_image_project with id YOUR_EXISTING_PROJECT_ID. Retrieve this existing project only. Do not create or recreate media.

Tool discovery alone does not prove authenticated access or a usable output. Keep the existing connection and use the [media workflow guidance](../skills/magic-hour-media/SKILL.md) for supported operations, quality review and recovery.

Before creating media, establish the tool, inputs and an approved credit budget, including repairs. Submit once and retain the accepted project ID. If submission times out without an ID, reconcile the original request before retrying. If polling or downloading fails, retrieve the same project; do not create another paid job to recover it. Save and inspect the completed media in durable storage before using it in an app; avoid expiring signed URLs in production code.

## Published app integration

The personal chat connection equips Lovable while it builds. It does not become part of a published app. Runtime media generation needs a separate server-side API integration and private credential storage.

If your app already sends a brief or form to an automation, preserve that route. The existing [product-image workflow](https://github.com/magichourhq/docs/blob/main/examples/distribution-workflows/product-image-workflow.md) describes that UI-to-automation handoff; this guide adds the personal chat connection without replacing it.

See Lovable's [custom MCP setup](https://docs.lovable.dev/integrations/custom-mcp) and [chat connector guide](https://docs.lovable.dev/integrations/chat-connectors).
