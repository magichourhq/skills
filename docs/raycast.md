# Use Magic Hour in Raycast AI

Connect Raycast AI to Magic Hour's hosted creation MCP to work with images, video and audio. No local Magic Hour server or API wrapper is required.

This setup follows Raycast's current documented HTTP and OAuth controls. Native installation, Magic Hour authorization and media retrieval in Raycast have **not yet been verified**. This is not a Raycast Store extension or an accepted Store listing.

## Connect the creation server

You need Raycast Pro on a supported desktop and a Magic Hour account. Raycast's AI usage and Magic Hour's generation credits are separate. Do not purchase a subscription or credits automatically.

1. Open **Manage MCP Servers** and check for an existing Magic Hour connection. Reuse it if it works.
2. If none exists, open **Install MCP Server**. Name it `magic-hour`, choose **HTTP**, and enter `https://mcp.magichour.ai/`.
3. Use **Dynamic** OAuth and follow Raycast's normal **Sign In** flow. Review the Magic Hour account and consent screen before allowing access. Do not put an API key in chat, a public issue or a committed configuration file.
4. Check the server's status and tool list in **Manage MCP Servers**. The separate `https://docs.magichour.ai/mcp` endpoint searches documentation; it does not create media.

If OAuth fails, retain the error for diagnosis without including tokens or account data. Do not replace the connection with a guessed client ID, callback URL or secret. A configured server or visible tool list is not proof of API authorization.

In AI Chat or Quick AI, select the `magic-hour` server from the `@` menu and ask:

> Use get_account_info to verify my Magic Hour access. Do not generate media or buy credits.

Check that the request is the account read you intended. Then recover an image you already created:

> Use get_image_project with this existing image project ID: <existing-project-id>. Show its current status and output. Do not create another project or regenerate it.

Replace the placeholder with your saved image project ID. Account access and existing-project recovery are separate checks. If you have no saved image, the recovery step remains unverified.

## Reuse your creative skills

If you already installed Magic Hour skills, keep that installation. Raycast scans `~/.agents/skills` and other supported folders. In **Settings → AI → Skills**, use **Skill Folders** to add an existing skills directory if needed; each skill must be one subfolder containing its `SKILL.md` and supporting files. Do not copy only the Markdown file and lose its references.

Choose a workflow from the [Magic Hour skill list](../README.md#choose-your-workflow). Confirm it appears in Raycast's Skills settings, then select it from the `@` menu in AI Chat or Quick AI. Raycast's AI Commands do not load skills. Skill installation and MCP authorization are separate.

With a photo you may use, the connection and a matching skill selected, ask:

> Animate this photo as a short impossible scene. Keep me recognizable, inspect the result and save the finished video. Use my existing spending limit, including repairs; if none is set, ask before generating. Do not buy credits. Keep the project ID and accepted files so we can continue without starting over.

Keep Raycast's normal tool permissions enabled and review paid creation requests before approving them. Raycast may approve read-only calls automatically under its normal policy. A timeout does not mean a creation failed: recover the **same project ID** before considering another paid request. Retrieve an existing project again if its download URL expires. Reuse accepted footage for edits that do not require generation.

See [first-run troubleshooting](quickstart.md#unstick-the-first-run), [Raycast MCP setup](https://manual.raycast.com/ai/model-context-protocol) and [Raycast skills](https://manual.raycast.com/ai/skills). A Store package is a later distribution step that requires a genuine publisher identity, supported-host verification and normal Raycast review.
