# Security and Privacy

This utility uses the official Google Drive API.

## Google permission used

The script uses this OAuth scope:

```text
https://www.googleapis.com/auth/drive.file
```

That scope is narrower than full Drive access.

## Files you should never share

Do not upload or post these files publicly:

```text
credentials.json
token.json
```

## What gets uploaded

Only the file you choose to open is uploaded to your Google Drive.

## Where the converted file goes

The converted Google Docs, Sheets, or Slides file is created in your Google Drive.

## Formatting

Conversion quality is controlled by Google Drive/Google Workspace.

## Macro warning

Excel macro files like `.xlsm` can be uploaded and converted, but Google Sheets does not preserve Excel VBA macros as runnable Excel macros.
