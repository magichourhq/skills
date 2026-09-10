# Install Magic Hour skills and make your first useful asset

You need an agent that supports skills, Node.js/npm for `npx`, and a Magic Hour account with an API key and enough credits for the requested generation. Skill installation is free; generation is billed by Magic Hour. No server hosting or repository clone is required.

## Install for your agent

Run from the project where you want to create media. Choose **one** command:

```sh
# Codex
npx skills add magichourhq/skills --skill '*' --agent codex

# Claude Code
npx skills add magichourhq/skills --skill '*' --agent claude-code
```

For another supported agent, run `npx skills add magichourhq/skills` and select it. To install just one workflow, replace `'*'` with its exact skill name from the [cookbook](../README.md#choose-your-workflow). Start a new agent session after installation.

## Connect once

Already using the Magic Hour creation MCP? Keep that connection and skip to the first-result prompt. The creation endpoint is `https://mcp.magichour.ai/`. The docs endpoint, `https://docs.magichour.ai/mcp`, only searches documentation.

Get your key from [Magic Hour Developer](https://magichour.ai/developer). Keep it out of chat and committed files. Set `MAGIC_HOUR_API_KEY` securely in the environment that launches your agent. A terminal variable is not automatically available to an already-running desktop app.

**Codex CLI**, from that same environment:

```sh
codex mcp add magic-hour --url https://mcp.magichour.ai/ --bearer-token-env-var MAGIC_HOUR_API_KEY
```

**Claude Code**, from that same environment:

```sh
claude mcp add --transport http --scope user magic-hour https://mcp.magichour.ai/ --header 'Authorization: Bearer ${MAGIC_HOUR_API_KEY}'
```

The single quotes retain a variable reference rather than placing the key in the command. Claude Code supports [environment expansion in MCP headers](https://code.claude.com/docs/en/mcp#environment-variable-expansion-in-mcpjson). If you already have a server named `magic-hour`, inspect it rather than adding a second connection.

For **Claude's custom connector**, use the [maintained connection guide](https://github.com/magichourhq/magic-hour-mcp/blob/main/user.md#connect-with-claude), including OAuth client ID `magic-hour-mcp`. Connector setup and skill installation are separate; use your client's supported skill installation flow. For an existing API integration, keep the official [Python](https://github.com/magichourhq/magic-hour-python) or [Node](https://github.com/magichourhq/magic-hour-node) SDK and the [API quick start](https://docs.magichour.ai/get-started/quick-start).

## Make one useful result

Attach a product photo you are entitled to use, then paste:

> Use magic-hour-image-editing to make this product photo a square catalog image on white. Preserve its actual shape, material, cap and exact label. First verify the Magic Hour connection and authenticated account eligibility. Tell me the cost of one suitable image before generating; do not buy credits. Once I authorize that cost, complete the edit, inspect its actual dimensions and identity, save the image to this project, and show it. Ask before another paid attempt.

No photo? Use this instead:

> Use magic-hour-product-visuals to create one 16:9 hero image of an original cobalt-blue perfume bottle labeled AURORA on wet stone, product on the right and left third clear for my headline. This is a fictional product. Check connection, account eligibility and the cost of one image first. Once I authorize that cost, generate, inspect and save the actual output. Ask before a paid retry.

Connection success means `ping` returns `pong`; authenticated readiness requires an account read. Activation means you receive and accept a usable file. Installation, authentication and a queued project ID are intermediate steps. If the first result fails a requirement, keep its project ID and explain the failure before spending again.

## Continue without starting over

> Reuse the accepted source and brief from this project. Make only the requested change: a vertical version with the product below my headline. Reuse the original logo and exact copy. Check whether local layout can do this before another paid edit. Keep the existing accepted files and save the new version separately.

Keep source files, accepted outputs and project IDs in the same project. Retain only useful identity, voice, copy and layout decisions; credentials never belong in that brief. For animation, edit the approved still first if needed, then animate it with a motion-focused prompt. A new headline or crop should not require rebuilding the product.

## Unstick the first run

| What happened | Next action |
| --- | --- |
| Skill not listed | Confirm the install directory and selected agent; start a fresh session there |
| Tools absent | Check the creation endpoint, enable the server, restart the session |
| `ping` works but generation is unauthorized | Check the key in the agent's launch environment; ping alone does not authenticate |
| Insufficient credits or unavailable tier/model | Choose a supported option within budget; do not upgrade automatically |
| Local image path rejected | The agent must request an upload URL and PUT the bytes, then use `file_path` |
| Wait timed out | Retrieve the same project ID; do not submit another paid job |
| Download URL expired | Retrieve the existing project for a fresh exact URL |
| Wrong size or distorted subject | Inspect the actual file; crop only if requirements survive, otherwise repair within budget |

For help, [open an issue](https://github.com/magichourhq/skills/issues) with your agent, skill, failed step, expected result and redacted error. Never include keys, private account data or signed URLs. To update one installed workflow, run e.g. `npx skills update magic-hour-image-editing`. `npx skills update` without names can update other installed skills too, so review its scope.
