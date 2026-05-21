# OpenInGoogle User Setup

## What gets installed

The installer adds:

- The OpenInGoogle app
- Start Menu shortcuts
- Right-click menu options for supported Office files
- A credentials folder at `%APPDATA%\OpenInGoogle`
- A help file named `SAVE_YOUR_GOOGLE_CREDENTIALS_HERE.txt`

## Novice credential setup workflow

After installation, the installer opens the credentials folder and a setup guide.

You can also launch the guided setup from the Start Menu:

OpenInGoogle > Setup Google Credentials

The guided setup:

1. Opens the folder where `credentials.json` must be saved.
2. Opens the instruction file.
3. Offers to open the Google Cloud setup pages in your browser.

## Required file

Your Google credential file must be named:

credentials.json

It must be saved here:

%APPDATA%\OpenInGoogle\credentials.json

## Basic use after credentials are added

1. Right-click a Word, Excel, or PowerPoint file.
2. Choose Open in Google Docs, Sheets, or Slides.
3. On first use, approve the Google sign-in request.
