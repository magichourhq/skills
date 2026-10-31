# Use Magic Hour in OpenCode

Connect OpenCode to Magic Hour's hosted creation MCP, then install a workflow for the media you want to make. No local Magic Hour server or adapter is required.

This guide targets **OpenCode 2.2.5**, distributed as `@opencode/cli`. Its configuration has been checked against the released source. Native installation, authenticated access and media execution in OpenCode have not yet been verified.

## Check your version

```sh
opencode --version
```

OpenCode 1, distributed as `opencode-ai`, uses a different configuration format. Do not paste this V2 example into V1 settings. Follow the [official V2 installation](https://opencode.ai/v2/docs/) or [migration guide](https://opencode.ai/v2/docs/migrate-v1/) if needed.

## Connect the creation MCP

Get an API key from [Magic Hour Developer](https://magichour.ai/developer?tab=api-keys). Make `MAGIC_HOUR_API_KEY` available securely in the environment that launches OpenCode. Never paste the key into chat, a command argument or a committed file. An already-running app does not automatically inherit a variable set in another terminal. See the [setup guidance](quickstart.md#connect-once) and [security policy](../SECURITY.md).

Merge the [V2 example](../examples/opencode/opencode.json) into your project's `opencode.json` or `opencode.jsonc`. Preserve existing settings and connections. If you already have a working `magic-hour` connection, reuse it rather than adding another.

The example connects to `https://mcp.magichour.ai/`, passes a bearer-token environment reference, and disables OAuth for this API-key route. The docs MCP at `https://docs.magichour.ai/mcp` searches documentation and does not create media.

It sets `codemode: false` to expose Magic Hour's tools directly and an `ask` permission for `magic-hour_*` so each tool call needs approval. Preserve those confirmations. Permission rules are ordered; later matching agent or session rules and previously saved approvals can affect the result. Review your effective permissions and choose **Allow once**, not **Allow always**, for a single call. Do not use `--auto` or `--dangerously-skip-permissions` for this setup.

Start a fresh OpenCode session from the configured project and environment, then check the connection:

```sh
opencode mcp list
```

Use `/mcps` in the interactive client to inspect the server. A connected status or visible tool list establishes discovery, not API-key validity. Ask:

> Use Magic Hour's get_account_info to verify this connection. Do not generate media or buy credits. Keep tool confirmations enabled.

Approve only the account-read request. Next, recover an image you already created:

> Use Magic Hour's get_image_project with this existing image project ID: <existing-project-id>. Retrieve its current status and output. Do not create another project or regenerate it.

Replace the placeholder with your actual saved image project ID. A successful account read verifies API access; a successful existing-project read verifies recovery without a paid creation. If no saved project is available, the recovery step remains unverified.

## Install a creative workflow

From the same project:

```sh
npx skills add magichourhq/skills --skill magic-hour-image-to-video --agent opencode
```

The skills installer supports OpenCode and installs project skills under `.agents/skills`, which OpenCode V2 discovers. Start a new session after installation. To invoke this workflow explicitly, mention `@magic-hour-image-to-video`. For another job, choose its exact skill name from the [workflow list](../README.md#choose-your-workflow). Installing instructions does not authenticate your account or spend credits.

## Create within your budget, then reuse the result

Attach a photo you may use and ask:

> Use @magic-hour-image-to-video to animate this photo. Keep me recognizable, inspect the result and save the finished video. Use my existing spending limit, including repairs; if none is set, ask before generating. Do not buy credits. Keep the project ID and accepted files so we can continue without starting over.

Review the tool and its arguments before approving a paid call. Keep normal confirmations enabled for generation and repairs. For a timeout or expired download link, retrieve the **same project ID** for its status or a fresh output URL. Do not repeat a paid creation when acceptance is uncertain. Reuse accepted footage for local crops, captions or other changes that do not need generation.

See [first-run troubleshooting](quickstart.md#unstick-the-first-run) and [workflow guidance](workflow-guide.md) for uploads, model availability, budgets and output review.
