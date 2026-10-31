---
name: magic-hour-media
description: Create or edit images and video through Magic Hour, or retrieve an existing media project's result.
---

# Create and recover Magic Hour media

Use the tools exposed by the connected Magic Hour MCP server. Inspect their current schemas and use `get_workflow_guide` for the relevant media workflow before choosing an operation.

If the connection needs authorization, direct the user to Kiro's normal Power authorization flow. Keep account credentials and OAuth tokens out of chat, project files and tool arguments. Verify actual API access with `get_account_info`; public discovery alone does not establish authorization.

Reuse the user's supplied media, accepted references and existing budget. Before a charged creation, check current settings and cost against that budget. If the budget or input rights are unclear, resolve the missing detail before spending. Installing this Power does not authorize paid media generation.

For a saved project, retrieve that exact ID without creating another job. For a new creation, retain its accepted ID immediately and wait or retrieve the same project until it reaches a terminal state. If submission acceptance is uncertain, reconcile the account's project history before another paid request. Do not infer failure from a timeout or recreate completed footage to refresh a download URL.

Retrieve and inspect the actual result before reporting completion. Keep normal tool confirmations enabled and distinguish source configuration, authenticated execution and usable output.
