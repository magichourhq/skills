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
| [`magic-hour-product-visuals`](skills/magic-hour-product-visuals) | Product shots, hero images, packaging visuals, and ad creative | Turns placement, geometry, branding, and rejection criteria into a production brief, then checks the finished image. |
| [`magic-hour-image-to-video`](skills/magic-hour-image-to-video) | Product shots, characters, ads, and hero visuals that need controlled animation | Builds or edits the start frame first, fixes visual problems while they are still cheap to fix, then prompts primarily for motion. |

The focused skills are deliberately narrow. Install `magic-hour-media` for broad requests and add a focused skill when that workflow is common in your work.

## Validation

We publish the proof boundary rather than treating a schema check as a successful generation.

| Workflow | Evidence as of September 10, 2026 |
| --- | --- |
| General media | Skill structure validated, public installation tested from an exact Git commit, current MCP tool names checked against live discovery, and a signed-in Magic Hour image generation completed and downloaded. Direct creation through the hosted MCP remains a separate integration check. |
| Product visuals | In a matched signed-in comparison using Z-Image Turbo, 640px, 16:9, and one image, the brief generic prompt centered the bottle and rendered its label ambiguously. The skill-guided brief produced the requested left-side negative space, one clearly legible `AURORA` label, stronger product geometry, and controlled lighting. |
| Image to video | In a matched signed-in comparison using LTX-2.5, 480p, 16:9, one second, and audio off, generic text-to-video duplicated the `AURORA` label and centered the product. The skill-guided start-frame workflow retained one correct label, intentional left-side negative space, stable bottle geometry, and a coherent dolly through the final frame. Earlier real API runs also completed image generation, image editing, and a playable H.264 image-to-video output. |

All three skills also enforce the same operational invariants: one creation request per intended job, persisted project IDs, retrieval instead of duplicate paid retries, exact signed download URLs, and output review before a result is called complete.

## Contributing

Add a skill only when it owns a distinct user job and has evidence beyond plausible prompt advice. Keep current model lists and pricing out of skill text; agents should read live schemas because those values change.

## License

[MIT](LICENSE)
