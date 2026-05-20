# Windows 11 Setup Guide

This guide assumes you are starting from scratch.

## 1. Install Python

1. Go to the official Python website.
2. Download the latest Python 3 version for Windows.
3. During install, check:

```text
Add python.exe to PATH
```

4. Finish the install.

Confirm it works:

```powershell
python --version
```

## 2. Create the local project folder

Create this folder:

```text
C:\OpenInGoogle
```

Copy these files into that folder:

```text
OpenInGoogle.py
requirements.txt
INSTALL_CONTEXT_MENU.ps1
UNINSTALL_CONTEXT_MENU.ps1
```

## 3. Install the Python packages

Open PowerShell and run:

```powershell
cd C:\OpenInGoogle
python -m pip install -r requirements.txt
```

## 4. Create Google Drive API credentials

You need your own Google OAuth desktop app credential.

High-level steps:

1. Go to Google Cloud Console.
2. Create a new project.
3. Enable the Google Drive API.
4. Configure the OAuth consent screen.
5. Create an OAuth Client ID.
6. Choose **Desktop app** as the application type.
7. Download the JSON file.
8. Rename it to:

```text
credentials.json
```

9. Place it here:

```text
C:\OpenInGoogle\credentials.json
```

Do not share this file.

## 5. Test the script manually

Try this with a real local file:

```powershell
cd C:\OpenInGoogle
python .\OpenInGoogle.py "C:\Users\YOURNAME\Desktop\Sample.docx"
```

On the first run, your browser should open a Google sign-in/approval screen.

Approve access.

After that, the script creates:

```text
token.json
```

That token lets the script run again without asking you to sign in every time.

Do not share `token.json`.

## 6. Add right-click menu option

Run PowerShell as your normal user and execute:

```powershell
cd C:\OpenInGoogle
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\INSTALL_CONTEXT_MENU.ps1
```

Now right-click a supported Office file and choose:

```text
Open in Google Docs
```

## 7. Uninstall

To remove the right-click menu:

```powershell
cd C:\OpenInGoogle
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\UNINSTALL_CONTEXT_MENU.ps1
```
