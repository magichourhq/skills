# Magic Hour skills: output evidence and reproducible examples

Maintained by Magic Hour. Last updated: **2026-09-11 UTC**. This page separates completed output cases from instructions that still need published quality validation. Installing a skill, authenticating an account and completing a job are different from producing an accepted asset.

## What has actually been generated and inspected?

| Case                                      | Inspect and reproduce                                                                       | What the case supports                                                                              | Limit                                                                                                   |
| ----------------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Personal image → scene → motion           | [Midnight remix inputs, export and all requests](../examples/midnight-remix)                | The edited portrait stays recognizable through a generated reaction in a new setting                | Head turns and final pose miss strict motion direction; frame review does not prove temporal smoothness |
| Face swap and whole-character replacement | [Original performance, alternate face, fox and both outputs](../examples/midnight-remix)    | Distinct operations change the face or whole character using the same source performance            | One subject; output size and timing change; no multi-person or animate-mode validation                  |
| Idea → impossible reveal                  | [Moon-elevator prompt and MP4](../examples/midnight-remix)                                  | Text-to-Video creates the requested setup and reveal                                                | Unwanted numerals and camera movement remain                                                            |
| Talking Photo, Lip Sync and Video Editor  | [Speech, source, outputs and stream measurements](../examples/midnight-remix)               | Real operation outputs make timing, dimensions and visual changes inspectable                       | Speech needs listening/sync review; video edit shifts source action; these are not full quality passes  |
| Product still → video                     | [AURORA inputs, prompts and files](../examples/aurora)                                      | In this pair, the guided workflow retained one readable label where the generic video duplicated it | Web-app runs; prompts and still cost differ; one synthetic product and very short clips                 |
| Product editing and reframing             | [All five attempts](../examples/aurora-edits)                                               | One catalog edit met the square requirement; two vertical edits still missed exact placement        | One synthetic product; no broad model ranking                                                           |
| Exact copy and ad export                  | [MP4, editable copy and FFmpeg recipe](../examples/aurora-finished)                         | A deterministic layout delivers exact copy without regenerating accepted media                      | Six-second export includes roughly one second of motion and a hold; source watermark retained           |
| Character continuity                      | [Five authenticated MCP outputs](../examples/nori-character)                                | Added identity detail helped one scene and hurt another; all attempts and 45 credits recorded       | One robot, two scene pairs, no seed control or blind review                                             |
| Thumbnail and editable headline           | [Two authenticated MCP outputs, final cover and small previews](../examples/nori-thumbnail) | A simpler layout removes unrequested visual clutter; the headline is separately editable            | 200 new credits; one pair; no click-through or independent preference measurement                       |
| Brand kit and product listing             | [2K edit, layouts, SVG and PDF guide](../examples/aurora-listing)                           | One image generation supports several composed deliverables                                         | Fictional product; editable composition is local, not an AI vector endpoint                             |
| Narrated explainer                        | [Full MP4, speech, generated motion and timeline](../examples/nori-explainer)               | The full cut combines reused references, narration and generated motion                             | Still holds are included; motion control is imperfect; listening review remains outstanding             |

## Which advanced workflows still need output validation?

Multi-character scenes, new character angles, multi-person face mapping, Character Replace animate mode, music-video generation, body swap, multilingual speech and subtitles still need published output validation. Talking Photo, Lip Sync and Video Editor now have actual outputs in the midnight case, with the specific failed or unreviewed criteria recorded there. Multi-shot identity stability, broader subjects and real-customer coverage also remain outstanding. These examples do not establish end-to-end comparative superiority.

## Do skills improve output over using an MCP directly?

A skill can add reference selection, composition, still review before animation, exact text finishing and recovery decisions around the same tools. The cases above show particular successes and failures. They do not establish a universal improvement, a percentage lift or that Magic Hour beats Higgsfield. The thumbnail case compares our direct prompt with our planned workflow; it is not a run of Higgsfield's skill.

For a fair comparison, keep the brief, source, model/settings, available tools and spending ceiling the same. Record every attempt, including failures, final accepted files, total cost and elapsed time. Hide workflow labels during quality review where practical. Repeat across subjects and runs before reporting a general advantage. Compare finished deliverables, not just whether API requests succeeded.

## How should I cite these results?

Cite the individual case and its run date, settings, output files and limitations. Each case preserves its prompts, source provenance and costs. For a fixed reference, open the case on GitHub and use **Copy permalink** so the URL includes its commit; the branch version can change as evidence improves. Distinguish the observed result from a broader inference.

For example: “Magic Hour's Nori character case (September 10, 2026, as dated in the case) reports mixed results from two paired scene comparisons: added identity wording helped one scene but introduced visible problems in another.” Check the case's own date when citing it; do not treat this index's update date as every experiment's date.

No search ranking, AI citation, activation, retention or revenue lift has been established by these examples. Useful, linked primary evidence makes a claim easier to inspect; it does not guarantee that a search or answer engine will cite it.

[Start with a useful asset](quickstart.md) · [Advanced recipes](../README.md#go-further) · [Workflow questions](workflow-guide.md)
