# Magic Hour AI media skills

Turn a product photo into an ad, an illustration into a video, or a portrait and recording into a talking clip. Tell your AI agent what you want; these skills guide the creative decisions, run [Magic Hour's creation MCP](https://github.com/magichourhq/magic-hour-mcp) or [API](https://docs.magichour.ai/api-reference), inspect the result and save files you can reuse.

[See actual outputs and reproducible examples](docs/evidence.md) · [Explore advanced recipes](#go-further) · [Get your first result](docs/quickstart.md)

## Start here

**New to skills? Paste this into Codex or Claude Code:**

> Set up the official Magic Hour skills from https://github.com/magichourhq/skills for this project and connect the Magic Hour creation MCP. Reuse any existing connection. Handle the installation and configuration you can access; guide me through only the sign-in or secure credential step that needs me. Never ask me to paste a key into chat. Verify the connection with an authenticated account read. Then help me make one useful asset from my brief; use my existing budget or ask for a spending limit before generating.

Your agent needs permission to run local commands. You need a [Magic Hour account and API key](https://magichour.ai/developer); no code writing, server hosting or repository clone is required. Skills are free to install; generation uses credits. [Step-by-step setup and supported clients →](docs/quickstart.md)

**Prefer the install command?**

```sh
npx skills add magichourhq/skills
```

Choose your agent and desired skills. Already connected and installed? Attach a photo and ask: **“Make this a clean square product photo for my store. Keep the actual product and label. Choose the creative details and show me the finished image.”** No model names or API parameters needed.

## Choose your workflow

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

> Make this product photo a square catalog image on white. Preserve its shape, material and exact label. Choose the settings, inspect the result and save the image here. Work within my existing budget; ask for a limit only if I haven't set one.

**Reference → edited still → video**

> Turn this reference into a product hero video. Keep the product on the right and the left third clear for copy. Fix and inspect the still with AI Image Editor before animating if needed. Preserve the exact label and geometry. Use a locked camera with subtle light movement, no cuts or audio. Choose the creative details, work within my budget and deliver the inspected video.

**Recurring character → new scene**

> Make the next scene in this character's series: tending a greenhouse. Keep the identity, proportions and rendering style of my approved image; change only the setting and pose. Choose the composition and compare the output with the original before any animation. Keep the accepted reference for the next episode.

**Speech + portrait → talking clip**

> Make a talking clip from my portrait and recording, with captions. Keep the full speech through the last word. Handle timing, check the face and mouth movement, then caption the final cut. Save both clean and captioned versions. Include both steps in my budget.

The agent should carry each request through to the file, make delegated creative choices and explain any failed requirement. It should reuse your budget and accepted work instead of repeatedly asking the same questions.

## Go further

These are instructions for real jobs, with inputs, creative decisions, recovery steps and deliverables. Each installs with its skill; you don't need to read them before asking for the result.

| Job                                                             | Recipe                                                                                                                                                     |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Catalog, lifestyle, close-up and hero images from one product   | [Reference photoshoot](skills/magic-hour-product-visuals/references/photoshoot.md)                                                                         |
| Background changes, relighting and difficult reframing          | [Faithful image edits](skills/magic-hour-image-editing/references/faithful-edits.md)                                                                       |
| A short film with coherent shots and motion                     | [Multi-shot direction](skills/magic-hour-image-to-video/references/multi-shot.md)                                                                          |
| A recurring cast, new angles and continuity at cuts             | [Characters across a series](skills/magic-hour-character-consistency/references/series.md)                                                                 |
| A readable cover with editable headline and deliberate variants | [Thumbnail direction](skills/magic-hour-thumbnails/references/cover-design.md)                                                                             |
| Presenter series, pronunciation and language versions           | [Speech and localization](skills/magic-hour-talking-video/references/localization.md)                                                                      |
| Turn existing footage into multiple finished placements         | [Repurpose a master](skills/magic-hour-video-editing/references/repurpose.md)                                                                              |
| Exact copy, finished ads and next month's campaign              | [Finishing](skills/magic-hour-campaign-kit/references/finishing.md) · [Reusable brand brief](skills/magic-hour-campaign-kit/references/brand-reference.md) |

[Answers to common media-generation questions →](docs/workflow-guide.md) · [What we have actually verified →](docs/evidence.md)

## Inspect the actual outputs

These are original Magic Hour web-app and authenticated MCP outputs plus a local finishing example. Every case links to inputs, exact prompts, settings and limitations.

| Approved product still                                                      | Edited catalog image                                                                           | Finished layout                                                                      |
| --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| ![Blue AURORA bottle with space for copy](examples/aurora/guided-image.png) | ![AURORA bottle edited onto a square white background](examples/aurora-edits/catalog-qwen.png) | ![Square AURORA ad with exact headline and CTA](examples/aurora-finished/poster.png) |
| [Image + motion comparison](examples/aurora)                                | [All five editing attempts](examples/aurora-edits)                                             | [MP4 + editable copy + render recipe](examples/aurora-finished)                      |

The guided video retains one readable label where the generic example duplicates it. Two editing attempts ignored the square setting; switching models corrected it. Two vertical edits still missed exact placement, which informed the separate layout step. Those failures are included, not discarded.

The [Nori character case](examples/nori-character) adds five real MCP outputs: an original robot and two paired scene comparisons. The shorter prompt preserved details better in the greenhouse; added identity instructions helped in the garden. All attempts, exact prompts and 45 charged credits are recorded, including the rejected output with extra scarf ends.

The [Nori thumbnail case](examples/nori-thumbnail) adds two authenticated MCP edits, an editable headline and full-size/small previews. The direct version adds unrequested text and miniature scenes; the finished version uses one large subject. Both attempts and their 200-credit cost are included. Audience response is unmeasured.

The finished ad has about one second of generated motion followed by a hold, six seconds total, and preserves the source watermark. It is a composition demonstration. The cases use one synthetic product and one robot; they do not establish general superiority. Talking-video and generative video-editing quality still need published authenticated comparisons. [Full evidence coverage and citation guidance →](docs/evidence.md)

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
