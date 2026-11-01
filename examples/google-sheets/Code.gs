/** @OnlyCurrentDoc */
function onOpen() {
  SpreadsheetApp.getUi().createMenu('Magic Hour')
    .addItem('Recover selected image', 'recoverMagicHourImage_').addToUi();
}

function recoverMagicHourImage_() {
  const ui = SpreadsheetApp.getUi();
  const projectId = SpreadsheetApp.getCurrentCell()?.getDisplayValue().trim();
  const key = PropertiesService.getScriptProperties().getProperty('MAGIC_HOUR_API_KEY');
  if (!projectId || !key) {
    ui.alert('Select one existing image project ID and configure the private script property.');
    return;
  }

  let project;
  try {
    const response = UrlFetchApp.fetch(
      'https://api.magichour.ai/v1/image-projects/' + encodeURIComponent(projectId),
      {
        method: 'get',
        headers: { Authorization: 'Bearer ' + key, Accept: 'application/json' },
        followRedirects: false,
        muteHttpExceptions: true,
        timeoutSeconds: 30,
      },
    );
    if (response.getResponseCode() !== 200) throw new Error();
    project = JSON.parse(response.getContentText());
  } catch {
    ui.alert('Image retrieval failed. Keep the same project ID and check the connection before retrying.');
    return;
  }

  if (project?.id !== projectId || project.enabled !== true) {
    ui.alert('This image project is unavailable. Check its ID and account ownership.');
    return;
  }
  if (project.status !== 'complete') {
    ui.alert('This image is not complete. Check it in Magic Hour; do not create a replacement.');
    return;
  }
  const download = Array.isArray(project.downloads) && project.downloads.find(item =>
    typeof item?.url === 'string' && /^https:\/\/[^/?#@\s]+(?:[/?#]\S*)?$/i.test(item.url) &&
    typeof item.expires_at === 'string' && Date.parse(item.expires_at) > Date.now());
  if (!download) {
    ui.alert('No current download is available. Recover the same project ID again later.');
    return;
  }
  ui.alert('Image ready\nProject: ' + projectId + '\nExpires: ' +
    download.expires_at + '\n\n' + download.url);
}
