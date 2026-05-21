# Security and Privacy

OpenInGoogle uses the official Google Drive API.

## OAuth scope

```text
https://www.googleapis.com/auth/drive.file
```

## Files not to share

```text
credentials.json
token.json
```

## What gets uploaded

Only the file you choose to open is uploaded to your Google Drive. The original local file is not deleted or modified.

## Where credentials are stored

```text
%APPDATA%\OpenInGoogle\credentials.json
%APPDATA%\OpenInGoogle\token.json
```

## Developer access

Files are uploaded directly from your computer to your own Google Drive. The developer does not receive or store your files.
