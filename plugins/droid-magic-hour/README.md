# Magic Hour for Factory Droid

Draft plugin source for creating, editing and recovering media through the hosted Magic Hour MCP server. Native installation, OAuth, skill discovery and protected tool execution have not been verified. This is not a Factory-managed connector or an official Factory catalog listing.

The repository's `.factory-plugin/marketplace.json` points to this self-contained folder. Its MCP entry uses Droid's `http` transport and normal client-managed OAuth. It contains no API key, authorization header, OAuth override, command, hook or dependency installer. Existing Claude Code, Cursor, Gemini and Kiro configuration is separate.

## Review the draft

Use a supported Factory Droid client and normal Factory account access. Obtain a clean checkout of this PR branch, then run from the repository root:

```sh
droid plugin marketplace add .
droid plugin marketplace list
```

Read the registered marketplace name from that output. Factory derives it from the source, so it may differ from the manifest name and changes for pinned sources. Run `droid plugin install` with the identifier `magic-hour@` followed by that exact registered name and `--scope user`. Do not install the plugin folder directly as a marketplace.

Open `/plugins` to confirm the plugin is installed and enabled. In `/mcp`, find its Magic Hour server, follow browser sign-in and consent, and inspect the available tools. Preserve normal trust and tool confirmations. Droid stores OAuth state in its system keyring or supported fallback; do not copy credential files or paste tokens into chat.

First verify `account_retrieve`, returning only tier and available credits. Then request recovery of one existing completed image or video using its actual project ID. Check returned status and output; discovery or a Connected badge alone is insufficient. This read-only verification does not authorize generation, upload or deletion. Real creation remains subject to the user's explicit request, budget and input rights.

A passing release needs clean-checkout installation, skill activation, OAuth, account access, same-project recovery and usable output in the native client. Until those are verified, keep this draft and do not claim a supported native release or submit it to another catalog.

- [Factory plugins](https://docs.factory.com/harness/plugins)
- [Factory MCP and OAuth](https://docs.factory.com/harness/mcp)
- [Magic Hour API](https://docs.magichour.ai/)
- [Privacy](https://magichour.ai/privacy-policy)
- [Support](https://help.magichour.ai/en/)
