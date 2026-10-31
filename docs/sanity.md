# Recover a Magic Hour image into Sanity

Source-reviewed API recipe draft. Native authentication, asset import and Studio selection have not been verified. This is a server-side Content Lake workflow, not a Studio plugin or Exchange listing.

Import an image you already created in Magic Hour into an existing Sanity project. Reuse your server-side workflow and credential store; no new adapter, package or public endpoint is required.

## Before importing

Use an image approved for public distribution. Sanity dataset assets are accessible to anyone with their CDN URL, even when the dataset is private. This recipe does not provide private Media Library asset delivery. Importing also shares the current Magic Hour signed download URL with Sanity.

You need your Magic Hour API credential, an existing image project ID, and a Sanity project/dataset with permission to create asset documents. Keep each service's credential in the server's normal secret store. Never put tokens in request URLs, Studio/frontend configuration, logs or committed files.

## Recover and import once

1. Make one authenticated request to the existing Magic Hour project:

   ```http
   GET https://api.magichour.ai/v1/image-projects/YOUR_EXISTING_PROJECT_ID
   ```

   Use the Magic Hour Bearer credential only for this API request. Require HTTP `200`, the expected `id`, `enabled: true`, `status: complete`, and an HTTPS `downloads[].url` with a future `expires_at`. Preserve the entire signed URL. If the project is disabled, unfinished or failed, stop before import. Recover an expired link from the same project ID; do not create new media.

2. Reuse a saved Sanity asset reference if this project was imported previously. Otherwise send the selected URL to Sanity using its separate Bearer credential and `Content-Type: application/json`:

   ```http
   POST https://YOUR_SANITY_PROJECT_ID.api.sanity.io/v2024-06-24/assets/images/YOUR_DATASET/from-url?sourceName=magic-hour&sourceId=YOUR_EXISTING_PROJECT_ID
   ```

   Replace project/dataset placeholders with the intended destination and URL-encode query values. The body is:

   ```json
   {"url": "CURRENT_HTTPS_DOWNLOAD_URL"}
   ```

   Replace the body value with the complete current download URL from step 1. Do not send the Magic Hour API header to Sanity or to the media URL. Keep the signed URL out of attribution metadata such as `sourceUrl`.

3. Require HTTP `200` and a nonempty `document._id`, then retain that asset ID alongside the Magic Hour project ID in your existing workflow. That ID is the durable asset reference. Select the imported asset through the normal Studio image-field asset picker. Importing an asset does not update or publish a content entry.

Sanity's from-URL endpoint accepts images up to 50 MiB and a JSON body up to 4 KiB. Its source fetch can take 300 seconds, so allow more than 300 seconds for the request and ensure the signed link remains valid long enough. Check project quota and upload permissions through normal account controls.

## Recover uncertain acceptance

If an import times out or the connection closes, inspect the target dataset before any retry. The asset may already exist. Use the saved reference or query the persisted asset fields `source.name` (`magic-hour`) and `source.id` (the original Magic Hour project ID), then retain the actual asset ID. Upload parameters `sourceName`/`sourceId` populate those fields; they are not an idempotency key. Do not blindly rerun the import or recreate the Magic Hour image.

The first native verification should use one authorized existing image and one approved import, then confirm the returned asset and normal Studio selection. Keep content publishing, a custom Studio asset-source UI and Exchange admission separate.

See Magic Hour's [Get image details](https://docs.magichour.ai/api-reference/image-projects/get-image-details), Sanity's [Assets API](https://www.sanity.io/docs/http-reference/assets) and [dataset asset visibility](https://www.sanity.io/docs/content-lake/assets) documentation.
