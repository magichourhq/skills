# Install Magic Hour skills and make your first useful asset

You need an agent that supports skills and a [Magic Hour account with an API key](https://magichour.ai/developer). Installation is free; media generation uses credits. No server hosting, code writing or repository clone is required.

## Let your agent handle setup

In Codex or Claude Code, paste the [setup request](../README.md#start-here). The agent can install skills and configure the connection when it has local command/configuration access. You handle account sign-in and any credential entry it cannot securely perform. This is assisted setup, not a claim that installation also signs you in.

The agent should detect its client, check whether Node.js/npm and the skills already exist, use the matching command below, and preserve other connections. If Node.js is missing, explain that prerequisite and use the client's permitted installation flow. If your credential is already in an authorized secret store or private local file, use the client's supported authentication mechanism without printing it. Otherwise guide you to the client's secure credential flow; never request the key in chat or store it in project files.

When setup succeeds, continue to your creative request. A session restart may be necessary for newly installed skills or tools. Do not repeat setup on each generation.

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

Attach a portrait or character image you are entitled to use, then paste:

> Turn this photo into a short scene with golden fish swimming through the air around me. Keep me recognizable. Choose the creative details, edit and inspect the still if needed, then animate it. Save and show the finished video. Use my existing spending limit; if I haven't set one, ask before generating. Do not buy credits.

No photo? Use this instead:

> Make a short vertical video of an elevator opening onto the moon. No specific identity is needed. Choose the direction and settings, leave time to see the reveal, inspect and save the video. Use my existing spending limit; if I haven't set one, ask before generating.

The agent should check `account_retrieve` before the first paid job. Tool discovery and even a successful `ping` can work with an invalid key; the account read checks actual API authorization. You are ready when you receive a usable file, not just an installation message or project ID. The agent should inspect the result and repair a specific failure within your authorized budget; it should stop and explain if further spending is not covered.

For example, **“Up to 300 credits for this job, including repairs; choose the creative details”** establishes a ceiling, not an instruction to spend it all. Use a limit appropriate to your account and requested media. If you want to approve each draft, say so; otherwise the agent should perform the creative checks you delegated and continue.

## Continue without starting over

> Reuse the accepted clip and brief from this project. Make only the requested change: a shorter vertical cut with this exact caption. Check whether local editing can do this without another generation. Keep the accepted files and save the new version separately.

Keep source files, accepted outputs and project IDs in the same project. Retain only useful identity, voice, copy and layout decisions; credentials never belong in that brief. For animation, edit the approved still first if needed, then animate it with a motion-focused prompt. A new caption or crop should not require regenerating accepted footage.

## Unstick the first run

| What happened                                           | Next action                                                                                                 |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Skill not listed                                        | Confirm the install directory and selected agent; start a fresh session there                               |
| Tools absent                                            | Check the creation endpoint, enable the server, restart the session                                         |
| Tools listed, but `ping` says `Authentication required` | The server is reachable; supply the credential in the agent's launch environment, then restart that session |
| `ping` works but generation is unauthorized             | Check the key in the agent's launch environment; ping alone does not authenticate                           |
| Insufficient credits or unavailable tier/model          | Choose a supported option within budget; do not upgrade automatically                                       |
| Local image path rejected                               | The agent must request an upload URL and PUT the bytes, then use `file_path`                                |
| Wait timed out                                          | Retrieve the same project ID; do not submit another paid job                                                |
| Download URL expired                                    | Retrieve the existing project for a fresh exact URL                                                         |
| Wrong size or distorted subject                         | Inspect the actual file; crop only if requirements survive, otherwise repair within budget                  |

For help, [open an issue](https://github.com/magichourhq/skills/issues) with your agent, skill, failed step, expected result and redacted error. Never include keys, private account data or signed URLs. To update one installed workflow, run e.g. `npx skills update magic-hour-image-editing`. `npx skills update` without names can update other installed skills too, so review its scope.
