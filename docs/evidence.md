# Magic Hour skills: output evidence and reproducible examples

Maintained by Magic Hour. Last updated: **2026-09-11 UTC**. This page separates completed output cases from instructions that still need published quality validation. Installing a skill, authenticating an account and completing a job are different from producing an accepted asset.

## What has actually been generated and inspected?

| Case                            | Inspect and reproduce                                                                       | What the case supports                                                                              | Limit                                                                                         |
| ------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Product still → video           | [AURORA inputs, prompts and files](../examples/aurora)                                      | In this pair, the guided workflow retained one readable label where the generic video duplicated it | Web-app runs; prompts and still cost differ; one synthetic product and very short clips       |
| Product editing and reframing   | [All five attempts](../examples/aurora-edits)                                               | One catalog edit met the square requirement; two vertical edits still missed exact placement        | One synthetic product; no broad model ranking                                                 |
| Exact copy and ad export        | [MP4, editable copy and FFmpeg recipe](../examples/aurora-finished)                         | A deterministic layout delivers exact copy without regenerating accepted media                      | Six-second export includes roughly one second of motion and a hold; source watermark retained |
| Character continuity            | [Five authenticated MCP outputs](../examples/nori-character)                                | Added identity detail helped one scene and hurt another; all attempts and 45 credits recorded       | One robot, two scene pairs, no seed control or blind review                                   |
| Thumbnail and editable headline | [Two authenticated MCP outputs, final cover and small previews](../examples/nori-thumbnail) | A simpler layout removes unrequested visual clutter; the headline is separately editable            | 200 new credits; one pair; no click-through or independent preference measurement             |

## Which advanced workflows still need output validation?

The recipes for multi-shot films, multi-character scenes, new character angles, talking portraits, lip sync, multilingual speech, subtitles and generative video edits provide task-specific guidance and use reviewed tool routes. They **do not yet have published end-to-end quality comparisons here**. Broader product, portrait and real-customer coverage is also outstanding. Read each recipe's limits before treating it as evidence for a particular result.

## Do skills improve output over using an MCP directly?

A skill can add reference selection, composition, still review before animation, exact text finishing and recovery decisions around the same tools. The cases above show particular successes and failures. They do not establish a universal improvement, a percentage lift or that Magic Hour beats Higgsfield. The thumbnail case compares our direct prompt with our planned workflow; it is not a run of Higgsfield's skill.

For a fair comparison, keep the brief, source, model/settings, available tools and spending ceiling the same. Record every attempt, including failures, final accepted files, total cost and elapsed time. Hide workflow labels during quality review where practical. Repeat across subjects and runs before reporting a general advantage. Compare finished deliverables, not just whether API requests succeeded.

## How should I cite these results?

Cite the individual case and its run date, settings, output files and limitations. Each case preserves its prompts, source provenance and costs. For a fixed reference, open the case on GitHub and use **Copy permalink** so the URL includes its commit; the branch version can change as evidence improves. Distinguish the observed result from a broader inference.

For example: “Magic Hour's Nori character case (September 10, 2026, as dated in the case) reports mixed results from two paired scene comparisons: added identity wording helped one scene but introduced visible problems in another.” Check the case's own date when citing it; do not treat this index's update date as every experiment's date.

No search ranking, AI citation, activation, retention or revenue lift has been established by these examples. Useful, linked primary evidence makes a claim easier to inspect; it does not guarantee that a search or answer engine will cite it.

[Start with a useful asset](quickstart.md) · [Advanced recipes](../README.md#go-further) · [Workflow questions](workflow-guide.md)
