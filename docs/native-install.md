# Install the Magic Hour media plugin

The plugin packages the same `skills/` directory as the [individual skill installer](quickstart.md). Choose one installation method for a project to avoid loading duplicate copies. It does not install a second MCP server or replace an existing connection.

## Claude Code

Run in Claude Code:

```text
/plugin marketplace add magichourhq/skills
/plugin install magic-hour@magic-hour
```

Restart or reload plugins as your client requests. Ask:

> Use Magic Hour to turn this product photo into a finished image. Help me connect if needed, verify my account, and use my existing budget. Choose the creative details and deliver the actual file.

Plugin skills are namespaced. For an explicit invocation, use `/magic-hour:magic-hour-product-visuals`. Other skills follow the same `magic-hour:<skill-name>` format. [Claude Code's plugin reference](https://code.claude.com/docs/en/plugins-reference) describes discovery and invocation.

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

Install the individual skills today:

```sh
npx skills add magichourhq/skills --agent cursor
```

The repository also includes a Cursor plugin manifest for local plugin imports and marketplace submission. Follow [Cursor's local plugin instructions](https://cursor.com/docs/plugins) if you are developing or reviewing the package. Manifest availability does not mean it has been accepted into Cursor's marketplace; native Cursor loading still needs a client-level check.

## Connect once, then create

Installation makes instructions available; generation still needs an authenticated Magic Hour MCP or API connection. Follow [connect once](quickstart.md#connect-once), reuse an existing connection and verify `account_retrieve` before spending credits. Do not paste an API key into a public issue or commit it to a project. The plugin contains no credentials, install scripts or automatic generation jobs.

To update, use your client's plugin update/marketplace upgrade controls. If you installed individual skills, use the skills installer's update command instead. Keep the same installation method and retain your project's accepted references and editable source files.
