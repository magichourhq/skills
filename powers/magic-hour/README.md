# Magic Hour Power for Kiro

Create and edit images and video using Magic Hour's hosted MCP, with guidance for recovering accepted projects and retrieving their output. This Power adds no local server, adapter, scripts or dependencies.

**Draft package:** native import, activation, OAuth authorization, tool discovery and authenticated project retrieval have not yet been verified in Kiro. Registry submission and acceptance are separate release steps.

## Review locally

1. Check out the exact commit under review. In Kiro's Powers panel, choose **Add Custom Power**, then **Import power from a folder** and select this `powers/magic-hour` folder.
2. Confirm that Magic Hour and its media skill are discovered. Try a request such as “Use Magic Hour to retrieve my existing image project's result.”
3. Complete Kiro's normal authorization flow when requested. Kiro Web documents **Agent Config > Powers & MCP > Authorize**. Follow the actual consent screen and keep normal tool confirmations enabled.
4. Verify `account_retrieve`, then retrieve an existing project by its saved ID. These checks do not require a new generation. Record the client version and actual results before calling this a working integration.

The portable `mcp.json` declares only the HTTPS Streamable HTTP endpoint. OAuth discovery, consent and credential storage belong to the client. It contains no bearer token, API-key placeholder or custom OAuth configuration. Do not add secrets to the package or paste them into chat.

After authorization, ask for an image or video workflow within your existing Magic Hour credit budget. Installation is free; media generation uses account credits. A timeout or expired output link requires checking the existing project, not blindly repeating a paid creation.

### Kiro CLI

Kiro also supports installing a local Power without opening the IDE. From the root of the exact checkout under review, run:

```sh
kiro-cli powers install ./powers/magic-hour
```

Use Kiro's V3 agent harness for Power activation, for example `kiro-cli chat --v3`. V3 refers to the agent harness, not the CLI's version number. See Kiro's [CLI 2.25.0 release notes](https://kiro.dev/changelog/cli/2-25/) for local Power installation and its [CLI reference](https://kiro.dev/docs/reference/cli-commands/) for `--v3`.

Then perform the authorization and existing-project checks above. Magic Hour's native CLI import, activation, OAuth and authenticated retrieval remain unverified.

## Package

- `plugin.json`: Agent Plugins 1.0 metadata and activation keywords.
- `mcp.json`: the hosted Magic Hour MCP connection.
- `skills/magic-hour-media/SKILL.md`: current workflow discovery, budget and same-project recovery guidance.

The existing Cursor, Claude Code, Codex and Gemini CLI packages are separate. This folder does not change their configuration. See [Kiro's creation guide](https://kiro.dev/docs/powers/create/) and [Power authentication](https://kiro.dev/docs/web/sandbox/mcp/#power-authentication-oauth) for the supported client flows.

## Privacy, support and license

- [Magic Hour Privacy Policy](https://magichour.ai/privacy-policy)
- Support: [support@magichour.ai](mailto:support@magichour.ai)
- License: [MIT](LICENSE)

Submit to the Kiro registry only after native verification and the required publisher review. This source package does not establish registry approval.
