# Recover an existing Magic Hour image from Google Sheets

Use a manual menu action in a private, owner-only spreadsheet to read one existing image project and show its current download link. The action does not write cells, download media, generate an image or run from a formula.

Source-reviewed example. Apps Script authorization, saved-property behavior, native menu execution and result-dialog usability have not been verified.

## Keep the credential boundary private

Use a spreadsheet and bound script that only you can access. Do not use a shared team sheet, published sheet or shared drive. Bound scripts inherit their spreadsheet's access list, so an editor can change the code and access its credentials.

This example uses **Script Properties**, which are shared by the users of that script. They are not a per-user secret vault. Do not add collaborators, share, publish or copy the credential-bearing file/project. Before any sharing or copying, remove the key and review the new destination's access. Do not assume a copy safely drops stored properties.

A multi-user integration needs a separately reviewed credential/account connection. Do not adapt this private example by sharing one owner's key.

## Set up the private bound script

Confirm in **Project Settings** that the project already uses the **V8 runtime** before adding or running this example. This recipe does not change runtime settings, manifests or security controls.

1. In your private spreadsheet, open **Extensions → Apps Script**. Add [Code.gs](../examples/google-sheets/Code.gs). Preserve existing code and menus; if your project already has `onOpen`, combine only the menu-creation statements rather than replacing that function.
2. In Apps Script, open **Project Settings → Script Properties → Add script property**. Set **Property** to `MAGIC_HOUR_API_KEY` and **Value** to your [Magic Hour API key](https://magichour.ai/developer?tab=api-keys), then save. Enter the key only in this private setting, never in a cell, formula, source file or log.
3. Save the script and reopen the spreadsheet to load **Magic Hour → Recover selected image**. Opening the file only adds the menu; it does not read the key or call the API.
4. Put one existing image-project ID in a cell and select that cell. Use the ID owned by the connected Magic Hour account, not a URL. Start with an already completed project.
5. Choose **Magic Hour → Recover selected image**. Complete Google's normal authorization flow if requested, reviewing the current-spreadsheet and external-request permissions. Keep Workspace/admin restrictions and required confirmations; do not bypass them.

Google documents [bound-script access](https://developers.google.com/apps-script/guides/bound), [manual Script Properties](https://developers.google.com/apps-script/guides/properties), [menu actions](https://developers.google.com/apps-script/guides/menus) and [authorization](https://developers.google.com/apps-script/guides/services/authorization).

## What the action checks

Each menu invocation makes one `GET` to `https://api.magichour.ai/v1/image-projects/{encodedId}` using `UrlFetchApp`. It disables redirects, keeps normal HTTPS certificate validation and uses a 30-second request limit. It does not send the credential to a media URL.

A link is shown only for HTTP `200`, the expected project `id`, `enabled: true`, `status: complete`, and a returned HTTPS download whose `expires_at` is still in the future. For projects with multiple downloads, it selects the first currently usable one.

Other states and failed requests produce a fixed message without exposing a raw response or server error. The result is a plain dialog containing only the project ID, expiration and selected signed link. No result is written to the spreadsheet or logged. The link can grant access to private media, so do not share the dialog, a screenshot or its URL with someone who is not allowed to receive the asset.

If the request fails or a link expires, keep the original project ID and invoke recovery again when appropriate. Do not generate a replacement image. There is no polling loop, schedule or automatic retry.

## Use the menu, not a formula

The network handler is named `recoverMagicHourImage_`. Google reserves trailing-underscore functions as private and does not allow them as cell custom functions. Its official [menu sample](https://github.com/googleworkspace/apps-script-samples/blob/1f297d16fdb72f819ae27eb1b07b9fa3bae9103e/solutions/automations/equipment-requests/Code.js) uses the same private-handler pattern.

Custom functions have different authorization behavior, and `getUserProperties()` in a formula reads the spreadsheet owner's properties. Do not turn this action into a formula or claim it isolates collaborators' keys. See Google's [custom-function restrictions](https://developers.google.com/apps-script/guides/sheets/functions).

This is a private bound-script example, not a Workspace Marketplace add-on or a verified installation. Native credential isolation, one same-ID response, secret/log behavior and usable dialog output remain verification gates. No public deployment or catalog acceptance is claimed.
