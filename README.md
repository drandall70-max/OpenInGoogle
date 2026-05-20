# Open Microsoft Office Files in Google Docs, Sheets, or Slides

A small Windows 11 utility for people who live in Google Workspace but still receive Microsoft Office files.

This tool uploads a local Microsoft Office file to Google Drive, converts it to the matching Google format, and opens it in your browser.

## Supported files

| Local file type | Opens in |
|---|---|
| `.docx`, `.doc`, `.rtf`, `.txt` | Google Docs |
| `.xlsx`, `.xls`, `.xlsm`, `.csv` | Google Sheets |
| `.pptx`, `.ppt` | Google Slides |

## What it does

1. Takes a local Office file path.
2. Uses the Google Drive API.
3. Uploads the file to your Google Drive.
4. Converts it to Google Docs, Sheets, or Slides.
5. Opens the converted file in your default browser.

## What it does not do

- It does not include my Google credentials.
- It does not collect analytics.
- It does not send files anywhere except your own Google Drive.
- It does not bypass Google OAuth permissions.
- It does not permanently delete your original local file.
- It does not guarantee perfect formatting conversion. Google’s conversion engine controls that.

## Quick start

1. Download the files.
2. Put them in C:\OpenInGoogle.
3. Add your own Google OAuth `credentials.json`.
4. Run `python -m pip install -r requirements.txt`.
5. Right-click an Office file and choose Open in Google Docs.

## Install summary

See `SETUP_WINDOWS_11.md` for the full beginner-friendly setup.

Quick version:

```powershell
cd C:\OpenInGoogle
python -m pip install -r requirements.txt
python .\OpenInGoogle.py "C:\path\to\file.docx"
```

## Security note

You must create your own Google Cloud OAuth desktop credential and save it as:

```text
C:\OpenInGoogle\credentials.json
```

Do not share `credentials.json` or `token.json`.

See `SECURITY_AND_PRIVACY.md`.

## Tip jar

If this saved you time, a small tip is appreciated but absolutely not required.

**Venmo: @drandall70 / https://venmo.com/u/drandall70**
