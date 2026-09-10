# Magic Hour skills

Installable agent skills for creating production-ready images, video, and audio with [Magic Hour](https://magichour.ai). Each skill encodes a concrete workflow, quality checks, and safe handling for paid asynchronous generations.

## Install

Install the full cookbook:

```sh
npx skills add magichourhq/skills --all
```

Or install one workflow:

```sh
npx skills add magichourhq/skills --skill magic-hour-image-to-video
```

These skills work with the hosted Magic Hour creation MCP at `https://mcp.magichour.ai/` or the [Magic Hour API](https://docs.magichour.ai/api-reference). Generation consumes Magic Hour credits.

## Cookbook

| Skill | Use it for | Why it exists |
| --- | --- | --- |
| [`magic-hour-media`](skills/magic-hour-media) | General image, video, and audio creation or project recovery | Routes a request to the right Magic Hour tool and carries it through completion, inspection, and delivery. |
| [`magic-hour-image-to-video`](skills/magic-hour-image-to-video) | Product shots, characters, ads, and hero visuals that need controlled animation | Builds or edits the start frame first, fixes visual problems while they are still cheap to fix, then prompts primarily for motion. |
| [`magic-hour-talking-media`](skills/magic-hour-talking-media) | Talking portraits and lip-syncing existing video | Chooses the correct workflow, prepares compatible inputs, and checks mouth timing, identity, audio, and frame stability. |

The focused skills are deliberately narrow. Install `magic-hour-media` for broad requests and add a focused skill when that workflow is common in your work.

## Validation

We publish the proof boundary rather than treating a schema check as a successful generation.

| Workflow | Evidence as of September 10, 2026 |
| --- | --- |
| General media | Skill structure validated, public installation tested from an exact Git commit, current MCP tool names checked against live discovery, and a signed-in Magic Hour image generation completed and downloaded. Direct creation through the hosted MCP remains a separate integration check. |
| Image to video | Real Magic Hour API runs completed an image generation, an image edit, and a one-second image-to-video generation that produced a playable H.264 MP4. The exact editor-output-to-video chain has been contract-checked; the three paid steps were not submitted as a single run. |
| Talking media | Signed-in Magic Hour Talking Photo and Lip Sync runs completed and downloaded during revenue-path QA. Current MCP operation names and request schemas are checked against the maintained OpenAPI contract. |

All three skills also enforce the same operational invariants: one creation request per intended job, persisted project IDs, retrieval instead of duplicate paid retries, exact signed download URLs, and output review before a result is called complete.

## Contributing

Add a skill only when it owns a distinct user job and has evidence beyond plausible prompt advice. Keep current model lists and pricing out of skill text; agents should read live schemas because those values change.

## License

[MIT](LICENSE)
