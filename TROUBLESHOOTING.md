# Troubleshooting

## Error: Missing credentials.json

Fix:

1. Download your OAuth Desktop App JSON from Google Cloud Console.
2. Rename it to `credentials.json`.
3. Save it in `C:\OpenInGoogle`.

## Browser says app is not verified

This can happen when you create your own Google OAuth app for personal use.

Fix:

- Make sure you are signing in with an account allowed on the OAuth consent screen.
- If the app is in testing mode, add your Google account as a test user.

## ModuleNotFoundError

Fix:

```powershell
cd C:\OpenInGoogle
python -m pip install -r requirements.txt
```

## Permission denied or execution policy error in PowerShell

Run this only for the current PowerShell session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then run the install script again.

## The right-click menu does not show up

Try restarting File Explorer:

1. Open Task Manager.
2. Find Windows Explorer.
3. Right-click it.
4. Choose Restart.

## I want to remove it

Run:

```powershell
cd C:\OpenInGoogle
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\UNINSTALL_CONTEXT_MENU.ps1
```
