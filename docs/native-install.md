# Install the Magic Hour media plugin

The plugin packages the same `skills/` directory as the [individual skill installer](quickstart.md). Choose one installation method for a project to avoid loading duplicate copies. The Cursor and Gemini CLI packages also configure Magic Hour's hosted creation MCP; Claude Code and Codex continue to use the connection already configured in those clients.

## Claude Code

Run in Claude Code:

```text
/plugin marketplace add magichourhq/skills
/plugin install magic-hour@magic-hour
```

Restart or reload plugins as your client requests. Ask:

> Use Magic Hour to turn this portrait into an impossible scene and animate it. Help me connect if needed, verify my account, and use my existing budget. Choose the creative details, keep me recognizable and deliver the actual video.

Plugin skills are namespaced. For an explicit invocation, use `/magic-hour:magic-hour-image-to-video`. Other skills follow the same `magic-hour:<skill-name>` format. [Claude Code's plugin reference](https://code.claude.com/docs/en/plugins-reference) describes discovery and invocation.

## Codex

On a Codex CLI with `plugin marketplace` and `plugin add` support:

```sh
codex plugin marketplace add magichourhq/skills
codex plugin add magic-hour@magic-hour
```

Start a new session if the current session has not picked up the skills. Ask for a Magic Hour workflow in plain language. If your Codex version does not expose these plugin commands, use the supported skill installation path:

```sh
npx skills add magichourhq/skills --agent codex
```

## Cursor

Until the plugin is accepted into Cursor Marketplace, install the individual skills:

```sh
npx skills add magichourhq/skills --agent cursor
```

The repository also includes a Cursor plugin package for local review and marketplace submission. Follow [Cursor's local plugin instructions](https://cursor.com/docs/plugins) to place the repository at `~/.cursor/plugins/local/magic-hour` and reload Cursor. Open **Plugins → Configure**, then enter the key in **Magic Hour API key**. Cursor stores the value in plugin configuration and passes it as a bearer token to `https://mcp.magichour.ai/`; the key is not stored in this repository. Verify the connection with `account_retrieve` before spending credits.

Manifest availability does not mean the plugin has been accepted into Cursor Marketplace. Native loading still needs a client-level check before submission.

## Gemini CLI

The repository includes a Gemini CLI extension package for native review. It reuses the existing `skills/` directory and connects to Magic Hour's hosted creation MCP without a local server or additional adapter. Native installation, discovery of all 20 bundled skills, sensitive-setting storage and reload, authenticated account access and saved-image recovery were verified with Gemini CLI 0.66.0 on Linux ARM64. Gallery listing is a separate release step.

Review an exact commit before installing it:

```sh
gemini extensions install https://github.com/magichourhq/skills --ref <reviewed-commit>
```

Replace `<reviewed-commit>` with the commit being reviewed. Follow Gemini CLI's normal extension and MCP consent prompts. Enter your key only in the **Magic Hour API key** sensitive-setting prompt, never in chat or a command argument. The manifest declares `MAGIC_HOUR_API_KEY` so Gemini CLI can pass it to the hosted connection. A working Gemini CLI model sign-in is separate from your Magic Hour API key.

Start a new session, inspect `/extensions list` and `/mcp`, then ask for `get_account_info` to verify API access without generating media. Next, retrieve a saved project by its existing ID before trying a paid workflow. Keep normal tool confirmations enabled. If a connection named `magic-hour` already exists in your Gemini settings, that configuration takes precedence; reuse the working connection rather than registering a duplicate.

To replace the stored setting, use `gemini extensions config magic-hour`. See the official [extension reference](https://geminicli.com/docs/extensions/reference/) and [publishing guide](https://geminicli.com/docs/extensions/releasing/). Direct installation and gallery acceptance are separate release steps.

## Connect once, then create

Installation makes instructions available; generation still needs an authenticated Magic Hour MCP or API connection. Cursor plugin users configure the included hosted connection as described above. In other clients, follow [connect once](quickstart.md#connect-once), reuse an existing connection and verify `account_retrieve` before spending credits. Do not paste an API key into a public issue or commit it to a project. The plugin contains no credentials, install scripts or automatic generation jobs.

To update, use your client's plugin update/marketplace upgrade controls. If you installed individual skills, use the skills installer's update command instead. Keep the same installation method and retain your project's accepted references and editable source files.
