# Magic Hour AI media skills

Create and edit images, animate approved references, make talking videos, and finish campaign assets from your AI agent. These skills use [Magic Hour's creation MCP](https://github.com/magichourhq/magic-hour-mcp) or [API](https://docs.magichour.ai/api-reference), with workflows for preserving identity, fixing failed outputs and reusing accepted work.

**Start with one useful asset.** Install the cookbook, [connect once](docs/quickstart.md#connect-once), then paste a starter below. Works with Codex, Claude Code and other agents supported by the skills installer. Skills are free to install; generation uses Magic Hour credits.

```sh
npx skills add magichourhq/skills
```

Choose your agent and desired skills in the installer. [Exact Codex/Claude Code commands, setup and troubleshooting →](docs/quickstart.md)

## Choose your workflow

Prefer a native plugin? See [Claude Code and Codex plugin installation, plus Cursor packaging](docs/native-install.md). The plugin uses the same skills and your existing Magic Hour connection.

| I want to…                                | Skill                                                                       | What it adds beyond a tool call                                                                  |
| ----------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Create or recover general media           | [magic-hour-media](skills/magic-hour-media)                                 | Select the operation, finish asynchronous jobs and retrieve files without duplicate paid retries |
| Make a product shot or website hero       | [magic-hour-product-visuals](skills/magic-hour-product-visuals)             | Preserve geometry and labels, plan copy space and inspect the delivered file                     |
| Edit an existing image                    | [magic-hour-image-editing](skills/magic-hour-image-editing)                 | Separate changes from protected details and recover from drift or wrong dimensions               |
| Animate an approved image                 | [magic-hour-image-to-video](skills/magic-hour-image-to-video)               | Fix the still before motion, control the camera and inspect temporal consistency                 |
| Finish an ad or matching campaign set     | [magic-hour-campaign-kit](skills/magic-hour-campaign-kit)                   | Reuse a brand reference, compose exact copy and deliver finished placements                      |
| Keep a character consistent across scenes | [magic-hour-character-consistency](skills/magic-hour-character-consistency) | Separate identity from pose/style references and review continuity across shots                  |
| Make a thumbnail or episode cover         | [magic-hour-thumbnails](skills/magic-hour-thumbnails)                       | Build a truthful visual hook, preserve references and judge readability at feed size             |
| Make a talking portrait or lip-sync clip  | [magic-hour-talking-video](skills/magic-hour-talking-video)                 | Approve speech first, match timing and caption the final cut                                     |
| Edit or repurpose existing footage        | [magic-hour-video-editing](skills/magic-hour-video-editing)                 | Choose generative edits versus precise local changes and preserve action/audio                   |

Install one: `npx skills add magichourhq/skills --skill magic-hour-image-editing`. Install all: `npx skills add magichourhq/skills --skill '*'`. Each skill works independently; you do not need the whole collection for a single job.

## Try a real job

Attach your source media and use the matching prompt. The agent should use the current tool schema and your existing budget, not ask you to fill in API parameters.

**Product photo → catalog image**

> Use magic-hour-image-editing to make this product photo a square catalog image on white. Preserve its shape, material and exact label. Verify the connection and cost of one image first. Once I authorize that cost, complete the edit, inspect the downloaded dimensions and identity, and save the result here. Ask before another paid attempt.

**Reference → edited still → video**

> Use magic-hour-image-to-video to make a product hero video from this reference. Keep the product on the right and the left third clear for copy. If needed, use AI Image Editor to fix the still before animating. Preserve the exact label and geometry. Use a locked camera with subtle light movement, no cuts or audio. Check the total still-plus-video cost against my budget, inspect the complete clip, and deliver the actual video.

**Recurring character → new scene**

> Use magic-hour-character-consistency with my approved character image. Make the next scene in the same series: the character tending a greenhouse. Keep identity, proportions and rendering style; change only the setting and pose. Compare the output with the original before any animation. Retain the accepted reference for the next episode.

**Speech + portrait → talking clip**

> Use magic-hour-talking-video with my portrait and recording. Preserve the full speech through the last word. Measure the audio first, choose a supported talking-photo interval, then inspect mouth timing and face stability. Add captions only after the clean video passes. Check the total cost before starting.

For covers, existing footage and assembled ads, open the matching skill above. [Workflow decisions and common questions →](docs/workflow-guide.md)

## Inspect the actual outputs

These are original Magic Hour web-app and authenticated MCP outputs plus a local finishing example. Every case links to inputs, exact prompts, settings and limitations.

| Approved product still                                                      | Edited catalog image                                                                           | Finished layout                                                                      |
| --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| ![Blue AURORA bottle with space for copy](examples/aurora/guided-image.png) | ![AURORA bottle edited onto a square white background](examples/aurora-edits/catalog-qwen.png) | ![Square AURORA ad with exact headline and CTA](examples/aurora-finished/poster.png) |
| [Image + motion comparison](examples/aurora)                                | [All five editing attempts](examples/aurora-edits)                                             | [MP4 + editable copy + render recipe](examples/aurora-finished)                      |

The guided video retains one readable label where the generic example duplicates it. Two editing attempts ignored the square setting; switching models corrected it. Two vertical edits still missed exact placement, which informed the separate layout step. Those failures are included, not discarded.

The [Nori character case](examples/nori-character) adds five real MCP outputs: an original robot and two paired scene comparisons. The shorter prompt preserved details better in the greenhouse; added identity instructions helped in the garden. All attempts, exact prompts and 45 charged credits are recorded, including the rejected output with extra scarf ends.

The finished ad has about one second of generated motion followed by a hold, six seconds total, and preserves the source watermark. It is a composition demonstration. The product cases use one synthetic product and the character case uses one robot; they do not establish general superiority. Thumbnail, talking-video and video-editing workflows have live tool/schema checks but still need published authenticated output comparisons. [Full evidence coverage →](docs/workflow-guide.md#what-evidence-is-published)

## Make the next job easier

Keep approved references, clean masters, exact copy, voice choices, project IDs and accepted layout decisions in your project. On the next job, ask the skill to reuse that work and change only what the new brief requires. A new headline, crop or download link should not require paying to recreate an accepted product. [Reusable brand reference →](skills/magic-hour-campaign-kit/references/brand-reference.md)

## Questions

**Do I need both a skill and MCP?** The skill provides workflow instructions. The MCP executes Magic Hour tools. Use the API instead if your project already integrates it. Installing a skill does not authenticate your account.

**Which model should I use?** Choose current supported settings for the task and budget. Model lists and pricing change; the agent reads live schemas. [Observed failures and routing decisions →](skills/magic-hour-campaign-kit/references/model-observations.md)

**Why create or edit an image before video?** It lets you correct identity, composition and label problems before paying for motion. The approved still becomes the video input. [Detailed decision guide →](docs/workflow-guide.md#should-i-use-text-to-video-or-image-to-video)

**Something failed?** Keep the project ID. A polling timeout or expired URL usually needs retrieval, not a duplicate generation. [Troubleshooting →](docs/quickstart.md#unstick-the-first-run)

## Contribute a useful workflow

Start with a distinct user job, a reproducible failure or an output that improves a real task. Include source provenance, settings, all attempts/costs, accepted and failed criteria, and honest validation limits. Keep skill instructions concise and self-contained. Do not add model-price catalogs or claim quality, citations or revenue results without evidence. [Report an issue](https://github.com/magichourhq/skills/issues).

## License

[MIT](LICENSE). Example provenance and any production limitations are recorded with each case.
