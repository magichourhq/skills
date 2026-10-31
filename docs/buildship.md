# Recover a Magic Hour image in BuildShip

Source-reviewed setup draft. Native BuildShip execution, secret masking and a BuildShip catalog listing are not yet verified.

Use BuildShip's existing **Starter HTTP** node to retrieve an image project you already created in Magic Hour. This route needs no custom node, package or local server. You need access to a BuildShip workspace, your Magic Hour API key and an existing image project ID from that account.

## Configure the read

Reuse an existing suitable node and secret before adding another. Keep this first check in the workflow editor; it does not need a public trigger or **Ship** deployment.

1. Add **Starter HTTP** from the core node library. Open its **HTTP** settings.
2. Set **Method** to **GET** and **Server URL** to the following, replacing `YOUR_EXISTING_PROJECT_ID` with your actual existing image project ID:

   ```text
   https://api.magichour.ai/v1/image-projects/YOUR_EXISTING_PROJECT_ID
   ```

3. In the node's **Inputs**, add a required string input named `authorization`, titled `Magic Hour authorization`, and mark it sensitive.
4. In the workspace, open that input's expression control (`</>`), choose **Secrets**, then **Add a Secret**. Use the normal Secret Manager to create `MAGIC_HOUR_AUTHORIZATION`. Its private value is the word `Bearer`, one space, then your actual API key. Save it, refresh the secret choices and select that secret for the input. Keep the full value inside Secret Manager, not in source, a chat, a URL or a caller-supplied workflow input.
5. Under **HTTP → Parameters**, add `Authorization` with type **Header**. Use **Variables** to select the node's `authorization` input as its value, and mark the header **Sensitive**. Do not add a request body.

BuildShip documents Secret Manager storage separately from sensitive-field marking. Keep both in place. If the actual UI cannot bind the secret through this normal route, stop there instead of pasting the credential into a static header. Do not share or export resolved secrets or authorization headers.

## Verify the existing project

Save the configuration and check that the secret reference survives reopening the node without revealing its value. Use **Test Node** once with a known completed project ID. This makes a read request; it does not create new media. BuildShip's own execution charges remain separate.

Inspect the node's **Status Code** and **Response**. Success requires HTTP `200`, the expected project `id`, `enabled: true`, `status: complete` and at least one HTTPS download in `downloads` whose `expires_at` is still in the future. Do not forward disabled, nonready or expired output to another step. If you need typed downstream fields, use BuildShip's **Update Output Schema** on the actual successful result, rather than inventing an example response.

For a queued or rendering project, check the same ID later. For an error or canceled project, inspect the reported state. An authentication failure, missing project or failed download is not a reason to create another job.

Download completed media from its returned HTTPS `downloads[].url`, preserving the signed URL exactly. Do not attach your API authorization header to that asset download. Keep signed links private, including any workflow history containing them, and save the actual file in appropriate durable storage before relying on it in an app. If a link expires, retrieve fresh details for the same project ID.

Before adding any creation step later, agree on the tool, inputs and credit budget. Submit once and retain the accepted ID. If acceptance is uncertain, reconcile that request before retrying. Recover polling or download failures through the same ID. Adding a public workflow endpoint, its caller authentication and any catalog submission are separate release steps.

See BuildShip's [Starter HTTP](https://docs.buildship.com/core-nodes/http), [node inputs](https://docs.buildship.com/nodes/input), [Secrets Manager](https://docs.buildship.com/secrets) and [output schema](https://docs.buildship.com/nodes/update-outputs) documentation, and Magic Hour's [Get image details](https://docs.magichour.ai/api-reference/image-projects/get-image-details) reference.
