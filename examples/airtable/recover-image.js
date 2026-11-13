const { projectId: configuredId } = input.config();
if (typeof configuredId !== "string" || !configuredId.trim()) {
  throw new Error("Set projectId to an existing Magic Hour image project ID.");
}
const projectId = configuredId.trim();
let key;
try {
  key = input.secret("MAGIC_HOUR_API_KEY");
} catch {
  throw new Error("Add the MAGIC_HOUR_API_KEY secret to this script.");
}
if (typeof key !== "string" || !key.trim()) {
  throw new Error("Add the MAGIC_HOUR_API_KEY secret to this script.");
}
let response;
try {
  response = await fetch(`https://api.magichour.ai/v1/image-projects/${encodeURIComponent(projectId)}`, {
    method: "GET",
    headers: { Authorization: `Bearer ${key}`, Accept: "application/json" },
    redirect: "error",
  });
} catch {
  throw new Error("Image lookup failed. Keep this project ID and check the connection before another lookup.");
}
if (!response.ok) {
  throw new Error("Image lookup failed. Check the API key and saved project ID.");
}
let project;
try {
  project = await response.json();
} catch {
  throw new Error("Image lookup returned an unreadable response.");
}
if (!project || project.id !== projectId || typeof project.enabled !== "boolean" ||
    !["queued", "rendering", "complete", "error", "canceled", "draft"].includes(project.status) ||
    !Array.isArray(project.downloads)) {
  throw new Error("Image lookup returned an unexpected response.");
}
const download = project.downloads.find((item) => item && typeof item.url === "string" &&
  item.url.startsWith("https://") && typeof item.expires_at === "string" && Date.parse(item.expires_at) > Date.now());
const ready = project.enabled && project.status === "complete" && Boolean(download);
output.set("projectId", projectId);
output.set("status", project.status);
output.set("ready", ready);
if (ready) {
  output.set("downloadUrl", download.url);
  output.set("expiresAt", download.expires_at);
}
