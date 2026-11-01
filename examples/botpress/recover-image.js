workflow.magicHourReady = false
workflow.magicHourStatus = ''
workflow.magicHourDownloadUrl = ''
workflow.magicHourExpiresAt = ''

const projectId = workflow.magicHourProjectId
if (typeof projectId !== 'string' || !projectId.trim()) {
  throw new Error('Set magicHourProjectId to an existing Magic Hour image project ID.')
}
if (!env.MAGIC_HOUR_API_KEY) {
  throw new Error('Set MAGIC_HOUR_API_KEY in Botpress Configuration Variables.')
}

try {
  const response = await axios.get(
    `https://api.magichour.ai/v1/image-projects/${encodeURIComponent(projectId)}`,
    {
      headers: { Authorization: `Bearer ${env.MAGIC_HOUR_API_KEY}` },
      timeout: 15000,
      maxRedirects: 0,
    }
  )
  const project = response.data
  if (response.status !== 200 || project?.id !== projectId ||
      typeof project.enabled !== 'boolean' || typeof project.status !== 'string') {
    throw new Error('Unexpected image project response.')
  }

  workflow.magicHourStatus = project.status
  if (project.enabled && project.status === 'complete' && Array.isArray(project.downloads)) {
    const download = project.downloads.find((item) =>
      typeof item?.url === 'string' && /^https:\/\/[^/?#@\s]+(?:[/?#]\S*)?$/.test(item.url) &&
      typeof item.expires_at === 'string' && Date.parse(item.expires_at) > Date.now()
    )
    if (download) {
      workflow.magicHourDownloadUrl = download.url
      workflow.magicHourExpiresAt = download.expires_at
      workflow.magicHourReady = true
    }
  }
} catch {
  throw new Error('Magic Hour image lookup failed. Keep the same project ID and check configuration privately.')
}
