# Connection and input upload

Use the Magic Hour creation MCP at `https://mcp.magichour.ai/`. The separate `https://docs.magichour.ai/mcp` searches documentation and cannot create media. Follow the maintained [MCP user guide](https://github.com/magichourhq/magic-hour-mcp/blob/main/user.md) for client authentication.

If creation tools are unavailable, use the official [Python SDK](https://github.com/magichourhq/magic-hour-python), [Node SDK](https://github.com/magichourhq/magic-hour-node), or direct HTTPS with `MAGIC_HOUR_API_KEY` stored outside source code. Read the [current OpenAPI document](https://docs.magichour.ai/api-reference/openapi.json) before composing a request.

For each local portrait, video, or audio input:

1. Call `video_assets_generate_presigned_url` with its real media type and extension.
2. Upload raw bytes to the returned `upload_url` with an HTTPS `PUT`. Do not add the Magic Hour bearer token to this storage request.
3. Verify the upload, then use the corresponding returned `file_path` in the creation request.

For direct API calls, create with `POST /v1/ai-talking-photo` or `POST /v1/lip-sync`, then poll `GET /v1/video-projects/{id}` using the original ID. Never retry an ambiguous creation POST automatically.
